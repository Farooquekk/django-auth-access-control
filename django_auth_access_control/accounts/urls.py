from django.urls import path
from .views import login_view,logout_view,profile_view,dashboard_view,export_view

urlpatterns=[
    path("login/",login_view),
    path("profile/",profile_view),
    path("logout/",logout_view),
    path("dashboard/",dashboard_view),
    path("export/",export_view)
    
]