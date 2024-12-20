from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    # path('categories/<slug:category_slug>/', views.main, name='category_wise_posts'),
    path('user/', include('user.urls')),
    path('categories/', include('categories.urls')),
    path('books/', include('books.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)