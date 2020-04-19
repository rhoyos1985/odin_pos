from rest_framework import serializers

from ..models import Category
from .subcategory_serializer import SubCategorySerializer

class CategorySerializer(serializers.ModelSerializer):
	subcategories = SubCategorySerializer(many=True)

	class Meta:
		model = Category
		fields = ('code','description','subcategories')
