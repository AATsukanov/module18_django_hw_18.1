from django.shortcuts import render

# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')

def games(request):
    games = ['Heroes of Might and Magic',
             'The Gothic',
             'The Kreed',
             'World Of Tanks']
    context = {'games': games}
    return render(request, 'fourth_task/games.html', context=context)

def cart(request):
    return render(request, 'fourth_task/cart.html')