from django.shortcuts import render

from .forms import ViewDataForm

def index(request):

    # https://docs.djangoproject.com/en/3.1/topics/forms/

    if request.method == 'POST':
        form = ViewDataForm(request.POST)
        if form.is_valid():

            label = form.cleaned_data['label']
            location = form.cleaned_data['location']
            year = form.cleaned_data['year']

            return render(request, 'sidebar.html', {'form': form})

    else:
        form = ViewDataForm()
    return render(request, 'sidebar.html', {'form': form})
