from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from portfolio.views import (
    ProjectListCreateView, ProjectDetailView,
    ExperienceListCreateView, ExperienceDetailView,
    GalleryImageListCreateView, GalleryImageDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('api/experience/', ExperienceListCreateView.as_view(), name='experience-list-create'),
    path('api/experience/<int:pk>/', ExperienceDetailView.as_view(), name='experience-detail'),
    path('api/gallery/', GalleryImageListCreateView.as_view(), name='gallery-list-create'),
    path('api/gallery/<int:pk>/', GalleryImageDetailView.as_view(), name='gallery-detail'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)