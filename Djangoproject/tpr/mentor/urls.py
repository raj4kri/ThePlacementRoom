
from django.contrib import admin
from django.urls import path
from django.conf import  settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('mentor', views.mentor_img, name = 'mentor'),
    path('success', views.success, name = 'success'),
    path('mentor_images', views.display_images, name = 'mentor_images'),
    

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)