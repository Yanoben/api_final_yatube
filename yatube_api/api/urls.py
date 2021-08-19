from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet

router = SimpleRouter()
router.register('v1/posts', PostViewSet, basename='post')
router.register('v1/groups', GroupViewSet, basename='group')
router.register(r'v1/posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
