
from django.contrib import admin
from django.urls import path, include
from core import views as v

urlpatterns = [
    path('', v.index, name="index"),
    path('core/', include('core.urls')),
    path('boss/', admin.site.urls),
]
