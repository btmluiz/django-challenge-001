from django.contrib.auth import login
from django.utils.translation import ugettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token

from api.models import Article
from api.serializers import LoginSerializer, SignupSerializer, ArticleSerializer, LoggedUserArticleSerializer, \
    AnonymousArticleSerializer


class LoginAuthToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'id': user.pk,
                'token': token.key,
            }

            login(request, user)

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class SignupAuthToken(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            data = {
                'id': user.pk,
                'token': token.key
            }

            login(request, user)

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ArticleView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        article_id = request.query_params.get('id', None)
        category = request.query_params.get('category', None)

        if category:
            return self.get_category(request, category)
        elif article_id:
            return self.get_detail(request, article_id)
        else:
            return self.get_default(request)

    def get_category(self, request, category):
        articles = Article.objects.filter(category=category).all()
        serializer = ArticleSerializer(instance=articles, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def get_detail(self, request, article_id):
        try:
            article = Article.objects.get(id=article_id)

            if request.user.is_authenticated:
                serializer = LoggedUserArticleSerializer(instance=article, many=False)
            else:
                serializer = AnonymousArticleSerializer(instance=article, many=False)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({
                "error": _("Article not found")
            }, status=status.HTTP_404_NOT_FOUND)

    def get_default(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(instance=articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
