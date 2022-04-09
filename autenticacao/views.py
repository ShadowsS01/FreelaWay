from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/jobs/perfil/')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        confirmar_senha = request.POST.get('confirm-password')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem')
            return redirect('/auth/cadastro')

        if len(username.strip()) == 0 or len(senha.strip()) == 0:
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/auth/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usário com esse username')
            return redirect('/auth/cadastro')

        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
            return redirect('/auth/logar')

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/auth/cadastro')

def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/jobs/perfil/')
        return render(request, 'logar.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/auth/logar')
        else:
            auth.login(request, usuario)
            return redirect('/jobs/perfil/')

def sair(request):
    auth.logout(request)
    return redirect('/auth/logar')

def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response

def handler500(request, *args, **argv):
    response = render(request, '500.html')
    response.status_code = 500
    return response