from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from ..models import Category
from ..serializers import CategorySerializer

class CategoryListView(ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def perform_create(self, serializer):
		serializer.validated_data['user_created'] = self.request.user.username
		serializer.validated_data['user_updated'] = self.request.user.username
		return super(ListCreateAPIView, self).perform_create(serializer)

class CategoryDetail(RetrieveUpdateDestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

	def perform_update(self, serializer):
		serializer.validated_data['user_updated'] = self.request.user.username
		return super(CategoryDetail, self).perform_update(serializer)
