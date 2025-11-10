from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

# Importer les modèles définis dans ce module (ou depuis .models selon usage)
from .models import User, Company, ActivityCategory, Activity, CompanySection


class ActivityInline(admin.TabularInline):
    model = Company.activities.through
    extra = 1


class CompanySectionInline(admin.StackedInline):
    model = CompanySection
    extra = 0
    min_num = 0


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'legal_form','slogan','mission','vision','is_active', 'phone', 'email','address',)
    search_fields = ('name', 'slogan', 'mission','vision','address')
    list_filter = ('is_active',)
    inlines = [CompanySectionInline, ActivityInline]


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', 'description')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'summary')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')  
    search_fields = ('email','first_name','last_name')  


@admin.register(CompanySection)
class CampanySectionAdmin(admin.ModelAdmin):
    list_display = ('company','title', 'content')
    list_filter = ('company', 'content')
    search_fields = ('company','title','content')


class CustomUserAdmin(BaseUserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
