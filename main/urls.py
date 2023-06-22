from django.urls import path

from main.views import *

urlpatterns = [

    path('', index, name="index"),
    path('about-us/', about, name="about"),
    path('our-clients/', clients, name="clients"),
    path('our-services/', services, name="services"),
    path('our-services/events/', events, name="events"),
    path('our-services/media-production-and-training/', media, name="media"),
    path('our-services/cvc-and-general-printing/', printing, name="printing"),
    path('our-services/travels-and-logistics/', travels, name="travels"),
    path('our-projects/', ProjectsView.as_view(), name="projects"),
    path('contact-us/', contact, name="contact"),
    path('masterclass/', masterclass, name="masterclass"),

]