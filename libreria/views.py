from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

def inicio(request):
  return render(request, 'paginas/inicio.html')

def nosotros(request):
  return render(request, 'paginas/nosotros.html')

def libros(request):
  # * obtener info de la base de datos
  libros = Libro.objects.all()
  return render(request, 'libros/index.html', {'libros': libros})

def crear(request):
  formulario = LibroForm(request.POST or None, request.FILES or None)
  if formulario.is_valid():
    formulario.save() # ? guarda la informacion obtenida del formulario
    return redirect('libros') # ? redirecciona a la pagina '/libros'
  return render(request, 'libros/crear.html', {'formulario': formulario})

def editar(request, id):
  libro = Libro.objects.get(id=id)
  formulario = LibroForm(request.POST or None, request.FILES or None, instance=libro)
  if formulario.is_valid() and request.POST:
    if 'imagen' in request.POST:
      if libro.imagen:
        libro.imagen.storage.delete(libro.imagen.name)
    formulario.save()
    return redirect('libros')
  return render(request, 'libros/editar.html', {'formulario': formulario})

def eliminar(request, id):
  libro = Libro.objects.get(id=id)
  libro.delete()
  return redirect('libros')