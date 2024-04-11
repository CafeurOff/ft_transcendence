from django.contrib import admin
from .models import User, Game, Friend

admin.site.register(User)
admin.site.register(Game)
admin.site.register(Friend)

admin.site.site_header = 'Transcendence Administration'
admin.site.site_title = 'Transcendence Administration'

