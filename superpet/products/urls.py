from django.urls import path
from .import views

urlpatterns = [
    path('',views.ProductListView.as_view(),name="products"),
    path('royal-Canin/',views.royalCanin,name="royalCanin"),
    path('Pedigree/',views.pedigree,name="Pedigree"),
    path('Drools/',views.drools,name="Drools"),
    path('search/',views.search,name="search"),
    path('<int:pk>/',views.ProductDetailView.as_view(),name="product-detail"),
    path('create-product/',views.ProductCreateView.as_view(),name="create-product"),
    path('update-product/<int:pk>/',views.productUpdateView.as_view(),name="product-update"),
    path('delete-product/<int:pk>/',views.productDeleteView.as_view(),name="delete-product"),
    path('<slug:slug>/',views.CategoryDetailView.as_view(),name="category-detail")
] 