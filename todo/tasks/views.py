from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

from django.core.mail import send_mail
# Create your views here.

def index(request):
	tasks = Task.objects.all()

	form = TaskForm()

	if request.method =='POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')


	context = {'tasks':tasks, 'form':form}
	return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}

	return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/')

	context = {'item':item}
	return render(request, 'tasks/delete.html', context)


def signup(request):
    if request.method == 'POST':
        # Get form values
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        dob=request.POST.get('dob')
        user = Signup(username=username, password=password,email=email,dob=dob)
        mydict={'username':username}
        user.save()

    #  send_mail(
    #          'Congratulations Mail',
    #         'Your are successfully checkin',
    #         'chiragsaxena001@gmail.com',
    #         ['chiragsaxena001@gmail.com'],
    #         fail_silently=False,
    #     )   
    
        return redirect('login')
    else:
        return render(request, 'tasks/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        email=request.POST['email']
        password = request.POST['password']
       
       
        try:
            d1 = Signup.objects.get(username=username, password=password,)
        except Signup.DoesNotExist:
            return render(request, 'tasks/login.html')
        else:
            request.session['uid'] = d1.id
        
        return redirect("tasks/list")
    else:
        return render(request, 'tasks/login.html')     

def profile(request):
    users=Signup.objects.all()
    return render(request, 'profile.html', {'users':users})                   

