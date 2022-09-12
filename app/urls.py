from atexit import register

from django.contrib import admin
from django.urls import path,include
from app import views
from rest_framework.routers import DefaultRouter


'''router = DefaultRouter()
router.register('pro',views.ProductsViewsetAPI, basename="products")'''

urlpatterns =[

    
    path('clsapi',views.ProductsclassAPI.as_view() ,name="clsAPI"),
    path('clsapi/<id>',views.ProductsclassAPI.as_view() ,name="clsAPI"),
   
    
]


'''

    path('',views.home , name = "home"),

    #Function based API ==========================================================================

    path('funapi/',views.Pruduct_list_or_create , name="listpost"),
    path('funapi/<id>/',views.Pruduct_get_put_delete , name="listpost"),
    

    #class based API ==============================================================================
     

    #creating router obj 
    
    path('clsapi',views.ProductsclassAPI.as_view() ,name="clsAPI"),
    path('clsapi/<id>',views.ProductsclassAPI.as_view() ,name="clsAPI"),

    


   
   #Generic Based API==============================================================================
urlpatterns = router.urls

    path('genapi',views.genericAPI_list_create.as_view()),
    path('genapi/<id>/',views.genericAPI_update_delete.as_view()),  #GenMixAPI_list_create


     
    # GenricMixins Based API ===========================================================================
    path('genmixapi',views.GenMixAPI_list_create.as_view()),
    path('genmixapi/<int:pk>/',views.GenMixAPI_update_put_delete.as_view()),  #<int:pk>
  

  #view set 
    path('view/',include(router.urls)),


'''

