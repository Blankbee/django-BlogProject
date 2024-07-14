from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

def articles(request):
    keyword=request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()

    return render(request,"articles.html",{"articles":articles})

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addArticle(request):#Aynı formu oluştururken olduğu gibi appin modeli olduğundan kolayca ona kaydeder.
    form=ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)#commit=False ile formu hazırlar ancak göndermez.commit=False işlemini 
        article.author=request.user#author bilgisini formda vermediğimiz ve burada vermemiz gerektiği için yaptık..
        article.save()
        messages.success(request,"Article successfully created.")
        return redirect("article:dashboard")


    return render(request,"addarticle.html",{"form":form})

def detail(request,id):
    #article=Article.objects.filter(id=id).first()
    article=get_object_or_404(Article,id=id)

    comments=article.comments.all()
    return render(request,"detail.html",{"article":article,"comments":comments})
    
@login_required
def updateArticle(request,id):
    article=get_object_or_404(Article, id=id)
    if article.author != request.user:
        messages.warning(request,"You cannot update an article that is not yours. Nice try bro ;)")
        return redirect("index")
    else:
        form=ArticleForm(request.POST or None,request.FILES or None,instance=article)
        if form.is_valid():
            article=form.save(commit=False)#commit=False ile formu hazırlar ancak göndermez.commit=False işlemini 
            article.author=request.user#author bilgisini formda vermediğimiz ve burada vermemiz gerektiği için yaptık..
            article.save()
            messages.success(request,"Article successfully editted.")
            return redirect("article:dashboard")

        return render(request,"update.html",{"form":form})
@login_required
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    if article.author != request.user:
        messages.warning(request,"You cannot delete an article that is not yours. Nice try bro ;)")
        return redirect("index")
    else:
        article.delete()
        messages.success(request,"Article successfully deleted.")
        return redirect("article:dashboard")


def addComment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))