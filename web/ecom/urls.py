from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="indexecom"),
    path('about/', views.about,name="about"),
    path('contact/', views.contact,name="contact"),
    path('tracker/', views.tracker,name="tracking"),
    path('search/', views.search,name="search"),
    path('products/<int:id>', views.productview,name="productview"),
    path('cheakout/', views.cheakout,name="cheakout"),
]
