from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, createBlogs,EditProfileForm, commentForm
from django.contrib.auth.models import User
from . import models
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import MakeBlogs, Comments
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'user was created for '+ user)
			
		return redirect('/login/')

	else:
		form = RegistrationForm()
		return render(request, "main/register.html",{'form':form,})


def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username = username, password = password)

		if user is not None:
			login(request, user)
			return redirect('/')
		else:
			messages.info(request, "username or password is incorrect")
			return render(request, "registration/login.html", {})

	else:
		return render(request, "registration/login.html", {})
		
login_required(login_url = 'login')
def logoutUser(request):
	logout(request)
	return redirect('login')



login_required(login_url = 'login')
def CreateBlog_user(request):
	if request.method == 'POST':
		form = createBlogs(request.POST)
		if form.is_valid():
			n = form.cleaned_data.get('title')
			d = form.cleaned_data.get('description')
			r = form.cleaned_data.get('reference')
			t = MakeBlogs(title = n, description = d, reference = r, user = request.user)
			t.save()
			print("data uploaded successfully")
			return redirect('/')
		else:
			form = createBlogs()
			return render(request, "registration/create.html",{'form':form})

	else:
		form = createBlogs(request.POST, request.FILES)
		return render(request, "registration/create.html",{'form':form})




login_required(login_url = 'login')
def editProfile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('/')

	else:
		form = EditProfileForm(instance = request.user)
		return render(request, "main/editprofile.html",{'form':form})



from django.shortcuts import get_object_or_404
login_required(login_url = 'login')
def newuser(request):
	return render(request, "main/myuser.html", {})

login_required(login_url = 'login')
def YourBlogs(request):
	webp_list= MakeBlogs.objects.filter(user = request.user)
	my_dict= {'web_list':webp_list,}
	return render(request, "main/yourblogs.html", context = my_dict)

def get_absolute_url(self):
    return "/people/%i/" % self.id

def like_post(request):
	post = get_object_or_404(MakeBlogs, id = request.POST.get('post_id'))
	post.likes.add(request.user)
	post.dislikes.remove(request.user)
	return redirect("/")

def dislike_post(request):
	post = get_object_or_404(MakeBlogs, id = request.POST.get('post_id'))
	post.dislikes.add(request.user)
	post.likes.remove(request.user)
	return redirect("/")

def save_post(request):
	post = get_object_or_404(MakeBlogs, id = request.POST.get('post_id'))
	post.saveduser.add(request.user)
	return redirect("/")


def saved_post(request):
	list_blog = MakeBlogs.objects.filter(saveduser = request.user).order_by('date')
	return render(request, "main/blogs.html",{'web_list':list_blog, 'saved':"Saved"})

def comment_post(request):
	post = get_object_or_404(MakeBlogs, id = request.POST.get('post_id'))
	webp_list = MakeBlogs.objects.filter(id = request.POST.get('post_id'))
	form = commentForm(request.POST)
	if form.is_valid():
		c = form.cleaned_data['comment']
		t = Comments(comment = c, user = request.user, post = post)
		t.save()
		comments = Comments.objects.filter(post = post).order_by('-id')
		return render( request, "main/comment.html", {'comments':comments, 'web_list': webp_list, 'form':form})

	else:
		form = commentForm()
		comments = Comments.objects.filter(post = post).order_by('-id')
		webp_list = MakeBlogs.objects.filter(id = request.POST.get('post_id'))
		return render( request, "main/comment.html", {'comments':comments, 'web_list': webp_list, 'form':form})


		

	

def liked_post(request):
	#post = get_object_or_404(MakeBlogs, id = )
	list_blog = MakeBlogs.objects.filter(likes = request.user).order_by('date')
	return render(request, "main/blogs.html",{'web_list':list_blog}) 

def delete_post(request):
	post = get_object_or_404(MakeBlogs, id = request.POST.get('delete_id'))
	if request.method == 'POST':
		form = MakeBlogs(request.POST)
		post.delete()
		return redirect('/yourblogs/')

	else:
		return render(request, "main/yourblogs.html")


def AllBlogs(request):
	webp_list= MakeBlogs.objects.all()
	my_dict= {'web_list':webp_list,}
	return render(request, "main/blogs.html", context = my_dict)



