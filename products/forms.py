from .models import Comment
from django import forms
from django.contrib.auth.models import User

class CommentProducts(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.product_id = kwargs.pop('product_id', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.user = self.user
        comment.product_id = self.product_id
        comment.save()
    class Meta:
        model = Comment
        fields = ["Content"]
        widgets = {
            'Content': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }