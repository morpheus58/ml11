from django.contrib import admin
from .models import Books, Prices, Authors
# Register your models here.
admin.site.register(Books)
admin.site.register(Prices)
admin.site.register(Authors)
