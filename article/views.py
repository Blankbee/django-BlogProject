from django.shortcuts import render,redirect
from .forms import ArticleForm
from django.contrib import messages
from .models import Article

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)
def addArticle(request):#Aynı formu oluştururken olduğu gibi appin modeli olduğundan kolayca ona kaydeder.
    form=ArticleForm(request.POST or None)
    if form.is_valid():
        article=form.save(commit=False)#commit=False ile formu hazırlar ancak göndermez.commit=False işlemini 
        article.author=request.user#author bilgisini formda vermediğimiz ve burada vermemiz gerektiği için yaptık..
        article.save()
        messages.success(request,"Article successfully created.")
        return redirect("index")


    return render(request,"addarticle.html",{"form":form})