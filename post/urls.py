from rest_framework import routers
from post.api import PostViewSet


router = routers.DefaultRouter()
router.register('api/post', PostViewSet, 'post')


urlpatterns = router.urls
