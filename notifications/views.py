from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render (request, 'notifications/lobby.html')