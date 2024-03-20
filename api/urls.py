from django.contrib import admin
from django.urls import path, include
from api.views import DoctorView, ServiceView, AppointmentView, PatientView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'doctor/<int:pk>/',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:pk>/',
        PatientView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:pk>/patient/',
        DoctorView.as_view({
            'get': 'list_patient',
        })
    ),
    path(
        'service/',
        ServiceView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'service/<int:pk>/',
        ServiceView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'appointment/',
        AppointmentView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'appointment/<int:pk>/',
        AppointmentView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
