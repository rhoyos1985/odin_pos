from django.contrib import admin
from .models import Category, SubCategory

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('code', 'description', 'user_created')
	action = None

	def save_model(self, request, obj, form, change):

		if change:
			obj.user_updated = request.user.username
		else:
			obj.user_created = request.user.username
			obj.user_updated = request.user.username

		super().save_model(request, obj, form, change)

class SubCategoryAdmin(admin.ModelAdmin):
	list_display = ('code', 'description', 'category', 'user_created')
	action = None

	def save_model(self, request, obj, form, change):

		if change:
			obj.user_updated = request.user.username
		else:
			obj.user_created = request.user.username
			obj.user_updated = request.user.username

		super().save_model(request, obj, form, change)

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
