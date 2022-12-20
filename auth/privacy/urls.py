from rest_framework import routers
from .views import PlaceViewSet
from privacy import views
from django.urls import path

router = routers.SimpleRouter()
router.register(r'', views.PlaceViewSet,basename='place'),

urlpatterns = [
   
    
]

urlpatterns += router.urls