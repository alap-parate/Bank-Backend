from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
from django.views.generic import TemplateView
from user_master.views import UserActivationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/',SpectacularAPIView.as_view(), name='schema'),
    path('doc/',SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('redoc/',SpectacularRedocView.as_view(url_name='schema'),name='redoc'),
    path('api/auth/activate/<uid>/<token>', UserActivationView.as_view({'get': 'activation'}), name='activation'),
    path('api/auth/',include('user_master.urls')),
    path('api/auth/',include('djoser.urls')),
    path('api/auth/',include('djoser.urls.jwt')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]