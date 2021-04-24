from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',  # Url endpoint
                views.HelloApiViewSet,
                base_name='hello-viewset'  # use when you want to override model name or not using model
                )
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))  # '' since we do NOT want to include prefix to our URLs
]
