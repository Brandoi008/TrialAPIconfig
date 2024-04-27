from django.http import response
import requests
from django.shortcuts import render

def home(request):
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    data=response.json()
    result=data['setup']
    result1=data['punchline']

    response2=requests.get('https://dog.ceo/api/breeds/image/random')
    data2 =response2.json()
    result2 =data2['message']
    return render(request, 'templates/index.html',{'result':result, 'result1':result1,'result2':result2})
  
