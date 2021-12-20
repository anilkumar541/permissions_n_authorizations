from django.urls import path
from myapp import views


urlpatterns = [
    path("category/", views.CategoryListView.as_view()),
    path("post/category/", views.CategoryCreateView.as_view()),
    path("product/", views.ProductListView.as_view()),
    path("post/product/", views.ProductCreateView.as_view()),
]
