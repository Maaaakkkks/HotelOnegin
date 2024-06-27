from django.urls import path

from booking import views

app_name = 'booking'

urlpatterns = [
    # path('/<int:Rooms_descript_id>/', views.booking, name='room'),
    path('1/', views.booking1, name='booking1'),
    path('2/', views.booking2, name='booking2'),
    path('3/', views.booking3, name='booking3'),
    path('4/', views.booking4, name='booking4'),
    path('5/', views.booking5, name='booking5'),
    path('6/', views.booking6, name='booking6'),
]