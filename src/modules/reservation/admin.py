from django.contrib import admin
from modules.reservation import models


admin.site.register(models.UserProfile)
admin.site.register(models.Coach)
admin.site.register(models.Event)
