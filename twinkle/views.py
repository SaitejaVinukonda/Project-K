from django.shortcuts import render

# Create your views here.
def galaxy(request):
    return render(request, 'galaxy/galaxy.html')
