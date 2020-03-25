from django.urls import include, path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='products'),
    path('products/<int:product_id>/', views.get_product, name='product'),
    path('categories/', views.list_categories, name='categories'),
    path('categories/<int:category_id>/', views.get_category, name='category'),
    path('categories/<int:category_id>/products/', views.category_products, name='products by category')
]