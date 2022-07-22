from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'banner1': 'img\menu1.jpg',
        'soto1' : 'img/soto1.jpeg',
        'soto2' : 'img/soto2.jpeg',
        'soto3' : 'img/soto3.jpeg',
        'soto4' : 'img/soto4.jpeg',
        'nav1': [
            ['/', 'Home'],
            ['/menu', 'Menu']
        ]
    }
    return render(request, 'menu.html', context)