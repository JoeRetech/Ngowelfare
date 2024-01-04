from django.contrib import admin
from django.urls import path,include
from ngoapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('',views.index,name='index'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('home/', views.home, name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('event/',views.event,name='event'),
    path('send_email/',views.send_email,name='send_email'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)