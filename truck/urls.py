
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("home.urls",namespace='home')),
    path('^accounts/', include("accounts.urls", namespace="accounts")),
    path('^accounts/', include("django.contrib.auth.urls")),
    path(r'accounts/login/$', views.IndexView.as_view(), name="index"),
    path('thanks/', views.ThanksPage.as_view(), name="thanks"),
    path('booking/', include("booking.urls", namespace="booking")),
    path('contactus/', include("contactus.urls", namespace="contactus")),
    path('bookings/', include("bookings.urls", namespace="bookings")),

]
