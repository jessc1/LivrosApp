from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Livros

class HomePageView(ListView):
    model = Livros
    template_name = 'livraria.html'
    context_object_name = 'all_livros' 

class LivroDetailView(DetailView):
    model = Livros
    template_name = 'livros_detail.html'

class LivroCreateView(CreateView):
    model = Livros
    template_name = 'novo_livro.html'
    fields = '__all__'

class LivroDeleteView(DeleteView):
    model = Livros
    template_name = 'deletar_livro.html'
    success_url = reverse_lazy('livraria')


class LivroUpdateView(UpdateView):
    model = Livros
    template_name= 'editar_livro.html'
    fields = ['nome', 'autor', 'preco', 'qtd_paginas']