from django.shortcuts import render, redirect
from .forms import FormDataForm
from django.contrib import messages
import requests

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            state = form.cleaned_data['state']
            subject_1 = form.cleaned_data['subject_1']
            subject_2 = form.cleaned_data['subject_2']
            subject_3 = form.cleaned_data['subject_3']
            subject_4 = form.cleaned_data['subject_4']
            subject_5 = form.cleaned_data['subject_5']
            email = form.cleaned_data['email']

            # replace 4500 with the api port number
            api_endpoint = 'http://127.0.0.1:4500/api/signup/'
            api_data = {
                'first_name': first_name,
                'last_name': last_name,
                'state': state,
                'subject_1': subject_1,
                'subject_2': subject_2,
                'subject_3': subject_3,
                'subject_4': subject_4,
                'subject_5': subject_5,
                'email': email,
            }
            response = requests.post(api_endpoint, json=api_data)

            if response.status_code == 201:
                
                return redirect('success_page')  # Redirect to a success page
            else:
                # Handle error
                pass

    else:
        form = FormDataForm()

    return render(request, 'index.html', {'form': form})


def success(request):
    return render(request, 'success.html')