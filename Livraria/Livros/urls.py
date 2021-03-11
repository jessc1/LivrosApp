from django.urls import path
from .views import ( 
    HomePageView,
    LivroDetailView,
    LivroCreateView,
    LivroUpdateView, 
    LivroDeleteView
)

urlpatterns = [
    path('livros/<int:pk>/deletar/',LivroDeleteView.as_view(), name='deletar_livro'),
    path('livros/<int:pk>/editar/', LivroUpdateView.as_view(), name='editar_livro'),
    path('livros/novo/', LivroCreateView.as_view(), name='novo_livro'),
    path('livros/<int:pk>/', LivroDetailView.as_view(), name='livros_detail'),
    path('', HomePageView.as_view(), name='livraria'),
    
]

