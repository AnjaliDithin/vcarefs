from django .urls import path,include,re_path
from web import views
from .views import index,home,about,contact,services,team
urlpatterns =[
    path('',views.index.as_view(),name='index'),
    path('home/',views.home.as_view(),name='home'),
    path('about/',views.about.as_view(),name='about'),
    path('contact/',views.contact.as_view(),name='contact'),
    path('services/',views.services.as_view(),name='services'),
    path('team/',views.team.as_view(),name='team'),
    #error
   
]