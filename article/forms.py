from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):#Burada zaten appimizin bir db modeli olduğu için ordakini aldık ve tekrardan     
    class Meta:                    #form oluşturmaya gerek kalmadı.
        model=Article
        fields=["title","content","article_image"]
