from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
# Create your views here.

def register(request):
    form=RegisterForm(request.POST or None)
    #post or none sayesinde get ve post için if-else bloğu açmamıza gerek kalmaz
    #eğer post ve valid ise is_validi geçer ve if'e girer.
    #get ise is_validi geçemez ve if'i atlar ve formun olduğu register sayfasına yönlendirilir.
    #form sayfasında kullanıcı bilgileri alınır ve methodu post'a çevrilip tekrar buraya gelir.
    #bu kez method post olduğundan is_validi geçer ve kullanıcı oluşturulur.
    if form.is_valid(): #is_valid django sayesinde tanımladığımız clean() fonksiyonunu otomaik olarak çalıştırır
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Succesfully registered")
        return redirect("index")
    
    context={
    "form":form
    }

    return render(request,"register.html",context)

def loginUser(request):
    return render(request,"login.html")
def logoutUser(request):
    pass