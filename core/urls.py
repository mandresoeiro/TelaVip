
# core/urls.py
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cine.views import NewCineCreateView, CineListView, CineDetailView, CineUpdateView, CineDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('', CineListView.as_view(), name='cine_list'),
    path('new_cine/', NewCineCreateView.as_view(), name='new_cine'),
    path('cine/<int:pk>/', CineDetailView.as_view(), name='cine_detail'),
    path('cine/<int:pk>/update/', CineUpdateView.as_view(), name='cine_update'),
    path('cine/<int:pk>/delete/', CineDeleteView.as_view(), name='cine_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
