from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import *
from .models import *

from django.http import HttpResponse
from django.core import serializers

# Create your views here.

def quienes_somos_view(request):
	nombre='Juana la loca'
	lista=[1,2,3,4,5,6]
	#return render(request,'quienes_somos.html',{'n':nombre}) #un diccionario
	return render(request,'quienes_somos.html',locals())

def contacto_view(request):
	email=""
	subject=""
	text=""
	info_enviado=False
	if request.method=='POST':
		formulario =contacto_form(request.POST) #cuando se le de clic en enviar
		if formulario.is_valid():  # saco la infor del form en variables
			email=formulario.cleaned_data['correo']
			subject=formulario.cleaned_data['asunto']
			text=formulario.cleaned_data['texto']
			info_enviado=True
		else:
			msg='la informacion no es correcta'
	else:
		formulario=contacto_form()

	#formulario=contacto_form() #asi se llama la clase del form
	return render(request,'contacto.html',locals())


def index_view(request):
	return render(request,'index.html')

def nuestros_servicios_view(request):
	return render(request,'nuestros_servicios.html')


def lista_productos_view(request):
	lista=Producto.objects.filter(status=True)
	#lista=Producto.objects.filter()
	return render(request,'lista_productos.html',locals())

def agregar_producto_view(request): 
	if request.user.is_authenticated and request.user.is_superuser:
		if request.method=='POST':
			formulario=agregar_producto_form(request.POST, request.FILES) #me recibe los archivos
			if formulario.is_valid():
				formulario.save()  #me guarda en la bd, es como el insert, guarda en bd y en RAM
				return redirect('/lista_productos') #me redirecciona  a esta pagina
			else:
				msj:"hay datos no validos"
		else:	
			formulario=agregar_producto_form()
		return render(request,'agregar_producto.html',locals())


def ver_producto_view(request, id_prod): #le paso el mismo nombre del parametro que esta en la url
	try:
		obj=Producto.objects.get(id=id_prod) #obtenga un objeto de producto segun su id y guardelo en la variable

	except:
		print("error en la consulta EL PRODUCTO NO EXISTE")
		msj="error en la consulta EL PRODUCTO NO EXISTE"
	return render(request,'ver_producto.html',locals())


def editar_producto_view(request, id_prod): #le paso el mismo nombre del parametro que esta en la url
		#no hay necesidad de crear html
	#hago la consulta
	obj=Producto.objects.get(id=id_prod) # ya me deberia cargar la info
	if request.method=='POST':   #paso la info que viene desde el POST
		formulario=agregar_producto_form(request.POST, request.FILES, instance=obj)
		if formulario.is_valid():
			#formulario.save(commit =False) #solo guarda en RAM 
			formulario.save()
			return redirect('/lista_productos')
	else:	
		formulario=agregar_producto_form(instance=obj)

	formulario=agregar_producto_form(instance=obj) #me trae el mismo formulario
	return render(request,'agregar_producto.html',locals())


def eliminar_producto_view(request, id_prod):
	obj=Producto.objects.get(id=id_prod)
	obj.delete()
	return redirect('/lista_productos')

def desactivar_producto_view(request, id_prod):
	obj=Producto.objects.get(id=id_prod)
	obj.status=False
	obj.save()
	return redirect('/lista_productos')

def login_view(request):
	usu=''
	cla=''
	if request.method=='POST':
		formulario=login_form(request.POST)
		if formulario.is_valid():
			usu=formulario.cleaned_data['usuario']
			cla=formulario.cleaned_data['clave']
			usuario=authenticate(username=usu,password=cla)
			if usuario is not None and usuario.is_active: #none =nulo , is active retorna un booleano
				login(request,usuario)
				return redirect('/lista_productos')
			else: #si no se pudo loguear
				msj: "usuario o clave incorrectos"
	formulario=login_form()
	return render(request,'login.html',locals())

def logout_view(request):
	logout(request)
	return redirect('/login/')


def register_view(request):
	formulario= register_form()
	if request.method=='POST':
		formulario=register_form(request.POST)
		if formulario.is_valid():
			usuario=formulario.cleaned_data['username']
			correo=formulario.cleaned_data['email']
			password_1=formulario.cleaned_data['password_1']
			password_2=formulario.cleaned_data['password_2']
			u=User.objects.create_user(username=usuario, email=correo, password=password_1)
			u.save()
			return render(request,'thanks_for_register.html',locals())
		else:
			return render(request,'register.html',locals())
	return render(request,'register.html',locals())


def servicio_web_view(request):
	data=serializers.serialize('json',Producto.objects.all())
	return HttpResponse(data,content_type='application/json')
