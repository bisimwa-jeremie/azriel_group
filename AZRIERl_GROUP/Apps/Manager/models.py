from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

# Create your models here.
class Deletequery(models.QuerySet):
    def delete(self):
        return super().delete(delete_at = datetime.now())

class Mymanager(models.Manager):
    def get_queryset(self):
        return Deletequery(self.model, using=self._db).filter(delete_at=None)
    
class BaseModelpro(models.Model):
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    create_by = models.ForeignKey("bmtapp.User", on_delete=models.CASCADE, null=True)
    delete_at = models.DateTimeField(auto_now=True)
    update_at = models.DateField(auto_now=True)

    objects = Mymanager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.delete_at=datetime.now()
        self.save
