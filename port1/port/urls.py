from django.urls import path
from . import views
urlpatterns = [

    path('',views.makeport,name="makeport"),
    path('show/',views.showport,name="showport"),
    path('showfull/<int:pk>',views.showfullport,name="fullport"),
]
