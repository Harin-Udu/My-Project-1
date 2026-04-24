from datetime import date, time

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .models import ContactMessage, Booking


def home(request):
    success = False

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and phone and message:
            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                message=message
            )
            success = True

    return render(request, 'salon/index.html', {'success': success})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'salon/signup.html', {'form': form})


@login_required
def booking_page(request):
    success = False
    error = None

    if request.method == 'POST':
        service = request.POST.get('service', '').strip()
        appointment_date = request.POST.get('appointment_date', '').strip()
        appointment_time = request.POST.get('appointment_time', '').strip()
        notes = request.POST.get('notes', '').strip()

        if service and appointment_date and appointment_time:
            selected_date = date.fromisoformat(appointment_date)
            selected_time = time.fromisoformat(appointment_time)

            if selected_date < date.today():
                error = 'You cannot book an appointment for a previous date.'

            elif selected_time < time(10, 0) or selected_time > time(22, 0):
                error = 'Appointments can only be booked between 10:00 AM and 10:00 PM.'

            elif selected_time.minute not in [0, 30, 45]:
                error = 'Please select a valid appointment time.'

            else:
                existing_count = Booking.objects.filter(
                    appointment_date=selected_date,
                    appointment_time=selected_time
                ).count()

                if existing_count >= 3:
                    error = 'This time slot is fully booked. Please select another time.'
                else:
                    Booking.objects.create(
                        user=request.user,
                        service=service,
                        appointment_date=selected_date,
                        appointment_time=selected_time,
                        notes=notes
                    )
                    success = True
        else:
            error = 'Please complete all required fields.'

    return render(request, 'salon/booking.html', {
        'success': success,
        'error': error
    })

def our_team(request):
    return render(request, 'salon/our_team.html')


def about(request):
    return render(request, 'salon/about.html')


def help(request):
    return render(request, 'salon/help.html')
