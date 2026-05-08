from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView



from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Retrieve the user without authenticating
            user = User.objects.get(username=username)
            # Log in the user regardless of the password
            login(request, user)

            # Redirect based on user role
            if user.is_staff:
                return redirect('admin:index')  # Redirect to the admin dashboard
            else:
                return redirect('accounts:profile')  # Redirect regular user to the profile page
        except User.DoesNotExist:
            # Handle case where user does not exist
            return render(request, 'accounts/login.html', {'error': 'User not found.'})

    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('landing_page')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


   
@login_required
def profile_view(request):
    if request.user.is_driver():
        # Driver-specific content
        context = {
            'assigned_bus': 'Bus details or task info here',
            'driver': True,
        }
    else:
        # Customer content
        context = {
            'customer': True,
        }
    
    return render(request, 'accounts/profile.html', context)





@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'accounts/profile_edit.html', {'form': form})
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Prevents logout after password change
            messages.success(request, 'Your password has been updated!')
            return redirect('accounts:profile')  # Or wherever you want to redirect
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'accounts/change_password.html', {'form': form})





'''class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')  
    '''