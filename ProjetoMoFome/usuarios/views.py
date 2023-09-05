from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from MoFome import models as MoFomeModels

def register(request):
    errors = []

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        nome_de_usuario = request.POST.get('nome_de_usuario')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password1 = request.POST.get('password2')


      
        if User.objects.filter(username=nome_de_usuario).exists():
            errors.append('Esse nome de usuário já está registrado.')
            return render(request, 'MoFome/cadastro.html', {'errors': errors})


        if User.objects.filter(email=email).exists():
            errors.append('Um usuário já está registrado com esse email.')
            return render(request, 'MoFome/cadastro.html', {'errors': errors})
        
        if password != password1:
            errors.append('As senhas não são iguais.')
            return render(request, 'MoFome/cadastro.html', {'errors': errors})

        if not errors:
            user = User.objects.create_user(username=nome_de_usuario, email=email, password=password, first_name=nome, last_name=sobrenome)
            return redirect('login')

    
      
    return render(request, 'MoFome/cadastro.html')

@login_required
def delete_user_profile(request):
    usuario = request.user
    try:
        user = User.objects.get(username=usuario.username)
        profile = Profile.objects.get(user=user)
        
         
        profile.delete()
        user.delete()
        return redirect('home')
    except User.DoesNotExist:
        return redirect('home') 
    except Profile.DoesNotExist:
        return redirect('home')
    
    

@login_required
def perfil(request):
    return render(request, 'MoFome/perfil.html')

@login_required
def editarperfil(request):
    errors = []

    user = request.user  

    if request.method == 'POST':
        nome_de_usuario = request.POST.get('nome_de_usuario')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        sobrenome = request.POST.get('sobrenome')
        imagem = request.FILES.get('profile_image')

        if nome_de_usuario != user.username and User.objects.filter(username=nome_de_usuario).exists():
            errors.append('Esse nome de usuário já está registrado.')
        else:
            if nome_de_usuario:
                user.username = nome_de_usuario
            if nome:
                user.first_name = nome
            if email:
                user.last_name = sobrenome
            if sobrenome:
                user.email = email
        
                
        
            perfil, created = Profile.objects.get_or_create(user=user)

            if imagem:
                perfil.image = imagem
                perfil.save()

            user.save()
           
            return redirect('perfil') 
        
    return render(request, 'MoFome/editarperfil.html', {'errors': errors})
    
def login_view(request):
    errors = []

    if request.method == 'POST':
        nome_de_usuario = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=nome_de_usuario, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            errors.append('Credenciais incorretas.')

   
    return render(request, 'MoFome/login.html', {'errors': errors})

def perfilDeOutroUsuario(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    
    usuario = request.user

    if usuario == profile.user:
        return render(request, 'MoFome/perfil.html')
    elif profile.modo_privacidade == 1:
        return render(request, 'MoFome/perfil_bloqueado.html')
    else:
        return render(request, 'MoFome/perfil_outro_usuario.html', {'perfil_do_usuario': profile})

def receitasDeOutroUsuario(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    receitas = MoFomeModels.Receita.objects.filter(autor=user)


    usuario = request.user

    if usuario == profile.user:
        return render(request, 'MoFome/perfil.html')
    elif profile.modo_privacidade == 1:
        return render(request, 'MoFome/perfil_bloqueado.html')
    else:
        return render(request, 'MoFome/receitas_outro_usuario.html', {'receitas': receitas, 'perfil_outro_usuario': profile})

    


@login_required
def modo_privacidade(request):
    if request.method == 'POST':
            modo = request.POST.get('modo_privacidade')
            user = request.user
            perfil = Profile.objects.get(user=user)
            
            if modo == '1':
                perfil.modo_privacidade = 1
                perfil.save()
            else:
                perfil.modo_privacidade = 0
                perfil.save()

            return redirect('perfil')

  