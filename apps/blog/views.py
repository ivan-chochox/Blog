from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Categoria, Articulo, CategoriaArticulo, Autor

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'blog/categorias/categoria_list.html'
    context_object_name = 'categorias'


class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'blog/categorias/categoria_detail.html'
    context_object_name = 'categoria'


class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'blog/categorias/categoria_form.html'
    context_object_name = 'categoria'
    fields = '__all__'
    success_url = reverse_lazy('categoria_list')


class CategoriaUpdateView(CreateView):
    model = Categoria
    template_name = 'blog/categorias/categoria_form.html'
    context_object_name = 'categoria'
    fields = '__all__'
    success_url = reverse_lazy('categoria_list')


class CategoriaDeleteView(CreateView):
    model = Categoria
    template_name = 'blog/categorias/categoria_confirm_delete.html'
    context_object_name = 'categoria'
    fields = '__all__'
    success_url = reverse_lazy('categoria_list')

#############################

class ArticuloListView(ListView):
    model = CategoriaArticulo
    template_name = 'blog/articulos/articulo_list.html'
    context_object_name = 'articulos'


class ArticuloDetailView(DetailView):
    model = CategoriaArticulo
    template_name = 'blog/articulos/articulo_detail.html'
    context_object_name = 'articulo'


class ArticuloCreateView(CreateView):
    model = CategoriaArticulo
    template_name = 'blog/articulos/articulo_form.html'
    context_object_name = 'articulo'
    fields = '__all__'
    success_url = reverse_lazy('articulo_list')


class ArticuloUpdateView(CreateView):
    model = CategoriaArticulo
    template_name = 'blog/articulos/articulo_form.html'
    context_object_name = 'articulo'
    fields = '__all__'
    success_url = reverse_lazy('articulo_list')


class ArticuloDeleteView(CreateView):
    model = CategoriaArticulo
    template_name = 'blog/articulos/articulo_confirm_delete.html'
    context_object_name = 'articulo'
    fields = '__all__'
    success_url = reverse_lazy('articulo_list')



#################################
class CategoriaArticuloListView(ListView):
    model = CategoriaArticulo
    template_name = 'blog/categoriaarticulos/categoriaarticulo_list.html'
    context_object_name = 'categoriasarticulos'


class CategoriaArticuloDetailView(DetailView):
    model = CategoriaArticulo
    template_name = 'blog/categoriaarticulos/categoriaarticulo_detail.html'
    context_object_name = 'categoriaarticulo'


class CategoriaArticuloCreateView(CreateView):
    model = CategoriaArticulo
    template_name = 'blog/categoriaarticulos/categoriaarticulo_form.html'
    context_object_name = 'categoriaarticulo'
    fields = '__all__'
    success_url = reverse_lazy('categoriaarticulo_list')


class CategoriaArticuloUpdateView(CreateView):
    model = CategoriaArticulo
    template_name = 'blog/categoriaarticulos/categoriaarticulo_form.html'
    context_object_name = 'categoriaarticulo'
    fields = '__all__'
    success_url = reverse_lazy('categoriaarticulo_list')


class CategoriaArticuloDeleteView(CreateView):
    model = CategoriaArticulo
    template_name = 'blog/categoriaarticulos/categoriaarticulo_confirm_delete.html'
    context_object_name = 'categoriaarticulo'
    fields = '__all__'
    success_url = reverse_lazy('categoriaarticulo_list')

#################################

class AutorListView(ListView):
    model = Autor
    template_name = 'blog/autor/autor_list.html'
    context_object_name = 'categorias'


class AutorDetailView(DetailView):
    model = Autor
    template_name = 'blog/autor/autor_detail.html'
    context_object_name = 'autor'


class AutorCreateView(CreateView):
    model = Autor
    template_name = 'blog/autor/autor_form.html'
    context_object_name = 'autor'
    fields = '__all__'
    success_url = reverse_lazy('autor_list')


class AutorUpdateView(CreateView):
    model = Autor
    template_name = 'blog/autor/autor_form.html'
    context_object_name = 'autor'
    fields = '__all__'
    success_url = reverse_lazy('autor_list')


class AutorDeleteView(CreateView):
    model = Autor
    template_name = 'blog/autor/autor_confirm_delete.html'
    context_object_name = 'autor'
    fields = '__all__'
    success_url = reverse_lazy('autor_list')