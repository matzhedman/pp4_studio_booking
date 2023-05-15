from django.shortcuts import render, redirect
from .models import Record

# Create your views here.


def get_booking_list(request):
    records = Record.objects.all()
    context = {
        'records': records
    }
    return render(request, 'booking/booking_list.html', context)


def create_record(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        phone = request.POST.get('item_phone')
        Record.objects.create(name=name, phone=phone)

        return redirect('get_booking_list')
    return render(request, 'booking/create_record.html')
