from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserRegister

# Create your views here.
def sign_up_by_html(request):
    # Псевдо-список users уже существующих пользователей:
    users = ['Alexey', 'Trump', 'Musk', 'JackieChan', 'vanDamme']
    info = {}

    if request.method == 'POST':
        # Получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        '''
        1.'Пароли не совпадают', если не совпали введённые пароли.
        2.'Вы должны быть старше 18', если возраст меньше 18.
        3.'Пользователь уже существует', если username есть в users.
        '''
        error_message = ''
        if password != repeat_password:
            error_message += 'Пароли не совпадают\n'
        try:
            age = int(age)
            if age < 18:
                error_message += 'Вы должны быть старше 18\n'
        except:
            error_message += 'Возраст должен быть целым числом\n'
        if username in users:
            error_message += 'Пользователь уже существует\n'

        # для контроля:
        print('sign_up_by_html(request):')
        print(f'username = "{username}"')
        print(f'password = "{password}"')
        print(f'repeat_password = "{repeat_password}"')
        print(f'age = "{age}"')
        print(info)

        if not error_message:
            users.append(username)
            # Http-ответ пользователю:
            return HttpResponse(f'Приветствуем, {username}!')
        else:
            info['error'] = error_message
            return render(request, 'fifth_task/index.html', context=info)
    # если это GET:
    return render(request, 'fifth_task/registration_page.html')

def sign_up_by_django(request):
    # Псевдо-список users уже существующих пользователей:
    users = ['Alexey', 'Trump', 'Musk', 'JackieChan', 'vanDamme']
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # Обрабатываем данные формы:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            '''
            1.'Пароли не совпадают', если не совпали введённые пароли.
            2.'Вы должны быть старше 18', если возраст меньше 18.
            3.'Пользователь уже существует', если username есть в users.
            '''
            error_message = ''
            if password != repeat_password:
                error_message += 'Пароли не совпадают\n'
            try:
                age = int(age)
                if age < 18:
                    error_message += 'Вы должны быть старше 18\n'
            except:
                error_message += 'Возраст должен быть целым числом\n'
            if username in users:
                error_message += 'Пользователь уже существует\n'

            # для контроля:
            print('sign_up_by_django(request):')
            print(f'username = "{username}"')
            print(f'password = "{password}"')
            print(f'repeat_password = "{repeat_password}"')
            print(f'age = "{age}"')
            print(info)

            if not error_message:
                users.append(username)
                # Http-ответ пользователю:
                return HttpResponse(f'Приветствуем, {username}!')
            else:
                info['error'] = error_message
                return render(request, 'fifth_task/index.html', context=info)
    else:
        # если это GET:
        form = UserRegister()
    return render(request, 'fifth_task/index_django.html', {'form': form})
