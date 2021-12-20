
from myapp.models import Category, Product
from myapp.serializers import CategorySerializer, ProductSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.exceptions import PermissionDenied





class CategoryListView(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
class CategoryCreateView(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    
    def check_permissions(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied
        if not request.user.has_perm("myapp.add_category"):
            raise PermissionDenied

  
class ProductListView(ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer    

class ProductCreateView(CreateAPIView):  
    queryset=Product.objects.all()
    serializer_class=ProductSerializer  

    def check_permissions(self, request):
        if not request.user.is_authenticated:
            raise PermissionDenied

        if not request.user.has_perm("myapp.add_product"):
            raise PermissionDenied    
        



            




