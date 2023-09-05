from django.urls import path
from .views import (
    ReceitaListView,
    ReceitaDetailView,
    ReceitaCreateView,
    ReceitaUpdateView,
    ReceitaDeleteView,
    TopicoListView,
    TopicoDetailView,
    TopicoCreateView,
    TopicoUpdateView,
    TopicoDeleteView,
    ComentarioCreateView,
    ComentarioTopicoCreateView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('receitas/', ReceitaListView.as_view() , name='receitas'),
    path('receitas/pesquisa/', views.ReceitaFilterView , name='filtro-de-receitas'),
    path('receitas/<int:pk>/', ReceitaDetailView.as_view() , name='receitas-detail'),
    path('receitas/<int:pk>/favoritar/', views.favoritar_receita , name='receitas-favoritar'),
    path('receitas/<int:pk>/avaliar/', views.avaliar_receita, name='avaliar_receita'),
    path('receitas/new/', ReceitaCreateView.as_view() , name='receitas-create'),
    path('receitas/<int:pk>/editar/', ReceitaUpdateView.as_view() , name='receitas-update'),
    path('receitas/<int:pk>/apagar/', ReceitaDeleteView.as_view() , name='receitas-delete'),
    path('receitas/<int:pk>/comentarios/', ComentarioCreateView.as_view() , name='receita-comentario'),
    path('perfil/suasreceitas/', views.minhas_receitas , name='minhasreceitas'),
    path('topicos/new/', TopicoCreateView.as_view() , name='topicos-create'),
    path('topicos/', TopicoListView.as_view() , name='topicos'),
    path('topicos/<int:pk>/', TopicoDetailView.as_view() , name='topicos-detail'),
    path('topicos/<int:pk>/editar/', TopicoUpdateView.as_view() , name='topicos-update'),
    path('topicos/<int:pk>/apagar/', TopicoDeleteView.as_view() , name='topicos-delete'),
    path('perfil/seustopicos/', views.meus_topicos , name='meustopicos'),
    path('topicos/<int:pk>/comentarios/', ComentarioTopicoCreateView.as_view() , name='topico-comentario'),

]   


