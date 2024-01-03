from django.contrib import admin
from django.urls import path, include
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# For media files.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('user_accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('employee/', include('EmployeeApp.urls')),
    path('admin/', admin.site.urls),
]

# urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

