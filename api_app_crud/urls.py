from django.urls import path
from . import views

urlpatterns = [
    path('',views.api_overview, name = 'api_overview'),
    path('product-list/',views.show_products, name = 'show_products'),
    path('product-detail/<int:pk>/',views.show_product_detail, name = 'show_product_detail'),
    path('product-create/',views.create_product, name = 'create_product'),
    path('product-update/<int:pk>/',views.update_product, name = 'update_product'),
    path('product-delete/<int:pk>/',views.delete_product, name = 'delete_product')



]