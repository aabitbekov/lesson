from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def admin_redirect(request):
    return redirect('admin:index')