from django.urls import path, include
from rest_framework import routers
from webservices.views import *
from home.models import *

router=routers.DefaultRouter()
router.register(r'productos',producto_viewset) #url del servicio, llama un viewset
router.register(r'marcas',marca_viewset) #url del servicio
router.register(r'catergorias',categoria_viewset) #url del servicio

urlpatterns=[
	path('api/',include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), # faltaaaaaa

]