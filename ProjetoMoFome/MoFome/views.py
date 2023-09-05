from typing import Optional
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Receita, Topico, Comentario, ComentarioTopico
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q, F, Count
import re

def home(request):
    return render(request, 'MoFome/home.html')


def receitas(request):
    context = {
        'receitas': Receita.objects.all()
    }
    return render(request, 'MoFome/receitas.html', context)

def minhas_receitas(request):
    receitas_do_usuario = Receita.objects.filter(autor=request.user).order_by('-data_do_post')    
    return render(request, 'MoFome/minhas_receitas.html', {'receitas': receitas_do_usuario})

@login_required
def avaliar_receita(request, pk):
    
    receita = get_object_or_404(Receita, pk=pk)
    avaliacao_atual = receita.avaliacao
    
    quantidade_de_avaliacoes = receita.quantidade_de_avaliacoes + 1

    rating = request.POST.get('avaliacao')

    request.user.profile.receitas_avaliadas.add(receita)
    

    avaliacao_atualizada = int(avaliacao_atual) + int(rating)
    receita.avaliacao = avaliacao_atualizada
    receita.quantidade_de_avaliacoes = quantidade_de_avaliacoes

    receita.media = int(avaliacao_atualizada) / int(quantidade_de_avaliacoes)


    receita.save()

    return redirect('receitas-detail', pk=pk)

@login_required
def favoritar_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)

    if receita in request.user.profile.receitas_favoritas.all():
        request.user.profile.receitas_favoritas.remove(receita)
    else:
        request.user.profile.receitas_favoritas.add(receita)

    return redirect('receitas-detail', pk=pk)



@login_required
def receitas_favoritas(request):
    user_profile = request.user.profile
    receitas_favoritas = user_profile.receitas_favoritas.all()

    return render(request, 'MoFome/receitas_favoritas.html', {'receitas_favoritas': receitas_favoritas})

class ReceitaListView(ListView):
    model = Receita
    template_name = 'MoFome/receitas.html'
    
    def get(self, request):
        ordenacao = request.GET.get('ordenacao', 'data') 
        receitas = Receita.objects.annotate(num_avaliacoes=Count('quantidade_de_avaliacoes'))

        if ordenacao == 'data':
            receitas = receitas.order_by('-data_do_post')
        elif ordenacao == 'avaliacoes':
            receitas = receitas.order_by('-quantidade_de_avaliacoes')

        context = {'receitas': receitas}
        return render(request, self.template_name, context)


    
def ReceitaFilterView(request):
    
    query = request.GET.get('palavra pesquisada')
    if query:
        receitas = Receita.objects.filter(
            Q(title__icontains=query) |  
            Q(ingredientes__icontains=query) | 
            Q(descricao__icontains=query) 
        ).distinct() 
    else:
        receitas = Receita.objects.all()
    
    return render(request, 'MoFome/receitas_filtro.html', {'receitas': receitas, 'query': query})
    


class ReceitaDetailView(DetailView):
    model = Receita

    template_name = 'MoFome/receita_detail.html'  

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        receita = self.object

        comentarios = Comentario.objects.filter(receita=receita)
        context['comentarios'] = comentarios
 
        return context
   

