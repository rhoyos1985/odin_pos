from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView

from ..models import SubCategory
from ..serializers import SubCategorySerializer

class SubCategoryListView(ListCreateAPIView):
	queryset = SubCategory.objects.all()
	serializer_class = SubCategorySerializer

	def perform_create(self, serializer):
		serializer.validated_data['user_created'] = self.request.user.username
		serializer.validated_data['user_updated'] = self.request.user.username
		return super(SubCategoryListView, self).perform_create(serializer)

class SubCategoryDetail(RetrieveUpdateDestroyAPIView):
	queryset = SubCategory.objects.all()
	serializer_class = SubCategorySerializer

	def perform_update(self, serializer):
		serializer.validated_data['user_updated'] = self.request.user.username
		return super(SubCategoryDetail, self).perform_update(serializer)
