from django.shortcuts import render,redirect
from.forms import Emailform
import requests
# Create your views here.

def fetch_data_from_api(email):
    # Replace with the actual API endpoint and parameters
    api_endpoint = 'http://127.0.0.1:4500/api/checkresults/'

    params = {'email': email}

    response = requests.get(api_endpoint, params=params)

    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON data
    else:
        return None
    

def index(request):
    if request.method == 'POST':
        form = Emailform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            print(email)

            api_endpoint = 'http://127.0.0.1:4500/api/checkresults/'

            data = {
                'email':email
            }

            response = requests.post(api_endpoint, json=data)

            if response.status_code == 200:
                data= response.json()['data']['student']

                context = {
                    'data':data
                }

                return render(request,'viewer.html',context)  
            elif response.status_code == 400:
                return render(request,'failed.html')
            

    form = Emailform()
    context = {
        'form':form
    }
    return render(request,'checker.html',context)


def results_view(request):
    if request.method == "POST":        
        email = request.POST.get('email') 
        print(email)

    return render(request,'viewer.html')
