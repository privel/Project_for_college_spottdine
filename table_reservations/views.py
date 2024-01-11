from django.shortcuts import render, redirect, get_object_or_404
from main_site.models import Zaved,bookingTable,rating, MenuPhotos

from django.http import HttpResponseRedirect



def my_page(request,  booking_id):
    booking = get_object_or_404(Zaved, id=booking_id)
    zaved = Zaved.objects.all()
    book = bookingTable.objects.all()
    retings = rating.objects.all()
    b = bookingTable()
    filter = request.GET.get('filter', None)
    if filter == 'positive':
        retings = rating.objects.filter(is_good=True, zaved_id=booking_id)  # Use booking_id here
    elif filter == 'negative':
        retings = rating.objects.filter(is_good=False, zaved_id=booking_id)  # And here
    else:
        retings = rating.objects.filter(zaved_id=booking_id)




    context = {'booking': booking, 'zaved':zaved, 'book':book,'retings':retings}

    if request.method == 'POST':
        # Обработка данных, отправленных из формы
        booking_time = request.POST.get('booking_time')
        booking_guests = request.POST.get('booking_guests')
        prod = request.POST.get('prod')
        date = request.POST.get('date')

        b.zaved = booking
        b.date_t = date
        b.time_t = booking_time
        b.count_g = booking_guests
        b.disc = prod

        b.save()

        return HttpResponseRedirect(f'/booking/{booking_id}')


    return render(request, 'my_page.html',context)

