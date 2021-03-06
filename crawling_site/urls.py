from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
]

urlpatterns += i18n_patterns(
    path('', include('movies.urls', namespace='movies')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('comments/', include('comments.urls', namespace='comments')),
    path('admin/', admin.site.urls),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
