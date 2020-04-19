from django.contrib import admin
from .models import MenuModel

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
	list_display = ('name', 'url', 'user')
	action = None

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		obj.save()

admin.site.register(MenuModel, MenuAdmin)
