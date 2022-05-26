from django.shortcuts import render, HttpResponseRedirect

def main_page(request):
    return render(request, 'index.html')