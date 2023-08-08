from django.contrib import admin
from contact.models import contactDetails

class contactDetaisAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile', 'message')

admin.site.register(contactDetails, contactDetaisAdmin)

# Register your models here.
