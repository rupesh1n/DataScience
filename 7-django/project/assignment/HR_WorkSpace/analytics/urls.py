from django.urls import path
from django.views.generic import TemplateView
from .views import attrition_view, tenure_view, performance_view

urlpatterns = [
    # APIs
    path('attrition/', attrition_view, name='attrition'),
    path('tenure/', tenure_view, name='tenure'),
    path('performance/', performance_view, name='performance_api'),

    # Dashboards (Pages)
    path('attrition/dashboard/', TemplateView.as_view(
        template_name='analytics/attrition.html'
    ), name='attrition_dashboard'),
    path('tenure/dashboard/', TemplateView.as_view(
        template_name='analytics/tenure.html'
    ), name='tenure_dashboard'),
    path('workforce/overview/', TemplateView.as_view(
        template_name='analytics/workforce_overview.html'
    ), name='workforce_overview'),
    path(
        "performance/dashboard/",
        TemplateView.as_view(template_name="analytics/performance.html"),
        name="performance_dashboard"
    ),
]