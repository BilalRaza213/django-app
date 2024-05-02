from django.shortcuts import render, get_object_or_404, redirect
from .forms import EventForm, ClientForm , GuestForm, EmployeeForm, VenueForm, CatererForm
from django.http import JsonResponse
from .models import Employee, Event, Client, Guest, Venue, Caterer

# Add views for adding, deleting, and modifying details as needed


def home(request):
    return render(request, 'event/home.html')
# Event work

def events_list(request):
    events = Event.objects.all()
    # print(events)
    return render(request, 'event/event_list.html', {'events': events})

def create_event(request):
    caterers = Caterer.objects.all()  # Fetch the list of caterers from the database

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events_list')  # Redirect to the events list page after saving
    else:
        form = EventForm()
        
    return render(request, 'event/create_event.html', {'form': form, 'caterers': caterers})

def edit_event(request, event_id):
    caterers = Caterer.objects.all()
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('/events')  # Redirect to the events list page after saving
    else:
        form = EventForm(instance=event)
    return render(request, 'event/edit_event.html', {'form': form, 'caterers': caterers})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('/events') 
    else:
        return redirect('/events') 

# //////////////////////////////////////////////////////////// # 

# Client views
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'event/client_list.html', {'clients': clients})

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to the client list page after saving
    else:
        form = ClientForm()
    return render(request, 'event/create_client.html', {'form': form})

def edit_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'event/edit_client.html', {'form': form})

def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('/clients')
    else:
        return redirect('/clients')
    


# //////////////////////////////////////////////////////////// # 

def guests_list(request):
    guests = Guest.objects.all()
    return render(request, 'event/guests_list.html', {'guests': guests})

def create_guest(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guests_list')
    else:
        form = GuestForm()
    return render(request, 'event/create_guest.html', {'form': form})

def edit_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    if request.method == 'POST':
        form = GuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
            return redirect('guests_list')
    else:
        form = GuestForm(instance=guest)
    return render(request, 'event/edit_guest.html', {'form': form})

def delete_guest(request, guest_id):
    guest = get_object_or_404(Guest, pk=guest_id)
    if request.method == 'POST':
        guest.delete()
        return redirect('/guests')
    else:
        return redirect('/guests')
    
# //////////////////////////////////////////////////////////// #  
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'event/employee_list.html', {'employees': employees})

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'event/create_employee.html', {'form': form})

def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'event/edit_employee.html', {'form': form})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    if request.method == 'POST':
        employee.delete()
    return redirect('employee_list')  

# //////////////////////////////////////////////////////////// # 


def venue_list(request):
    venues = Venue.objects.all()
    return render(request, 'event/venue_list.html', {'venues': venues})

def create_venue(request):
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueForm()
    return render(request, 'event/create_venue.html', {'form': form})

def edit_venue(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    if request.method == 'POST':
        form = VenueForm(request.POST, instance=venue)
        if form.is_valid():
            form.save()
            return redirect('venue_list')
    else:
        form = VenueForm(instance=venue)
    return render(request, 'event/edit_venue.html', {'form': form})

def delete_venue(request, venue_id):
    venue = get_object_or_404(Venue, pk=venue_id)
    if request.method == 'POST':
        venue.delete()
        return redirect('venue_list')
    else:
        return redirect('venue_list')
    
# //////////////////////////////////////////////////////////// # 


# index
def caterer_list(request):
    caterers = Caterer.objects.all()
    return render(request, 'event/caterer_list.html', {'caterers': caterers})

# create
def create_caterer(request):
    if request.method == 'POST':
        form = CatererForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('caterer_list')
    else:
        form = CatererForm()
    return render(request, 'event/create_caterer.html', {'form': form})

# edit
def edit_caterer(request, caterer_id):
    caterer = get_object_or_404(Caterer, pk=caterer_id)
    if request.method == 'POST':
        form = CatererForm(request.POST, instance=caterer)
        if form.is_valid():
            form.save()
            return redirect('caterer_list')
    else:
        form = CatererForm(instance=caterer)
    return render(request, 'event/edit_caterer.html', {'form': form})

# delete
def delete_caterer(request, caterer_id):
    caterer = get_object_or_404(Caterer, pk=caterer_id)
    if request.method == 'POST':
        caterer.delete()
        return redirect('caterer_list')
    else:
        return redirect('caterer_list')

