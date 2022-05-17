from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def portal_welcome(request):
    """
    If users are authenticated, direct them to the portal welcome page
    (template index.html). Otherwise, take them to the login page.
    """
    return render(request, 'portal/index.html', { 'request' : request })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')