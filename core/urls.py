from django.urls import path, reverse_lazy, include
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('auth/', include('core.authurls')),
    path('', views.HomeView.as_view(), name='home'),
    path('all/', views.AllListView.as_view(), name='all'),
    path('myproduct/', login_required(views.MyProductView.as_view()), name='my_products'),
    path('add/', views.login_required(views.AddProduct.as_view()), name='add'),
    path('detail/<int:pid>', views.MyDetailView.as_view(), name='detail'),
    path('<int:pid>', views.CategoryListView.as_view(), name='category'),

]

