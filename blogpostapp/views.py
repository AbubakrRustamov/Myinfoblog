from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import PostForm, PostUpdateForm, CommentForm, ContactForm
# Create your views here.



def home(request):
    category=Category.objects.all()
    post=Post.objects.all().order_by('-id') 
  
    return render(request, 'blogpostapp/home.html', {'category': category, 'posts':post})
@login_required
def create_post(request):
    category=Category.objects.all()
    form=PostForm()
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            obj=Post.objects.create(
                category=Category.objects.get(pk=int(form.cleaned_data.get('category'))),
                title=form.cleaned_data.get('title'),
                intro=form.cleaned_data.get('intro'),
                body=form.cleaned_data.get('body'),
                author=request.user
            )
            obj.save()
        else:
            print("Error: ", form.errors)
    return render(request, 'blogpostapp/create_post.html', {'category': category,'form':form})

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)


        if form.is_valid():
            form.save(commit=False)
            form.instance.post = post
            form.save()

            return redirect('detail', slug=post.slug)
    else:
        form = CommentForm()    
    context = {
        'post':post,
        'form':form,
        
    }
    return render(request,'blogpostapp/detail.html', context)

def post_edit(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail')
    else:
        form = PostUpdateForm(instance=post)    

    context = {
        'post':post,
        'form':form,
    }
    return render(request, 'blogpostapp/post_edit.html', context)


def post_delete(request,slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post':post
    }
    return render(request, 'blogpostapp/post_delete.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)


    context = {
        'category' : category
    }
    return render(request,'blogpostapp/category.html', context)



def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
        
    context = {'form':form}
    return render(request, 'blogpostapp/home.html', context)

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

    return render(request, 'blogpostapp/login.html')


def registration(request):

    if request.method == 'POST':
        name =request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']



        if password1 != password2:
            messages.info(request, 'Passwords are not suitable!')
        elif User.objects.filter(username=name).exists():
            messages.info(request,'This username has already been token!')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'This email has already been registered!')
        # elif len(password1) >= 8:
        #     messages.info(request,'This password is less than 8 characters!')
        else:
            user = User.objects.create_user(username=name, email=email, password=password1)
            user.save()
            print('user created')

        return redirect('login')

    return render(request, 'blogpostapp/registration.html')


def logout(request):
    auth.logout(request)
    return redirect('home')



    