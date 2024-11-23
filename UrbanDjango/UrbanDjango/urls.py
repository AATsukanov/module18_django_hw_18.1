"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# ДОБАВЛЯЕМ НАШИ ФУНКЦИЮ И КЛАСС ИЗ ФАЙЛА:
#from task2.views import index_class, index_function
#from task3.views import platform, games, cart
#from task4.views import platform, games, cart
from task5.views import sign_up_by_html, sign_up_by_django
#from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # пустой '' = значит главная страница:
    #>> ДЗ 18.2
    # для классового:
    # path('', index_class.as_view()),
    # для функционального:
    # path('index/', index_function),
    #>> ДЗ 18.3, 18.4
    # path('', platform),
    # path('platform', platform),
    # path('games', games),
    # path('cart', cart),
    #>> ДЗ 18.5
    path('', sign_up_by_html),
    path('django_sign_up', sign_up_by_django),
]
