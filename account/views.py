from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def waiting_for_auth(request):
    if request.user.checkForTI:
        return redirect("/")
    return render(request, 'waiting_for_auth.html')