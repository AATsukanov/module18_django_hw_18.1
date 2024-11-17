from django.shortcuts import render
# для шаблонов в виде классов:
from django.views.generic import TemplateView

# Create your views here.
# в виде класса:
class index_class(TemplateView):
    template_name = 'second_task/index_class.html'

# в виде функции:
def index_function(request):
    return render(request, 'second_task/index_function.html')

