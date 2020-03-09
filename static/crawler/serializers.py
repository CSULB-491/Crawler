from rest_framework import serializers
from crawler.models import NewArticle


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewArticle
        fields = '__all__'
