from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CUserChangeForm, CUserCreationForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signin')
    else:
        form = CUserCreationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/form.html',context)

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:profile', request.user.username)
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/form.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('accounts:signin')

@login_required
def update(request):
    if request.method == 'POST':
        form = CUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', request.user.username)
    else:
        form = CUserChangeForm(instance=request.user)
    context = {
        'form':form,
    }
    return render(request,'accounts/form.html',context)

@require_POST
@login_required
def delete(request):
    request.user.delete()
    return redirect('accounts:signin')

def profile(request,username):
    User = get_user_model()
    user = get_object_or_404(User,username=username)
    context = {
        'user':user,
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, username):
    User = get_user_model()
    user = get_object_or_404(User, username=username)
    if user != request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)
    return redirect('accounts:profile', user.username)