from django.contrib import admin
from django.urls import path, include
from analytics.views import home  # use your home view in analytics

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # APIs and pages are defined in analytics/urls.py
    path('api/', include('analytics.urls')),
    path('analytics/', include('analytics.urls')),  # for pages like /analytics/performance/dashboard/
]