from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Aluno
from datetime import datetime
from django.contrib import messages


def homepage_view(request):
    return render(request, 'homepage.html')


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {
            'login_incorreto': False
        })
    elif request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(username=email, password=senha)
        if user is not None and not Aluno.objects.filter(user=user).exists():
            login(request, user)
            return redirect('/portal-do-aluno')
        else:
            return render(request, 'login.html', {
                'login_incorreto': True
            })
        
def cadastrar_view(request):
    if request.method == 'GET':
        return render(request, 'cadastrar.html')
    elif request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        data_nascimento = request.POST['data_nascimento']  # Recupera a data de nascimento do formulário
        if User.objects.filter(username=email).exists():
            return render(request, 'cadastro_existente.html')
        # Se não existir, continua com o processo de cadastro normal
        user = User.objects.create_user(email, email, senha, first_name=name)
        user.data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')  # Define a data de nascimento no usuário
        user.save()
        login(request, user)
        return redirect('/portal-do-aluno')
    else:
        return HttpResponseBadRequest()       

def sobre_view(request):
    return render(request, 'sobre.html')

def linguagens_view(request):
    return render(request, 'linguagens.html')

def cursos_view(request):
    return render(request, 'cursos.html')

def portal_do_aluno_view(request):
    return render(request, 'portal-do-aluno.html')

def aula_view(request):
    return render(request, 'aula.html')  
  
  
def nossos_cursos_view(request):
    return render(request, 'nossos-cursos.html') 

def menu_view(request):
    return render(request, 'menu.html')

def get_unidade_content(request, unidade_id):
    # vou usar dados estáticos
    if unidade_id == '1':
        unidade_content = {
            'titulo': 'Título da Unidade 1',
            'texto': 'Este é o texto da Unidade 1',
            'imagem_url': 'static/img/aula/1.jpg'
        }
    elif unidade_id == '2':
        unidade_content = {
            'titulo': 'Título da Unidade 2',
            'texto': 'Este é o texto da Unidade 2',
            'imagem_url': 'static/img/aula/2.jpg'
        }
        
    elif unidade_id == '3':
        unidade_content = {
            'titulo': 'Título da Unidade 3',
            'texto': 'Este é o texto da Unidade 3',
            'imagem_url': 'static/img/aula/3.jpg'
        }
        
    elif unidade_id == '4':
        unidade_content = {
            'titulo': 'Título da Unidade 4',
            'texto': 'Este é o texto da Unidade 4',
            'imagem_url': 'static/img/aula/4.jpg'
        }
        
    elif unidade_id == '5':
        unidade_content = {
            'titulo': 'Título da Unidade 5',
            'texto': 'Este é o texto da Unidade 5',
            'imagem_url': 'static/img/aula/5.jpg'
        }
        
    elif unidade_id == '6':
        unidade_content = {
            'titulo': 'Título da Unidade 6',
            'texto': 'Este é o texto da Unidade 6',
            'imagem_url': 'static/img/aula/6.jpg'
        }
        
    elif unidade_id == '7':
        unidade_content = {
            'titulo': 'Título da Unidade 7',
            'texto': 'Este é o texto da Unidade 7',
            'imagem_url': 'static/img/aula/7.jpg'
        }
        
    elif unidade_id == '8':
        unidade_content = {
            'titulo': 'Título da Unidade 8',
            'texto': 'Este é o texto da Unidade 8',
            'imagem_url': 'static/img/aula/8.jpg'
        }
        
    elif unidade_id == '9':
        unidade_content = {
            'titulo': 'Título da Unidade 9',
            'texto': 'Este é o texto da Unidade 9',
            'imagem_url': 'static/img/aula/9.jpg'
        }
        
    elif unidade_id == '10':
        unidade_content = {
            'titulo': 'Título da Unidade 10',
            'texto': 'Este é o texto da Unidade 10',
            'imagem_url': 'caminho/para/imagem-da-unidade-2.jpg'
        }
        
    elif unidade_id == '11':
        unidade_content = {
            'titulo': 'Título da Unidade 11',
            'texto': 'Este é o texto da Unidade 11',
            'imagem_url': 'caminho/para/imagem-da-unidade-2.jpg'
        }
        
    elif unidade_id == '12':
        unidade_content = {
            'titulo': 'Título da Unidade 12',
            'texto': 'Este é o texto da Unidade 12',
            'imagem_url': 'caminho/para/imagem-da-unidade-2.jpg'
        }
        
    elif unidade_id == '13':
        unidade_content = {
            'titulo': 'Título da Unidade 13',
            'texto': 'Este é o texto da Unidade 13',
            'imagem_url': 'caminho/para/imagem-da-unidade-2.jpg'
        }
        
    elif unidade_id == '14':
        unidade_content = {
            'titulo': 'Título da Unidade 14',
            'texto': 'Este é o texto da Unidade 14',
            'imagem_url': 'caminho/para/imagem-da-unidade-2.jpg'
        }
        
    elif unidade_id == '15':
        unidade_content = {
            'titulo': 'Título da Unidade 15',
            'texto': 'Este é o texto da Unidade 15',
            'imagem_url': 'caminho/para/imagem-da-unidade-2.jpg'
        }
    # Adicione mais condições conforme necessário para outras unidades

    return JsonResponse(unidade_content)