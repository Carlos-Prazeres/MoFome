from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from MoFome import views
from usuarios import views as usuarios_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
     path('login/',  usuarios_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='MoFome/logout.html'), name='logout'),
    path('register/', usuarios_views.register, name='register'),
    path('', include('MoFome.urls')),
    path('perfil/', usuarios_views.perfil, name='perfil'),
    path('perfil/favoritas/', views.receitas_favoritas , name='receitas-favoritas'),
    path('perfil/editarperfil/', usuarios_views.editarperfil, name='editarperfil'),
    path('perfil/modo_privacidade/', usuarios_views.modo_privacidade, name='perfil-privacidade'),
    path('perfil/apagar/', usuarios_views.delete_user_profile, name='apagar-perfil'),
    path('perfil/<str:username>/', usuarios_views.perfilDeOutroUsuario, name='perfil-outro'),
    path('perfil/<str:username>/receitas', usuarios_views.receitasDeOutroUsuario, name='receitas_outro_usuario'),
    path('login/',  usuarios_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='MoFome/logout.html'), name='logout'),
    

    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
