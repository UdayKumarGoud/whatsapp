from django.contrib import admin
from .models import Token, AppUser
from django.contrib.auth.hashers import make_password

# Register your models here.

class TokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')
    fields = ('user',)
    ordering = ('-created',)

admin.site.register(Token, TokenAdmin)
# admin.site.register(AppUser)

@admin.register(AppUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'mobile', 'email', 'last_login', 'is_active', 'is_logged_in',]
    list_display_links = ['id', 'mobile', 'email']
    # list_filter = ['mobile', 'email', 'first_name', 'ssn_number']
    search_fields = ['mobile', 'first_name']
    
    def save_model(self, request, obj, form, change):
        password = form.cleaned_data.get('password')
        if password:
            obj.password = make_password(password)
        obj.save()
        super().save_model(request, obj, form, change)
