
from django import forms 
from django.forms  import ModelForm
from .models import Venue, Event


#Create a venue form 
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        # fields = "__all__"       #if you want all of fields of table (model) Venue will  come to in forms
        fields = ("name", 'address', 'zip_code','phone', 'web','email_address')    # the fields of table venue in terms of forms came here
        labels ={
            'name': '',
            'address': '',
            'zip_code':'',
            'phone':'',
            'web':'',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':"venue name"}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':"Address"}),
            'zip_code':forms.TextInput(attrs={'class':'form-control','placeholder':"Zip_code"}),
            'phone':forms.TextInput(attrs={'class':'form-control','placeholder':"Phone No."}),
            'web':forms.TextInput(attrs={'class':'form-control','placeholder':"Web Address"}),
            'email_address':forms.EmailInput(attrs={'class':'form-control','placeholder':"Email Address"}),
        }


#create a event form
class EventForm(ModelForm):
    class Meta:
        model = Event
        # fields = "__all__"       #if you want all of fields of table (model) Venue will  come to in forms
        fields = ("name", 'event_date', 'venue','manager', 'attendees','description')    # the fields of table venue in terms of forms came here
        labels ={
            'name': '',
            'event_date': '',
            'venue':'Venue',
            'manager':'Manager',
            'attendees':'Attendees',
            'description': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':"Event name"}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':"Event date-YYYY-MM-DD HH:MM:SS"}),
            'venue':forms.Select(attrs={'class':'form-select','placeholder':"venue"}),
            'manager':forms.Select(attrs={'class':'form-select','placeholder':"manger"}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control','placeholder':"attendees"}),
            'description':forms.Textarea(attrs={'class':'form-control','placeholder':"description"}),
        }