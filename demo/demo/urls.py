
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin


urlpatterns = [
    # Examples:
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('tests/', include('app1.urls')),
    path('admin/', admin.site.urls),
]