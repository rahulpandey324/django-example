from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/')


    return render(request,'basic_app/signup.html',{'form': form})
