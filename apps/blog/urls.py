from django.urls import path
from .views import (CategoriaListView, CategoriaDetailView, CategoriaCreateView,  CategoriaUpdateView, 
                    CategoriaDeleteView, ArticuloListView, ArticuloCreateView, ArticuloDeleteView, 
                    ArticuloDetailView, ArticuloUpdateView, CategoriaArticuloListView, CategoriaArticuloCreateView, 
                    CategoriaArticuloDeleteView, CategoriaArticuloDetailView, CategoriaArticuloUpdateView,
                    AutorCreateView, AutorDeleteView, AutorDetailView, AutorListView, AutorUpdateView)

urlpatterns = [
    path('categoria/list', CategoriaListView.as_view(), name='categoria_list'),
    path('categoria/<int:pk>', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categoria/create', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categoria/<int:pk>/update', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categoria/create', CategoriaDeleteView.as_view(), name='categoria_delete'),

    ############
    path('categoria/list', ArticuloListView.as_view(), name='articulo_list'),
    path('categoria/<int:pk>', ArticuloDetailView.as_view(), name='articulo_detail'),
    path('categoria/create', ArticuloCreateView.as_view(), name='articulo_create'),
    path('categoria/<int:pk>/update', ArticuloUpdateView.as_view(), name='articulo_update'),
    path('categoria/create', ArticuloDeleteView.as_view(), name='articulo_delete'),

    #################
    path('categoria/list', CategoriaArticuloListView.as_view(), name='categoriaarticulo_list'),
    path('categoria/<int:pk>', CategoriaArticuloDetailView.as_view(), name='categoriaarticulo_detail'),
    path('categoria/create', CategoriaArticuloCreateView.as_view(), name='categoriaarticulo_create'),
    path('categoria/<int:pk>/update', CategoriaArticuloUpdateView.as_view(), name='categoriaarticulo_update'),
    path('categoria/create', CategoriaArticuloDeleteView.as_view(), name='categoriaarticulo_delete'),

    ####################
    path('categoria/list', AutorListView.as_view(), name='autor_list'),
    path('categoria/<int:pk>', AutorDetailView.as_view(), name='autor_detail'),
    path('categoria/create', AutorCreateView.as_view(), name='autor_create'),
    path('categoria/<int:pk>/update', AutorUpdateView.as_view(), name='autor_update'),
    path('categoria/create', AutorDeleteView.as_view(), name='autor_delete')
]
