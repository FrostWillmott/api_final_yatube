from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, mixins, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    )

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs["post_id"])
        serializer.save(author=self.request.user, post_id=post.id)


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.UpdateModelMixin,
    # mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    # queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        # following = serializer.validated_data.get("following")
        # if self.request.user == following:
        #     raise ValidationError("Вы не можете следовать за собой.")
        # if Follow.objects.filter(
        #     user=self.request.user,
        #     following=following,
        # ).exists():
        #     raise ValidationError("Вы уже подписаны на этого пользователя.")
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)
