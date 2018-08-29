from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Marca (models.Model):
	nombre = models.CharField(max_length=100) # char, el id lo pone django

	def __str__(self):
		return self.nombre

class Categoria (models.Model):
	nombre = models.CharField(max_length=100) # char, el id lo pone django

	def __str__(self):
		return self.nombre


class Producto (models.Model):
	nombre = models.CharField(max_length=100) # char, el id lo pone django
	precio = models.IntegerField() 
	stock = models.IntegerField()
	status = models.BooleanField(default=True) # que por defecto tenga el valor de true, cada que agregue un producto
	foto = models.ImageField(upload_to='fotos', null=True, blank=True) # que se suba y la url donde esta, que se pueda no tener foto
	marca = models.ForeignKey(Marca, on_delete=models.PROTECT)#el modelo se llama marca, relacion producto con marca de uno a muchos, que no me elimine en cascada 
	categoria = models.ManyToManyField(Categoria,  null =True, blank =True)

	#la funcion que vamos a retorno
	def __str__(self): #unicode
		return self.nombre + str(self.precio)


class Perfil(models.Model):
	GENERO=( ('femenino','Femenino'),  #tupla no se puede editar
			('masculino','Masculino'),
	) #una se va a ir a formu, otra a bd
	image=models.ImageField(upload_to='perfiles', null=True, blank=True) #se va a guardar en la carpeta perfiles
	#la imagen no es obligatoria pero el telefono si
	telefono=models.CharField(max_length=100)
	genero=models.CharField(max_length=15, choices=GENERO)
	#la idea es no crear tabla genero para dos generos
	user= models.OneToOneField(User, on_delete=models.PROTECT) #Para que no me elimine en cascada

	def __str__(self):
		return self.telefono + '' + str(self.user.username)
		#self.user que tipo de datova a ser una llave foranea, debe tener el mismo tipo y longitud de llave primaria
		#self.user a a guardar un entero
		# yo puedo concatenar texto


