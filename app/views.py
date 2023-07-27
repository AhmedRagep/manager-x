from django.shortcuts import render,redirect
from .models import Person
from .resources import PersonResource
from django.contrib import messages
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .filters import ManagerFilter
from django_filters.views import FilterView

# Create your views here.
  
# class DashboardView(FilterView):
#     model = Person
#     # لتحديد عدد المنتجات التي ستظهر في الصفحه
#     # paginate_by = 3
#     ## filter
#     filterset_class = ManagerFilter
#     template_name = 'home.html'
@login_required(login_url='login')
def dashboard(request):
    user = request.user.username
    person = Person.objects.filter(code=user)
    user = request.user.username
    month = request.GET.get('month')
    year = request.GET.get('year')

    if month != '' and month is not None:
        person = Person.objects.filter(code=user, month=month)

    elif year != '' and month is not None:
        person = Person.objects.filter(code=user, year=year)

    
    return render(request,'dashboard.html',{'person':person})


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form =CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Succfully Join!')
            return redirect('login')
    return render(request,'register.html',{'form':form})


def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user =authenticate (request, username=username, password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request, 'Login Succfully Join!')
                return redirect('dashboard')
    return render(request,'login.html',{'form':form})


def my_logout(request):
    auth.logout(request)
    messages.warning(request, 'Logged Out!')
    return redirect('login')