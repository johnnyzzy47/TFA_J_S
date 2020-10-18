
from django.urls import path
#from django.conf.urls import url, include
from . import views

app_name = 'tracker_app'

urlpatterns =[
             path('',views.main),
             path('sightings/add/',views.add_squirrel),
             path('sightings/stats/',views.get_stats),
             path('sightings/<str:UID>/',views.edit_squirrel),
             path('sightings/',views.sighting),
             path('map/', views.map_squirrel),
             ]
