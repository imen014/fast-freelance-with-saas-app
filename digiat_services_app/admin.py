from django.contrib import admin
from .models import DigitalService, Transaction, Offre


admin.site.register(DigitalService)
admin.site.register(Transaction)
admin.site.register(Offre)