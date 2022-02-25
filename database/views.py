from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from greenpeace import settings
from .models import Evaluation
from django.shortcuts import render
from .forms import ViewDataForm
from datetime import datetime
from django.utils.timezone import now
from django.forms.models import model_to_dict
import json
import requests

def format(s):
    #Format a column name properly
    result = ''
    words = s.split('_')
    for i in range(len(words)):
        w = words[i]
        result += (w[0].capitalize() + w[1:])
        if(i < len(words) - 1):
            result += ' '
    return result
@csrf_exempt
def edit(request):
    if request.method == 'POST':
        #url = "https://sheets.googleapis.com/v4/spreadsheets/1BMgBYG41MbJ_FAg8wFv-TMfeRvIxS8kYrUvUS4UwF0I" + "?key=" + settings.GOOGLE_API_KEY
        #r = requests.get(url)
        #print(r.content)
        body = request.body
        json_data = json.loads(body)
        print(json_data)
        keys = [key for key in json_data.keys()]
        recent_entry_key = max(keys)
        r = json_data[str(recent_entry_key)]
        print(r)
        keywords = r[4].split(',')
        date=r[0]
        if date == 'today':
            date = now()
        e = Evaluation(date=date, NRO=r[1], evaluator=r[2], project_type=r[3], keywords=keywords, content=r[5])
        e.save()
        return HttpResponse("Saved Data")

    else:
        return HttpResponse("Invalid Request")

def index(request):

    # https://docs.djangoproject.com/en/3.1/topics/forms/
    all_entries = Evaluation.objects.all()
    print(all_entries)
    data = [{"evaluator": "marvin chun", "nro": "yale", "f":"F"}, {"evaluator": "peter salovey", "nro": "yale", "f":"F"}]
    data = json.dumps(data)
    if request.method == 'POST':
        form = ViewDataForm(request.POST)
        if form.is_valid():

            label = form.cleaned_data['label']
            location = form.cleaned_data['location']
            year = form.cleaned_data['year']
            #For now, the sidebar filter things are not the same as the database objects. Going to grab all()
            entries =Evaluation.objects.all()

    else:
        form = ViewDataForm()
        entries = Evaluation.objects.all()
    data = []
    #Hacky way of getting rid of invisible columns
    restricted_columns = ['id']
    for e in entries:
        entry_dict = {}
        temp = model_to_dict(e, fields=[field.name for field in e._meta.fields])
        for key in temp.keys():
            if not str(key) in restricted_columns:
                name = ''
                if isinstance(temp[key], list):
                    arr = temp[key]
                    length = len(arr)
                    for i in range(length - 1):
                        name += (arr[i] + ', ')
                    name += arr[length - 1]
                else:
                    name = str(temp[key])
                entry_dict[format(str(key))] = name
        data.append(entry_dict)

    data = json.dumps(data)
    return render(request, 'database.html', {'form': form, 'data': data})
