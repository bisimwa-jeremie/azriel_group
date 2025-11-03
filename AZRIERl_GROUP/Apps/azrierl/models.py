from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)
from django.utils import timezone
# from AZRIERl_GROUP.Apps.Manager.models import BaseModelpro


class CustomUserManager(BaseUserManager):
    """Manager personnalisé pour le User afin de permettre create_user et create_superuser."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'email doit être renseigné')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superuser doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superuser doit avoir is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """Modèle utilisateur personnalisé basé sur l'email."""
    email = models.EmailField('email', unique=True)
    first_name = models.CharField('prénom', max_length=150, blank=True)
    last_name = models.CharField('nom', max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'utilisateur'
        verbose_name_plural = 'utilisateurs'

    def __str__(self):
        return self.email


# ------------------------------------------------------------------
# Modèles pour AZRIERL GROUP
# ------------------------------------------------------------------

class ActivityCategory(models.Model):
    """Catégorie générale d'activités (ex: Construction, Agriculture, Imprimerie...)."""
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Catégorie d\'activité'
        verbose_name_plural = 'Catégories d\'activités'

    def __str__(self):
        return self.name


class Activity(models.Model):
    """Activité précise rattachée à une catégorie (ex: Construction des bâtiments)."""
    category = models.ForeignKey(ActivityCategory, on_delete=models.PROTECT, related_name='activities')
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Activité'
        verbose_name_plural = 'Activités'

    def __str__(self):
        return f"{self.title} ({self.category.name})"


class CompanyManager(models.Manager):
    """Manager personnalisé pour Company avec méthodes utilitaires persistantes."""

    def create_company(self, name, **kwargs):
        """Création rapide d'une entreprise.
        Ex: Company.objects.create_company(name='AZRIERL GROUP', ...)
        """
        company = self.model(name=name, **kwargs)
        company.save(using=self._db)
        return company

    def active_companies(self):
        return self.filter(is_active=True)


class Company(models.Model):
    """Représentation persistante de la société et ses zones d'activités."""
    name = models.CharField(max_length=255, unique=True)
    legal_form = models.CharField(max_length=50, blank=True, default='SARL')
    slogan = models.CharField(max_length=255, blank=True)
    mission = models.TextField(blank=True)
    vision = models.TextField(blank=True)
    established_date = models.DateField(null=True, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    activities = models.ManyToManyField(Activity, blank=True, related_name='companies')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CompanyManager()

    class Meta:
        verbose_name = 'Société'
        verbose_name_plural = 'Sociétés'

    def __str__(self):
        return self.name


# Optionnel: modèle pour stocker engagements / forces / zones d'activités détaillées
class CompanySection(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        verbose_name = 'Section société'
        verbose_name_plural = 'Sections société'

    def __str__(self):
        return f"{self.company.name} - {self.title}"
