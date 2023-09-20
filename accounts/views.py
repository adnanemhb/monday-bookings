from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:
        return redirect('/admin')
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "accounts/login.html", {'error': 'invalid username or password'})
        login(request, user)
        # Will be replaced by a redirection link for bookings
        return redirect('/admin')
    return render(request, "accounts/login.html", {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
    return render(request, "accounts/logout.html", {})
