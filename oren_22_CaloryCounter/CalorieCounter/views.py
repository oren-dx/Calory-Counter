from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,Count
from datetime import date
from django.contrib import messages
from CalorieCounter.models import *
from CalorieCounter.forms import *


def register(request):
    form_data = RegisterForm
    if request.method == 'POST':
        form_data = RegisterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, 'User Created Successfully')
            return redirect('login_page') 
    
    messages.warning(request, 'User Already Exists')
    form_data = RegisterForm()
    context = {
        'form_data':form_data,
        'title':'register page',
        'form_title':'User Register Page ',
        'form_btn':'Register'
    }
    return render(request, 'base-form.html',context)

def login_page(request):
    form_data = LoginForm
    if request.method == 'POST':
        form_data = LoginForm(request, request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request, user)
            messages.success(request, 'Login successfully')
            return redirect('dashboard')
        
    messages.warning(request, 'Invaild Credentials')
    form_data = LoginForm()
    context = {
        'form_data':form_data,
        'title':'Login page',
        'form_title':'User Login Page',
        'form_btn':'Login'
    }
    return render(request, 'base-form.html',context)

@login_required
def logout_page(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login_page')


@login_required
def dashboard(request):
    try:
        current_user = request.user
        bmr = round(request.user.user_info.bmr, 2)
    except:
        bmr = 0
        
    today = date.today()    
    today_consumed_data = ConsumedCalories.objects.filter(
        consumed_by = current_user,
        created_at = today
        )
    total_consumed_calories = today_consumed_data.aggregate(
         total_calorie = Sum('calorie'),
         total_count = Count ('calorie')) 
    

    context = {
        'required_calories':bmr,
        'today_consumed_data':today_consumed_data,
        'consumed_calories':total_consumed_calories['total_calorie'],
        'total_count':total_consumed_calories['total_count'],
    }
    return render(request, 'dashboard.html',context)

@login_required
def profile_page(request):
    
    return render(request, 'profile.html')

@login_required
def update_profile(request):
    try:
        current_user = request.user.user.info
    except:
        current_user = None
        
    if request.method == 'POST':
        form_data = ProfileUpdateForm(request.POST, instance = current_user)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = request.user
            weight = data.weight
            height = data.height
            age = data.age
            if data.gender == 'Male':
                # BMR= 66.47+(13.75 x weight in kg) + (5.003 x height in cm) - (6.755 x age in years) 
                bmr_calculate = 66.47 + (13.75 * weight) + (5.003 * height) - (6.755 * age)
            else:
                # BMR=655.1+(9.563 x weight in kg)+(1.850 xheight in cm) - (4.676 x age in years)
                bmr_calculate = 655.1 + (9.563 * weight) + (1.850 * height) - (4.676 * age)
            data.bmr = bmr_calculate
            data.save()
            messages.success(request, 'Profile Update Successfully')
            return redirect('profile_page')
                
            
    form_data = ProfileUpdateForm(instance = current_user)
    
    context = {
        'form_data':form_data,
        'form_title':'Update Profile Info',
        'form_btn':'Update'
    }
    return render(request, 'base-form.html',context)

@login_required
def consumed_calories_list(request):
    consumed_data = ConsumedCalories.objects.filter(consumed_by = request.user)
    
    context = {
        'consumed_data':consumed_data
    }
    return render(request, 'calorie_list.html',context)

@login_required
def add_calorie(request):

    if request.method == 'POST':
        form_data = ConsumedCalorieForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.consumed_by = request.user
            data.save()
            messages.success(request,'Calorie information added successfully')
            return redirect('consumed_calories_list')

    else:
        form_data = ConsumedCalorieForm()
    context = {
        'form_data':form_data,
        'form_title':'Add Calorie Info',
        'form_btn':'Add Calorie'
    }
    return render(request, 'base-form.html', context)

@login_required
def update_calorie(request, id):
    try:
        data = ConsumedCalories.objects.get(id = id)
    except:
        data = None

    if request.method == 'POST':
        form_data = ConsumedCalorieForm(request.POST , instance = data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.consumed_by = request.user
            data.save()
            messages.success(request,'Calorie information added successfully')
            return redirect('consumed_calories_list')

    else:
        form_data = ConsumedCalorieForm(instance = data)
    context = {
        'form_data':form_data,
        'form_title':'Update Calorie Info',
        'form_btn':'Update Calorie'
    }
    return render(request, 'base-form.html', context)

@login_required
def delete_calorie(request, id):
    try:
        data = ConsumedCalories.objects.get(id = id)
    except:
        data = None
    data.delete()
    messages.success(request,'Calorie Delete successfully')
    return redirect('consumed_calories_list')