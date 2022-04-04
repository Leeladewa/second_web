from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse
import csv
# Create your views here.

# FUNCTIIN FOR GENERATING A CSV FILE/EXCEL FILE OF LIST OF VENUES WE HAVE
def venue_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venues.csv'

    # Create a csv file
    writer = csv.writer(response)

    #Accessing Venue model for listing all venues in text file
    venues = Venue.objects.all()
    #Add column headings to the csv file
    writer.writerow(["Venue Name", "Address", "Zip Code","Phone", "Web Address" "Email Address"]) 
    
    # for listing the venues in text file we need to go for loop
    for venue in venues:
          
        writer.writerow([venue.name,venue.address,venue.zip_code,venue.phone,venue.web,venue.email_address]) 

   
    return response



# FUNCTIIN FOR GENERATING A TETX FILE OF LIST OF VENUES WE HAVE
def venue_text(request):
    response = HttpResponse(content_type ='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    #Accessing Venue model for listing all venues in text file
    venues = Venue.objects.all()
    lines = [] # an empty list for listing the all venues

    # for listing the venues in text file we need to go for loop
    for venue in venues:
          
        lines.append(f'{venue.name}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web}\n{venue.email_address}\n\n\n\n') 

    # lines = ["This is line 1\n",
    # "This is line 2\n",
    # "This is line 3\n"]

    # Write to Textfile
    response.writelines(lines)
    return response


# FUNCTION FOR SHOWING ALL EVENTS AND VENUES
def list_venues(request):
    venue_list = Venue.objects.all().order_by("name")
    return render(request,'events/venue.html',{"venue_list":venue_list})

def all_events(request):
    event_list = Event.objects.all().order_by("-name")

    return render(request,"events/event_list.html",{"event_list": event_list } )    



# FUNCTIONS FOR ADDING VENUES AND EVENTS
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')

    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html',{'form':form, 'submitted':submitted})

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html',{'form':form, 'submitted':submitted})    


# FUNCTIONS FOR UPDATING VENUES AND EVENTS
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')

    return render(request, 'events/update_event.html', {'event':event, 'form':form})

def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')

    return render(request, 'events/update_venue.html', {'venue':venue, 'form':form})


#FUNCTION FOR DELETING OF VENUES AND EVENTS
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')    



#FUNCTION FOR SEARCHING VENUES
def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains = searched)
        return render(request, 'events/search_venues.html', 
        {'searched':searched,
        'venues':venues})
    else:
        return render(request, 'events/search_venues.html', {})    


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/showVenue.html', {'venue':venue})


# FUNCTION FOR HOME OR FIRST PAGE OF WEBSITE
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):

    name = "Leela Dhar"
    month = month.title()
    # convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    # Create a calender
    cal = HTMLCalendar().formatmonth(year, month_number)
    now = datetime.now()
    # to get current year
    current_year = now.year

    #  to get current time
    time = now.strftime("%I:%M %p")

    return render(request, 'events/home.html',{
        "name": name,
        "year": year,
        "month": month,
        "month_num" : month_number,
        "cal": cal,
        "curr_year": current_year,
        "time": time,
        })




