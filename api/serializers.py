from django.contrib.auth import authenticatefrom django.contrib.auth.models import Userfrom django.utils.translation import ugettext_lazy as _from rest_framework import serializersfrom api.models import Author, Articleclass LoginSerializer(serializers.Serializer):    username = serializers.CharField(max_length=255)    password = serializers.CharField(        label=_('Password'),        style={'input_type': 'password'},        trim_whitespace=False,        max_length=255,        write_only=True    )    def validate(self, data):        username = data.get('username', None)        password = data.get('password', None)        user = authenticate(username=username, password=password, request=self.context.get('request'))        if not user:            raise serializers.ValidationError(                _('User not found'),                code='authorization'            )        data['user'] = user        return dataclass SignupSerializer(serializers.Serializer):    username = serializers.CharField(max_length=255)    email = serializers.EmailField()    first_name = serializers.CharField(max_length=255)    last_name = serializers.CharField(max_length=255)    password = serializers.CharField(        label=_('Password'),        style={'input_type': 'password'},        trim_whitespace=False,        max_length=255,        write_only=True    )    confirm_password = serializers.CharField(        label=_('Password confirmation'),        style={'input_type': 'password'},        trim_whitespace=False,        max_length=255,        write_only=True    )    def validate(self, data):        username = data.get('username', None)        email = data.get('email', None)        first_name = data.get('first_name', None)        last_name = data.get('last_name', None)        password = data.get('password', None)        confirm_password = data.get('confirm_password', None)        picture = data.get('picture', None)        if password != confirm_password:            raise serializers.ValidationError({                'password': _("Password does not match with password confirmation")            })        try:            Author.objects.get(username=username)            raise serializers.ValidationError({                'username': _("Username already exits.")            })        except Author.DoesNotExist:            user = Author.objects.create_user(username=username,                                              email=email,                                              first_name=first_name,                                              last_name=last_name,                                              password=password,                                              picture=picture)            data['user'] = user            return dataclass AuthorSerializer(serializers.ModelSerializer):    name = serializers.SerializerMethodField('get_name')    def get_name(self, instance):        return instance.get_full_name()    class Meta:        model = Author        fields = ('id', 'name', 'picture',)class AdminAuthorSerializer(AuthorSerializer):    class Meta:        model = Author        exclude = ('password',)class ArticleSerializer(serializers.ModelSerializer):    author = AuthorSerializer(read_only=True)    class Meta:        model = Article        fields = ('id', 'author', 'category', 'title', 'summary',)class AnonymousArticleSerializer(ArticleSerializer):    class Meta:        model = Article        fields = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph',)class LoggedUserArticleSerializer(ArticleSerializer):    class Meta:        model = Article        fields = ('id', 'author', 'category', 'title', 'summary', 'firstParagraph', 'body')class AdminArticleSerializer(ArticleSerializer):    class Meta:        model = Article        fields = '__all__'