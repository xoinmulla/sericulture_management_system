from django.shortcuts import render
from .models import Farmer
# In views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Sericulture Management!")

def add_farmer(request):
    return render(request, 'farmer_form.html')

def market_trends(request):
    return render(request, 'market_trends.html') 

def home(request):
    return render(request, 'home.html') 

def contact(request):
    return render(request, 'contact.html')

def add_farmer(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        # Save the farmer data into the database
        Farmer.objects.create(name=name, contact=contact)
        return render(request, 'success.html')  # Correctly render success page
    return render(request, 'farmer_form.html')  # Render form page

from django.shortcuts import render, get_object_or_404, redirect
from .models import MulberryFarm
from .forms import MulberryFarmForm

def list_mulberry_farm(request):
    farms = MulberryFarm.objects.all()
    return render(request, 'mulberry_farm/list_mulberry_farm.html', {'farms': farms})

def create_mulberry_farm(request):
    if request.method == 'POST':
        form = MulberryFarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_mulberry_farm')
    else:
        form = MulberryFarmForm()
    return render(request, 'mulberry_farm/create_mulberry_farm.html', {'form': form})

def edit_mulberry_farm(request, pk):
    farm = get_object_or_404(MulberryFarm, pk=pk)
    if request.method == 'POST':
        form = MulberryFarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect('list_mulberry_farm')
    else:
        form = MulberryFarmForm(instance=farm)
    return render(request, 'mulberry_farm/edit_mulberry_farm.html', {'form': form})

def delete_mulberry_farm(request, pk):
    farm = get_object_or_404(MulberryFarm, pk=pk)
    farm.delete()
    return redirect('list_mulberry_farm')


from django.shortcuts import render
from .models import SilkwormBatch

def list_silkworm_batches(request):
    batches = SilkwormBatch.objects.all()
    return render(request, 'silkworm_farm/list_silkworm_batches.html', {'batches': batches})

from django.shortcuts import render, redirect
from .forms import SilkwormBatchForm

def create_silkworm_batch(request):
    if request.method == 'POST':
        form = SilkwormBatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_silkworm_batches')
    else:
        form = SilkwormBatchForm()
    return render(request, 'silkworm_farm/create_silkworm_batch.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import SilkwormBatch
from .forms import SilkwormBatchForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import SilkwormBatch
from .forms import SilkwormBatchForm

def edit_silkworm_batch(request, pk):
    batch = get_object_or_404(SilkwormBatch, pk=pk)
    if request.method == 'POST':
        form = SilkwormBatchForm(request.POST, instance=batch)
        if form.is_valid():
            form.save()
            return redirect('list_silkworm_batches')  # This will redirect to the batch list page
    else:
        form = SilkwormBatchForm(instance=batch)
    return render(request, 'silkworm_farm/edit_silkworm_batch.html', {'form': form})



from django.shortcuts import get_object_or_404, redirect
from .models import SilkwormBatch

def delete_silkworm_batch(request, pk):
    batch = get_object_or_404(SilkwormBatch, pk=pk)
    batch.delete()
    return redirect('list_silkworm_batches')  # Change to your actual list view

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages

# Register view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home or dashboard
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')

# Forgot password view
class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'
