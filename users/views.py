from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.



def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display a blank registation form
        form = UserCreationForm()
    else:
        #Process completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log user in and redirect them to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('a_small_World:index'))

        context = {'form': form}
        return render(request, 'users/register.html', context)


def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('a_small_world:index'))