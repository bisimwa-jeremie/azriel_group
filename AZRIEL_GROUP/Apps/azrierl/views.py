from django.shortcuts import render

# Create your views here.
def text_tailwind(request):
    return render(request, 'index.html')