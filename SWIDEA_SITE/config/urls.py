from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include ('ideas.urls'),name='ideas'),
    path('tools/',include ('tools.urls'),name='tools'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

