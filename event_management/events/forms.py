from django import forms
from .models import Event, Client, Guest, Employee, Caterer, Venue

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'type', 'theme', 'date', 'time', 'duration', 'venue', 'caterer', 'client', 'guests']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter event description'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter event location'}),
            'type': forms.Select(attrs={'placeholder': 'Select event type'}),
            'theme': forms.TextInput(attrs={'placeholder': 'Enter event theme'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD'}),
            'time': forms.TimeInput(attrs={'placeholder': 'HH:MM:SS'}),
            'duration': forms.TimeInput(attrs={'placeholder': 'HH:MM:SS'}),
            'venue': forms.Select(attrs={'placeholder': 'Select event venue'}),
            'caterer': forms.Select(attrs={'placeholder': 'Select event caterer'}),
            'client': forms.Select(attrs={'placeholder': 'Select event client'}),
            'guests': forms.CheckboxSelectMultiple(),  # Use CheckboxSelectMultiple for ManyToManyField
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['guests'].queryset = Guest.objects.all()

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'contact_details', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter client name'}),
            'address': forms.TextInput(attrs={'placeholder': 'Enter client address'}),
            'contact_details': forms.TextInput(attrs={'placeholder': 'Enter contact details'}),
            'budget': forms.NumberInput(attrs={'placeholder': 'Enter budget'}),
        }

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['name', 'address', 'contact_details']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter guest name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter guest address'}),
            'contact_details': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact details'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'department', 'job_title', 'basic_salary', 'age', 'date_of_birth', 'passport_details', 'manager']

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'address', 'contact', 'min_guests', 'max_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'min_guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_guests': forms.NumberInput(attrs={'class': 'form-control'})
        }

class CatererForm(forms.ModelForm):
    class Meta:
        model = Caterer
        fields = ['name', 'address', 'contact_details', 'menu', 'min_guests', 'max_guests']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_details': forms.TextInput(attrs={'class': 'form-control'}),
            'menu': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'min_guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_guests': forms.NumberInput(attrs={'class': 'form-control'})
        }
