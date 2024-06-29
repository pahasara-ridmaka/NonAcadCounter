from django.urls import path
from .views import countdown_timer, like_comment

urlpatterns = [
    path('', countdown_timer, name='countdown_timer' ),
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment' ),
]
