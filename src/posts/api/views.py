from rest_framework.generics import (
					CreateAPIView,
					ListAPIView,
		 			RetrieveAPIView,
		 			DestroyAPIView,
		 			UpdateAPIView,
		 			RetrieveUpdateAPIView,
		 			)

from posts.models import Post
from .serializers import (
		PostCreateUpdateSerializer,
		PostListSerializer, 
		PostDetailSerializer,
		)


class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer

	def perform_create(self,serializer):
		serializer.save(user=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	#lookup_url_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostCreateUpdateSerializer
	lookup_field = 'slug'
	#lookup_url_field = 'slug'

	def perform_update(self,serializer):
		serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'slug'
	#lookup_url_field = 'slug'

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

