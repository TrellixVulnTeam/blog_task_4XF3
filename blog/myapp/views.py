from django.shortcuts import redirect, render
from httplib2 import Authentication
from myapp.forms import UserRegiistration,BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
# Create your views here.

# def index(requests):
#     return render(requests,'myapp/index.html')
def index(requests):
    return render(requests, 'myapp/index.html')

def user_register(requests):
    if requests.method=='POST':
        fm=UserRegiistration(requests.POST)
        if fm.is_valid():
            fm.save()
            messages.success(requests,"You are registered.")
            return redirect('login')
    else:
        fm=UserRegiistration()
    return render(requests,'myapp/register.html',{'form':fm})


def user_login(request):
    #if requests.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                user = authenticate(username=uname, password=pw)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfully loggedin!!")
                    return redirect('login')
        else:
            fm = AuthenticationForm()
        return render(request, 'myapp/login.html', {'form': fm})
    # else:
    #     return redirect('register')

def user_profile(request):
    if request.method=='POST':
        fm=BlogForm(request.POST)
        # import ipdb ; ipdb.set_trace()
        if fm.is_valid:
            fm.save()
            messages.success(request,'Your Blog is Posted.')
        else:
            #fm=BlogForm()
            print('Error')
    else:
        fm=BlogForm()
    return render(request,'myapp/profile.html',{'form':fm})