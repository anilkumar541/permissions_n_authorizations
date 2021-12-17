from django.db.models import query
from django.shortcuts import render

# Create your views here.
from myapp.models import Category, Product
from myapp.serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import PermissionDenied
            

class CategoryListCreateView(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def check_permission(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        
        if request.method =="GET":
            if self.request.user.has_perm("myapp.view_category"):
                pass
            else:
                raise PermissionDenied


        elif (request.method == 'POST'):
            if self.request.user.has_perm("myapp.add_category"):
                pass
            else:
                raise PermissionDenied
        
           
    # def get_queryset(self):
    #     user = self.request.user
    #     if (user.is_superuser or user.is_admin or user.is_active):
    #         queryset = Category.objects.all()
    #     else:
    #         queryset = Category.objects.filter(user=user)
    #     return queryset









class CategoryRUDView(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductListCreateView(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer    

class ProductRUDView(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer        


        