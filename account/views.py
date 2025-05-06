from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required 
from account.decorators import check_authoritation


@login_required
@check_authoritation
def waiting_for_auth(request):
    if request.user.checkForTI:
        return redirect("/")
    return render(request, 'waiting_for_auth.html')