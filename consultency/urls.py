"""
URL configuration for consultency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from user import views as user_view  # Import views from your user app
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # Assuming you have a dashboard app with its own urls.py

    # User management URLs
    path('register/', user_view.register, name='user-register'),
    path('profile/', user_view.profile, name='profile'),
    path('edit-personal-details/', user_view.edit_personal_details, name='edit_personal_details'),

    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    path('logout/', auth_views.LogoutView.as_view(), name='user-logout'),

    # Employee-specific URLs
    path('edit/', user_view.edit_employee_details, name='edit_employee_details'),
    path('employee/dashboard/', user_view.employee_dashboard, name='employee_dashboard'),

    # Manager-specific URLs
    path('assign-task/', user_view.assign_task, name='assign_task'),
    path('issue-offer-letter/', user_view.issue_offer_letter, name='issue_offer_letter'),
    path('handle-payroll/', user_view.handle_payroll, name='handle_payroll'),
    path('manager/dashboard/', user_view.manager_dashboard, name='manager_dashboard'),
    path('unauthorized/', user_view.unauthorized, name='unauthorized'),
    path('submit-attendance/', user_view.submit_attendance, name='submit_attendance'),
    path('attendance/', user_view.attendance, name='attendance'),
    path('upload-offer-letter/', user_view.upload_offer_letter, name='upload_offer_letter'),
    path('upload-payroll/', user_view.upload_payroll, name='upload_payroll'),
    path('view-offer-letter/', user_view.view_offer_letter, name='view_offer_letter'),
    path('view-payrolls/', user_view.view_payrolls, name='view_payrolls'),

]

# Static and media file handling during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

