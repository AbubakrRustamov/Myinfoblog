from django import forms
from django.forms import ModelForm, TextInput, Select, Textarea
from .models import  *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'intro', 'body']

        widgets = {
            'category': Select(attrs={'name': 'category'}),
            'title': TextInput(attrs={'name': 'title'}),
            'intro': TextInput(attrs={'name': 'intro'}),
            'body': Textarea(attrs={'name': 'body'}),
        }    

        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
        

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','messages']  



""" category=forms.CharField(widget=forms.Select(attrs={'name':'category'}))
    title=forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    intro=forms.CharField(widget=forms.TextInput(attrs={'name':'intro'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'name':'body'}))  """            