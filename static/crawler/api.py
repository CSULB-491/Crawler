from crawler.models import NewArticle
from rest_framework import viewsets, permissions
from crawler.static.crawler.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset =  NewArticle.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArticleSerializer