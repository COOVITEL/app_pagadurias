from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def waiting_for_auth(request):
    return render(request, 'waiting_for_auth.html')