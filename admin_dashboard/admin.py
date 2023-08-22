from django.contrib import admin
from admin_dashboard.models import AdminUser
# Register your models here.
# admin.site.register(AdminUser)

@admin.register(AdminUser)
class CustomAdminUser(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'is_staff', 'is_superuser',]
    
    # # def save_model(self, request, obj, form, change):
    # #     if change and 'username' in form.changed_data:
    # #         obj.set_password(form.cleaned_data['password'])
    # #     super().save_model(request, obj, form, change)
    
    # # def save_model(self, request, obj, form, change):
    # #     password = form.cleaned_data.get('password')
    # #     if password:
    # #         obj.password = make_password(password)
    # #     obj.save()
    # def save_model(self, request, obj, form, change):
    #     # Check if this is a new user
    #     if not change:
    #         # Create a new password for the user
    #         password = make_password(obj.password)
    #         # Set the password for the user
    #         obj.password = password
    #     # Otherwise, don't allow changing the password
    #     else:
    #         obj.password = AdminUser.objects.get(id=obj.id).password
    #         # print(obj.password)
    #     # Call the parent save_model method
    #     super().save_model(request, obj, form, change)

# # admin.site.unregister(Group)
