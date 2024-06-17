from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    # requesting all records from database here
    records = Record.objects.all()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in")
            return redirect('home')
    else:
        # If the user is not posting, show all the records from the databse here
        return render(request, 'home.html', { 'records': records })


def logout_user(request):
    logout(request)
    messages.success(request, "You have beem logged out...")
    return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

    
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "You must be logged in to view this page")
        return redirect('home')

def add_customer_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                print(add_record)
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to perform this action")
        return redirect('home')
        

def delete_customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record_to_del = Record.objects.get(id=pk)
        print(customer_record_to_del)
        customer_record_to_del.delete()
        deletion_text = "Record for {} {} deleted successfully"
        messages.success(request, deletion_text.format(customer_record_to_del.first_name, customer_record_to_del.last_name))
    else:
        messages.success(request, "You must be logged in to perform this action")

    return redirect('home')

def update_customer_record(request, pk):
    if request.user.is_authenticated:
        record_to_update = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=record_to_update)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect('home')
        else:
            return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to perform this action")