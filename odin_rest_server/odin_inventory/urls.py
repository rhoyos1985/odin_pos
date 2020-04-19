from django.urls import path


from . import views

app_name = 'odin_inventory'

urlpatterns = [
	path('categorias/', views.CategoryListView.as_view(), name='category-list'),
	path('categorias/<int:pk>', views.CategoryDetail.as_view(), name='category-detail'),
	path('subcategorias/', views.SubCategoryListView.as_view(), name='subcategory-list'),
	path('subcategorias/<int:pk>', views.SubCategoryDetail.as_view(), name='subcategory-detail'),
]
