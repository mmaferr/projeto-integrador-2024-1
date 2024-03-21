from django.contrib import admin
from django.urls import path
from lovelace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='home'),
    path('login', views.login_view, name='login'),
    path('cadastrar', views.cadastrar_view, name='cadastrar'),
    path('sobre', views.sobre_view, name='sobre'),
    path('linguagens', views.linguagens_view, name='linguagens'),
    path('portal-do-aluno', views.portal_do_aluno_view, name='portal-do-aluno'),   
    path('nossos-cursos', views.nossos_cursos_view, name='nossos-cursos'), 
    path('aula', views.aula_view, name='aula'),
    path('menu', views.menu_view, name='menu'),
    path('get_unidade_content/<str:unidade_id>/', views.get_unidade_content, name='get_unidade_content'),
]