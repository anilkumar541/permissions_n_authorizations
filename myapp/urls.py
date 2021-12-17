from django.urls import path
from myapp import views


urlpatterns = [
    path("category/", views.CategoryListCreateView.as_view()),
    path("category/<int:pk>/", views.CategoryRUDView.as_view()),
    path("product/", views.ProductListCreateView.as_view()),
    path("product/<int:pk>/", views.ProductRUDView.as_view()),
]
