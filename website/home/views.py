from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request, 'home/home.html', {})

def DemoView(request):
    return render(request, 'home/demo.html', {})
