from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,TaskForm
from .models import Task
from django.contrib import messages


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Signed up successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Signup failed. Please fix the errors.")
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect('profile')
            else:
                messages.error(request, "Invalid credentials. Try again.")
        else:
                messages.error(request,"Invalid username or password.")
       
    else:
        form = AuthenticationForm()
    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('login')

@login_required
def profile_view(request):

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, "Task added successfully.")
            return redirect('profile')
    else:
        form = TaskForm()
    status_filter = request.GET.get('status')
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    return render(request, 'registration/profile.html', {'form': form, 'tasks': tasks})

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Error updating task. Please try again.")
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'registration/profile.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('profile')
    return render(request, 'registration/profile.html')

@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in dict(Task.STATUS_CHOICES):
            task.status = status
            task.save()
            messages.success(request, "Updated Task successfully.")
        else:
            messages.error(request, "Invalid status selected.")
    return redirect('profile')
