from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     # models와 달리 CharField에서 max_length가 필수 인자가 아니다
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs = {
                'class': 'my-title',
                'placeholder': 'Enter the title',
            }
        )
    )
    # 모델 등록만 하면 끝
    class Meta:
        model = Article
        fields = '__all__'
