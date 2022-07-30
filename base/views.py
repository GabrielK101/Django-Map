from django.shortcuts import render
from django.http import HttpResponse
import folium
import requests


# Create your views here.

def map(request):
    response = requests.get('http://127.0.0.1:8000/api/')

    users = response.json()

    m = folium.Map(location=[0,0], zoom_start=2)

    for user in users:
        name = user['name']
        lat = user['lat']
        lng = user['lng']

        folium.Marker([lat, lng], tooltip=name, popup=f"Latitude:{lat}, Longitude:{lng}").add_to(m)

    m = m._repr_html_()

    context = {'m': m, 'users': users}

    return render(request, 'base/default.html', context)
