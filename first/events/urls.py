from django.urls import path
from . import views

urlpatterns = [


    #path Converter
    #int : numbers 
    #str : strings
    #path : whole urls
    #slug : hyphen- and _ underscores
    #UUID : Unniversally unique identifier
    
    path('', views.home, name='home'),       # url for base or first page of website
    path("<int:year>/<str:month>/",views.home, name="home"),   # calender page for website
    
    # url path for adding events and venue
    path("add_event", views.add_event, name="add-event"),
    path("add_venue", views.add_venue, name="add-venue"),

    # url for listing and showing venues
    path("events", views.all_events, name="list-events"),
    path("list_venues", views.list_venues, name='list-venues'),
    path("show_venue/<venue_id>", views.show_venue, name="show-venue"),

    # url for searching venues
    path("search_venues", views.search_venues, name="search-venues"),

    # url path for updating informaton about venues and events
    path("update_event/<event_id>", views.update_event, name="update-event"),
    path("update_venue/<venue_id>", views.update_venue, name="update-venue"),


    # url path for deleting an venues and event
    path("delete_event/<event_id>", views.delete_event, name="delete-event"),
    path("delete_venue/<venue_id>", views.delete_venue, name="delete-venue"),


    #url path for generating text file of any venues 
    path("venue_text", views.venue_text, name="venue-text"), 
    path("venue_csv", views.venue_csv, name="venue-csv"), 

]