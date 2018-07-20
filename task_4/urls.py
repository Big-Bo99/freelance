
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('market/', include('market.urls')),
    path('admin/', admin.site.urls),
]
