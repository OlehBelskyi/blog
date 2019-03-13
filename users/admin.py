from django.contrib import admin
from users.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    search_fields = ['email']

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
