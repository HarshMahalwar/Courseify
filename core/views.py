from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Course, Category, Boiler
from .forms import CourseForm, CategoryForm, BoilerForm
from django.contrib.auth.decorators import login_required


def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username or password is invalid.')
    context = {'page': page}
    return render(request, 'login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    page = 'register'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "The user already exists.")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "The password is incorrect.")
            return redirect('register')
    context = {'page': page}
    return render(request, 'register.html', context)


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    t = Boiler.objects.filter(Q(Course__category__name__icontains=q) |
                              Q(Course__title__icontains=q) |
                              Q(Course__desc__icontains=q)
                              #   Q(participant__name__icontains=q)
                              )
    t1 = Category.objects.all()
    context = {'courses': t, 'category': t1}
    return render(request, 'home.html', context)


@login_required(login_url='login')
def add(request, pk):
    t = Boiler.objects.get(id=pk)
    fr = BoilerForm(instance=t)
    if request.method == 'POST':
        fr = BoilerForm(request.POST, instance=t)
        if fr.is_valid():
            fr.save()
            return redirect('home')
    context = {'courses': t}
    return render(request, 'update_page.html', context)


@login_required(login_url='login')
def add_category(request):
    t1 = CategoryForm()

    if request.method == 'POST':
        fr1 = CategoryForm(request.POST)
        if fr1.is_valid():
            fr1.save()
            return redirect('home')
    context = {'courses': t1}
    return render(request, 'course_form.html', context)


@login_required(login_url='login')
def add_course(request):
    t1 = CourseForm()

    if request.method == 'POST':
        fr1 = CourseForm(request.POST)
        if fr1.is_valid():
            fr1.save()
            return redirect('home')
    context = {'courses': t1}
    return render(request, 'course_form.html', context)


# @login_required(login_url='login')
# def add_participant(request):
#     t1 = participantForm()

#     if request.method == 'POST':
#         fr1 = participantForm(request.POST)
#         if fr1.is_valid():
#             fr1.save()
#             return redirect('home')
#     context = {'courses': t1}
#     return render(request, 'course_form.html', context)


def delete_course(request, pk):
    r = Boiler.objects.get(id=pk)
    if request.user != r.host:
        return render(request, "sneaky.html")
    if request.method == 'POST':
        r.delete()
        return redirect('/')
    context = {'course': r}
    return render(request, 'delete.html', context)


def linkedin(request):
    return redirect('https://www.linkedin.com/in/harsh-mahalwar-4310b316a/')


def github(request):
    return redirect('https://github.com/HarshMahalwar?tab=repositories')


def update_course(request, pk):
    r = Boiler.objects.get(id=pk)
    fr = BoilerForm(instance=r)
    if request.user != r.host:
        return render(request, "sneaky.html")
    if request.method == 'POST':
        fr = BoilerForm(request.POST, instance=r)
        if fr.is_valid():
            fr.save()
            return redirect('/')
    context = {'courses': fr}
    return render(request, 'update_page.html', context)


def about(request):
    return redirect('https://harshmahalwar.github.io/portfolio/')