class ReceitaCreateView(LoginRequiredMixin, CreateView):
    model = Receita

    def get(self, request, *args, **kwargs):
        return render(request, 'MoFome/receita_create.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('titulo')
        descricao1 = request.POST.get('descricao')
        imagem = request.FILES.get('receita_imagem')
        horas = request.POST.get('horas')
        minutos = request.POST.get('minutos')
        custo = request.POST.get('custo')
        dificuldade = request.POST.get('dificuldade')
        pessoas = request.POST.get('pessoas')

        lista_ingredientes = request.POST.get('ingredientes')
        lista_modo_de_preparo = request.POST.get('modo_de_preparo')

     
    
    
        autor = request.user

     
        nova_receita = Receita.objects.create(
            title=title,
            descricao=descricao1,
            horas=horas,
            minutos=minutos,
            custo=custo,
            dificuldade=dificuldade,
            autor=autor,
            avaliacao = 0,
            quantidade_de_avaliacoes = 0,
            media = 0,
            ingredientes = lista_ingredientes,
            modo_de_preparo = lista_modo_de_preparo,
            pessoas = pessoas,
        )

       


      
        if imagem:
            nova_receita.imagem = imagem
        
        nova_receita.save()

        return redirect('receitas')
    


class ReceitaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, View):
    model = Receita

    template_name = 'MoFome/receita_update.html'  
    
    
    def get(self, request, pk):
        receita = Receita.objects.get(pk=pk)
        context = {'receita': receita}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        receita = Receita.objects.get(pk=pk)
        
        receita.title = request.POST.get('titulo')
        receita.descricao = request.POST.get('descricao')
        imagem = request.FILES.get('receita_imagem')
        receita.horas = request.POST.get('horas')
        receita.minutos = request.POST.get('minutos')
        receita.custo = request.POST.get('custo')
        receita.dificuldade = request.POST.get('dificuldade')
        receita.pessoas = request.POST.get('pessoas')

        receita.ingredientes = request.POST.get('ingredientes')
        receita.modo_de_preparo = request.POST.get('modo de preparo')

        if imagem:
            receita.imagem = imagem


        receita.save()

        return redirect('minhasreceitas')

    def test_func(self):
        receita = self.get_object()
        if self.request.user == receita.autor:
            return True
        return False 

class ReceitaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Receita
    success_url = reverse_lazy('minhasreceitas')

    def test_func(self):
        receita = self.get_object()
        if self.request.user == receita.autor:
            return True
        return False 


class ComentarioCreateView(CreateView):
    template_name = 'MoFome/receita_detail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, pk, *args, **kwargs):
        comentario1 = request.POST.get('comentario')
        receita1 = Receita.objects.get(pk=pk)

        autor = request.user

        novo_comentario = Comentario(
            receita=receita1,
            comentario=comentario1,
            autor = autor,
        )
        novo_comentario.save()

        return redirect('receitas-detail', pk=pk)

class ComentarioTopicoCreateView(CreateView):
    template_name = 'MoFome/topico_detail.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, pk, *args, **kwargs):
        comentario1 = request.POST.get('comentario')
        topico1 = Topico.objects.get(pk=pk)

        autor = request.user

        novo_comentario = ComentarioTopico(
            topico = topico1,
            comentario = comentario1,
            autor = autor,
        )
        novo_comentario.save()

        return redirect('topicos-detail', pk=pk)

def topicos(request):
    context = {
        'topicos': Topico.objects.all()
    }
    return render(request, 'MoFome/topicos.html', context)

def meus_topicos(request):
    topicos_do_usuario = Topico.objects.filter(autor=request.user)    
    ordering = ['-data_do_post']
    return render(request, 'MoFome/meus_topicos.html', {'topicos': topicos_do_usuario})


class TopicoListView(ListView):
    model = Topico
    template_name = 'MoFome/topicos.html'
    context_object_name = 'topicos'
    ordering = ['-data_do_post']

class TopicoDetailView(DetailView):
    model = Topico

    template_name = 'MoFome/topico_detail.html'  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topico = self.object
        comentarios = ComentarioTopico.objects.filter(topico=topico)
        context['comentarios_topicos'] = comentarios
        return context

class TopicoCreateView(LoginRequiredMixin, CreateView):
    model = Topico

    def get(self, request, *args, **kwargs):
        return render(request, 'MoFome/topico_create.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('titulo')
        discussao1 = request.POST.get('discussao')

        autor = request.user

        novo_topico = Topico(
            title = title,
            discussão = discussao1,
            autor = autor
        )
        
        novo_topico.save()

        return redirect('topicos')
    


class TopicoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, View):
    model = Topico

    template_name = 'MoFome/topico_update.html'  
    
    
    def get(self, request, pk):
        topico = Topico.objects.get(pk=pk)
        context = {'topico': topico}
        return render(request, self.template_name, context)

    def post(self, request, pk):
        topico = Topico.objects.get(pk=pk)
        
        topico.title = request.POST.get('titulo')
        topico.discussão = request.POST.get('discussao')
        
        
        topico.save()

        return redirect('meustopicos')

    def test_func(self):
        topico = self.get_object()
        if self.request.user == topico.autor:
            return True
        return False 

class TopicoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Topico
    success_url = reverse_lazy('meustopicos')

    def test_func(self):
        receita = self.get_object()
        if self.request.user == receita.autor:
            return True
        return False 

