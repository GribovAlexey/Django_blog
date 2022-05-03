from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from src import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include("blog.urls")),
                  path('members/', include('django.contrib.auth.urls')),
                  path('members/', include('members.urls')),
              ] + static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
