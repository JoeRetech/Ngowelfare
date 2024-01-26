from django.contrib import admin
from django.urls import path,include
from ngoapp import views
from django.contrib.auth import views as auth_views
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
    path('joinevent/<int:id>',views.joinevent,name='joinevent'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name="password_reset_complete"),

   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



