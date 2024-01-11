from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .forms import ReviewForm
from .models import Review, Zaved,rating, MenuPhotos,Auth
from django.contrib.auth.decorators import login_required
from .models import Zaved

def search_restaurants(request):
    query = request.GET.get('query', '')
    results = Zaved.objects.filter(name__icontains=query).values('id', 'name')
    return JsonResponse(list(results), safe=False)

def menu(request, menu_id):
    menus = get_object_or_404(Zaved, id=menu_id)
    zaved = Zaved.objects.all()
    menu = MenuPhotos.objects.all()
    context = {'menu': menus, 'zaved': zaved}

    return render(request, 'menu.html', context)

def main(request):
    retings = rating.objects.all()
    reviews = Review.objects.all()
    zaved = Zaved.objects.all()
    auth = Auth.objects.all()

    if request.method == 'POST' and request.POST.get('action') == 'login':
        login_email = request.POST.get('login_email')
        login_password = request.POST.get('login_password')

        try:
            user = Auth.objects.get(login=login_email)
            request.session['user_id'] = user.id

        except Auth.DoesNotExist:
            # Пользователь не найден
            return HttpResponse("Пользователь не найден")

        # Обработка регистрации
    elif request.method == 'POST' and request.POST.get('action') == 'register':

        reg_email = request.POST.get('reg_email')
        reg_password = request.POST.get('reg_password')

        # Создаем нового пользователя
        new_user = Auth(login=reg_email, password=reg_password)
        new_user.save()
        return HttpResponse("Регистрация прошла успешно")

        # Обработка формы отзывов
    elif request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')

    else:
        form = ReviewForm()




    return render(request, 'main.html', {'form': form, 'reviews': reviews, 'zaved': zaved, 'retings':retings})


def Reting(request,restoran_id):
    reting = get_object_or_404(Zaved, id=restoran_id)
    zaved= Zaved.objects.all()
    retings = rating()
    context = {'resoran_id':restoran_id, 'zaved':zaved}



    if request.method == 'POST':
        # Обработка данных, отправленных из формы
        preferences = request.POST.get('preferences')
        content = request.POST.get('content')
        autor = request.POST.get('autor')
        is_good = request.POST.get('is_good')
        print(preferences)
        retings.author = autor
        retings.bis = preferences
        retings.is_good = is_good
        retings.content = content
        retings.zaved = reting
        retings.save()


        return HttpResponseRedirect(f'/booking/{restoran_id}')

    return render(request, 'reting.html', context)


def Booking(request, booking_id):



    booking = get_object_or_404(Zaved, id=booking_id)
    zaved = Zaved.objects.all()
    context = {'booking': booking, 'zaved':zaved}


    return render(request, 'Booking.html', context)


def galery_view(request, zaved_id):
    galery = get_object_or_404(Zaved, id=zaved_id)
    zaved = Zaved.objects.all()
    context = {'galery': galery, 'zaved': zaved}

    return render(request, 'galery.html', context)

def account_info(request, zaved_id):
    account_info = get_object_or_404(Zaved, id=zaved_id)
    zaved = Zaved.objects.all()
    context = {'account_info': account_info, 'zaved': zaved}

    return render(request, 'account.html', context)