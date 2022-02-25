from django.http import HttpResponse
from django.shortcuts import render

from .forms import SignInForm

def index(request):

    # https://docs.djangoproject.com/en/3.1/topics/forms/

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            return render(request, 'index.html', {'form': form})

    else:
        form = SignInForm()
    return render(request, 'index.html', {'form': form})
