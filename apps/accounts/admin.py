from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html

from apps.accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from apps.accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    # Campos a mostrar en la lista de usuarios
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_worker",
        "display_image",  # Campo personalizado para mostrar la imagen
        "is_staff",
        "is_active",
    ]
    
    # Campos a mostrar en el formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('image','is_worker')}),
    )
    
    # Campos requeridos al crear usuario
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {
            'fields': ('image','is_worker'),
        }),
    )
    
    
    # Método para mostrar la imagen en la lista
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "Sin imagen"
    display_image.short_description = 'Imagen'

admin.site.register(CustomUser, CustomUserAdmin)