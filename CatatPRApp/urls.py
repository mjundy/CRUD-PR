from django.urls import path
from . import views
urlpatterns = [
    path('', views.ListPR.as_view(), name='list_pr'),
    path('register/', views.RegisterPR.as_view(), name='register_pr'),
    path('<int:pk>/update/', views.UpdatePR.as_view(), name='update_pr'),
    path('<str:pk>/delete/', views.DeletePR.as_view(), name='delete_pr'),
    path('list/statuspr', views.ListStatusPR.as_view(), name='list_status_pr'),
    path('register/statuspr', views.RegisterStatusPR.as_view(), name='register_status_pr'),
    path('<int:pk>/statuspr/update/', views.UpdateStatusPR.as_view(), name='update_status_pr'),
    path('<int:pk>/statuspr/delete/', views.DeleteStatusPR.as_view(), name='delete_status_pr'),
]
