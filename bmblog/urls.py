from . import views
from django.urls import path, include


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('queries', include('queries.urls')),
    path('templates/about/', views.about, name='about'),
    path('edit-comment/<int:pk>', views.edit_comment, name='edit-comment'),
    path('delete-comment/<int:pk>', views.delete_comment, name='delete-comment'),
]

handler404 = "bmblog.views.page_not_found_view"
handler500 = "bmblog.views.internal_server_error_view"
