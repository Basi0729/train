from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import  *
from django.contrib.auth import  login, logout,authenticate
from .models import Profile
from django.contrib.auth.models import User

def register_view(request):
    formset=NewProfile(request.POST, request.FILES)
    form =form= NewUserForm(request.POST or None)
    if request.method =='POST':
        if all([form.is_valid(), formset.is_valid()]):
            formset.cleaned_data
            usr_obj = form.save()
            t=Profile(name=formset.cleaned_data['name'],
            id2=usr_obj.id,age=formset.cleaned_data['age'],
            occupation=formset.cleaned_data['occupation'],
            place=formset.cleaned_data['place'],
            joining_date=formset.cleaned_data['joining_date'],
            email_id=formset.cleaned_data['email_id'],
            profile_Main_Img=formset.cleaned_data['profile_Main_Img'])
            t.save()
            return redirect('/')
            
    else:
        formset= NewProfile()
        form=UserCreationForm()
    context={
        'form': form,
        'id':id,
        'formset': formset,

    }    
    return render(request,'register.html',context)



def delete(request, id):
    obj= Profile.objects.get(id=id)
    ob=User.objects.get(id=obj.id2)

    obj.delete()
    ob.delete()
    return redirect('/')

def edit(request,id):
  obj= Profile.objects.get(id=id)

  form=NewProfile(request.POST or None ,instance=obj)
  if form.is_valid():
         
         form.save()
         
         return redirect('/')
  
        
  return render(request,'edit.html',{'form': form,})

def display(request, id):
    obj= Profile.objects.get(id=id)
    ob=User.objects.get(id=obj.id2)
    print(ob)
    context={ "obj": obj,
              "ob":ob}
    return render(request,'display.html',context)

def login_view(request):
    if request.method=="POST":
       username = request.POST.get("username")
       password =request.POST.get("password")
       user = authenticate(request,username=username,
       password=password)
       if user is None:
           context={"error":"Invalid Username or Password"}
           return render(request, "login.html",
           context)
       login(request,user)
       return redirect('/')
    return render(request, "login.html")
    

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "logout.html",{})