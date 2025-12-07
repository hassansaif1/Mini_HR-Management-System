from django.urls import path
from . import views  

urlpatterns = [
    path('leave-request/', views.leave_request, name='leave_request'),
    path("apply-leave/", views.apply_leave, name='apply_leave'),
    
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<uuid:id>/<str:status>/', views.update_status, name='update_status'),

]