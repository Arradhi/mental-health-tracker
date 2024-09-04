from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306240061',
        'name': 'Arradhi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)

# Create your views here.
