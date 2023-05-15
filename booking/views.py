from django.shortcuts import render, redirect, get_object_or_404
from .models import Record
from .forms import RecordForm


# Create your views here.


def get_booking_list(request):
    records = Record.objects.all()
    context = {
        'records': records
    }
    return render(request, 'booking/booking_list.html', context)


def create_record(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')
    form = RecordForm()
    context = {
        'form': form
    }

    return render(request, 'booking/create_record.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Record, id=item_id)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_booking_list')
    form = RecordForm(instance=item)
    context = {
        'form': form
    }

    return render(request, 'booking/booking_list.html', context)
