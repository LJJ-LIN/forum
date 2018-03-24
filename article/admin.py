from django.contrib import admin
from .models import Article,Comment

class CommentInline(admin.TabularInline):
	model = Comment
	can_delete = True
		

class articleAdmin(admin.ModelAdmin):
	list_display = ("block","title","content","create_timestamp","last_update_timestamp")
	inlines = [CommentInline]
	actions = ['make_picked']
	fieldsets = (
		('基本',{
			"classes":('wide',),
			"fields":("title","content")
			}),
		('高级',{
			"classes":('collapse',),
			"fields":("status",)
			})
		)

	def make_picked(modeladmin, request, queryset):
		for a in queryset:
			a.status = 10
			a.save()
	make_picked.short_description = "设置精华"

class commentAdmin(admin.ModelAdmin):
	list_display = ("owner","article","content","create_timestamp","last_update_timestamp")
		

admin.site.register(Article,articleAdmin)
admin.site.register(Comment,commentAdmin)
