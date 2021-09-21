from django.shortcuts import render

def show_my_page(request):
    return render(request, 'base.html')
