from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('database/', include('database.urls')),
    path('sign-in/', include('sign-in.urls')),
    path('sidebar/', include('sidebar.urls')),
    path('modal/', include('modal.urls'))
]
