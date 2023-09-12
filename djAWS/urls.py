from django.contrib import admin
from django.urls import path, include

# added
# third party
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.urls'))
]

# add to load media files from model to AWS
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)