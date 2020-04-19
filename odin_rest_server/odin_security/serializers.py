from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import MenuModel

class MenuSerializer(serializers.ModelSerializer):
	children = RecursiveField(many=True)

	class Meta:
		model = MenuModel
		fields = ('id','name','url','parent','children')
