from django.urls import path
from .import views

urlpatterns = [
    path("",views.index,name="index"),
    path('about/',views.about,name="about"),
    path('about/index',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('BALI/',views.BALI,name='BALI'),
    path('GREECE/',views.GREECE,name='GREECE'),
    path('MALDVIES/',views.MALDVIES,name='MALDVIES'),
    path('about/register',views.register,name='register'),
]