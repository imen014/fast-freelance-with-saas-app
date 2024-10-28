from django.shortcuts import render, get_object_or_404, redirect
from account_creation_app.forms import UserCreationForm, AuthenticatorForm
from account_creation_app.models import Freelancer

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


def create_account(request):
    form = UserCreationForm()
    message = ''
    if request.method=="POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = 'account created succefully'
        else:
            message= 'verifier vos données'

    return render(request, 'account_creation_app/account_created.html', {'form':form, 'message':message})

@login_required
def show_account(request, id):
    account_instance = get_object_or_404(Freelancer, id=id)
    return redirect('see_informations', id=account_instance.id)

@login_required
def get_accounts(request):
    accounts = Freelancer.objects.all()
    return render(request, 'account_creation_app/get_accounts.html', {'accounts':accounts})

@login_required
def see_informations(request, id):
    account = get_object_or_404(Freelancer, id=id)
    return render(request, 'account_creation_app/see_informations.html', {'account':account})

@login_required
def modify_profile(request, id):
    account_instance = get_object_or_404(Freelancer, id=id)
    form = UserCreationForm(instance=account_instance)
    message = ''
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES, instance=account_instance)
        if form.is_valid():
            form.save()
            return redirect('get_accounts')
    return render(request, 'account_creation_app/profile_modified.html', {'form':form, 'message':message})


@login_required
def delete_account(request, id):
    account_instance = get_object_or_404(Freelancer, id=id)
    account_instance.delete()
    return redirect('get_accounts')
    

def login_user(request):
    form = AuthenticatorForm()
    message = "there's a problem"
    if request.method == "POST":
        form = AuthenticatorForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            
    return render(request, 'account_creation_app/loggined.html', {'form':form})


@login_required
def home(request):
    return render(request, 'account_creation_app/home.html')

def logout_user(request):
    logout(request)
    return redirect('login_user')