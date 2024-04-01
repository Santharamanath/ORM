from django.contrib import admin
from .models import bookdetails,bookdetailsAdmin
Admin.site.register(bookdetails,bookdetailsAdmin)
