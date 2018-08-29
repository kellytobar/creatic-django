from rest_framework import serializers
from home.models import *

class producto_serializer(serializers.HyperlinkedModelSerializer): #con hyperlinked se basa en el modelo y lo va a serializar
#class producto_serializer(serializers.ModelSerializer): #hay que hacer una consulta adicional
	class Meta:
		model=Producto
		fields=('url','id','nombre','precio','foto','status','marca')


class marca_serializer(serializers.HyperlinkedModelSerializer): #con hyperlinked se basa en el modelo y lo va a serializar
	class Meta:
		model=Producto
		fields=('url','id','nombre')
		
class categoria_serializer(serializers.HyperlinkedModelSerializer): #con hyperlinked se basa en el modelo y lo va a serializar
	class Meta:
		model=Producto
		fields=('url','nombre')