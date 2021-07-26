from django import forms
from django.forms import ModelForm
from .models import  Comment, Contact

class PostForm(forms.Form):
    category=forms.CharField(widget=forms.Select(attrs={'name':'category'}))
    title=forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    intro=forms.CharField(widget=forms.TextInput(attrs={'name':'intro'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'name':'body'}))

class PostUpdateForm(forms.Form):
    category=forms.CharField(widget=forms.Select(attrs={'name':'category'}))
    title=forms.CharField(widget=forms.TextInput(attrs={'name':'title'}))
    intro=forms.CharField(widget=forms.TextInput(attrs={'name':'intro'}))
    body=forms.CharField(widget=forms.Textarea(attrs={'name':'body'}))    

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email','messages']        