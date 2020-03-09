from rest_framework import routers
from crawler.static.crawler.api import ArticleViewSet

router = routers.DefaultRouter()
router.register('api/Articles', ArticleViewSet,'articles')

urlpatterns = router.urls
