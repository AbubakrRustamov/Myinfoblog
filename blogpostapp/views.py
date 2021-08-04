from django.core import paginator
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import title
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import PostForm, CommentForm, ContactForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
# Create your views here.

def search(request):
    context = {}
    post = Post.objects.all()
    if request.method == 'GET':
        query = request.GET.get('search')
        queryset = post.filter(Q(title__icontains=query))
        total = queryset.count()
        context.update({
            'total': total,
            'query': query,
            'posts': queryset,
        })

        return render(request, 'blogpostapp/search.html', context)

def home(request):
    category=Category.objects.all()
    post=Post.objects.all().order_by('-id') 

    
    page = request.GET.get("page")
    paginator = Paginator(post, 3)

    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)        

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

            return redirect('detail', slug=slug)
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
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('detail', slug=slug )
    else:
        form = PostForm(instance=post)    

    context = {
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



    