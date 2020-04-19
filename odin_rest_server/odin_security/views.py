from django.shortcuts import render
from rest_framework.generics import ListAPIView

from django.db.models import Prefetch
from .models import MenuModel
from .serializers import MenuSerializer

# Create your views here.
class MenuList(ListAPIView):
	serializer_class = MenuSerializer

	def get_queryset(self):
		groups = self.request.user.groups.all()
		queryset = MenuModel.objects.filter(parent__isnull=True, group__in=groups)
		return queryset
