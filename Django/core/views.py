from django.shortcuts import render

#Create View controller function.
def home(request):
    return render(request, 'index.html')