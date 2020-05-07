from django.contrib import admin
from Blogging.models import Blog, UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Blog)


