from django.contrib import admin
from .models import Article

class articleAdmin(admin.ModelAdmin):
	list_display = ("block","title","content","create_timestamp","last_update_timestamp")

admin.site.register(Article,articleAdmin)