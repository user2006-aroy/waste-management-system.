from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portal import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("report/", views.report_issue, name="report"),
    path("track/", views.track_complaint, name="track"),
    path("awareness/", views.awareness, name="awareness"),
    path("reports/", views.reports, name="reports"),
    path("register/", views.register, name="register"),
    path("accounts/login/", views.login_view, name="login"),
    path("accounts/logout/", views.logout_view, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
