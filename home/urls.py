from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "AJ Admin"
admin.site.index_title = "Welcome to AJ Space"
admin.site.site_title = "AJ Admin Panel"

urlpatterns = [
    path('', views.index, name='home'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)