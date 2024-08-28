from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

handler404 = "mainapp.views.my_custom_page_not_found_view"
handler500 = "mainapp.views.my_custom_page_server_error"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('posts.urls')),
    path('accounts/', include('users.urls')),
]
