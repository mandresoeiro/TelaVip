from django.contrib.auth.forms import UserCreationForm, AuthenticationForm #TODO formulario QUE DJANFO DISPONIBILIZA PARA USUARIOS
from django.contrib.auth import authenticate, login, logout #TODO authenticate = verifica se o usuario existe(função djan)
from django.shortcuts import render, redirect



def register_view(request):
    if request.method == "POST":  # POST = usuario fazendo uma requisição (clicou no button de cadastrar)
        user_form = UserCreationForm(request.POST)  #TODO dos dados do formulario do usuario esta digitando
        if user_form.is_valid():  # is.valid = verifica se o formulario são valido
            user_form.save()
            return redirect("login") #redirect = redireciona para outra pagina
    else:
        user_form = UserCreationForm()
    return render(request, "register.html", {"user_form": user_form})


def login_view(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("cine_list")
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()
    return render(request, "login.html", {"login_form": login_form})


def logout_view(request):
    logout(request)
    return redirect("cine_list")


