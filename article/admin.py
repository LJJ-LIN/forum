from django.contrib import admin
from .models import Article,Comment

class articleAdmin(admin.ModelAdmin):
	list_display = ("block","title","content","create_timestamp","last_update_timestamp")

class commentAdmin(admin.ModelAdmin):
	list_display = ("owner","article","content","create_timestamp","last_update_timestamp")
		

admin.site.register(Article,articleAdmin)
admin.site.register(Comment,commentAdmin)