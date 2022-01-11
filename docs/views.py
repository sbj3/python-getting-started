
# from snippets.models import Snippet
# from snippets.permissions import IsOwnerOrReadOnly
# from snippets.serializers import SnippetSerializer
# from snippets.serializers import UserSerializer

from docs.models import Document, Folder, Topic, DocTopic
from docs.permissions import IsOwnerOrReadOnly
from docs.serializers import DocSerializer
from docs.serializers import FolderSerializer
from docs.serializers import TopicSerializer
from docs.serializers import DocTopicSerializer
from docs.serializers import UserSerializer

# from rest_framework import generics
from rest_framework import permissions
# from rest_framework import renderers
from rest_framework import viewsets

from rest_framework.decorators import api_view
# from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from django.contrib.auth.models import User


@api_view
def api_root(request, format=None):
    return Response({
        'docs': reverse('document-list', request=request, format=format),
        'folders': reverse('folder-list', request=request, format=format),
        'topics': reverse('topic-list', request=request, format=format),
        # 'users': reverse('user-list', request=request, format=format),
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'retrieve' actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DocViewSet(viewsets.ModelViewSet):
    """
    A document is in a folder and may have many topics.
    """
    queryset = Document.objects.all()
    serializer_class = DocSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FolderViewSet(viewsets.ModelViewSet):
    """
    A folder may hold documents or folders.

    A folder should only be removed if it is empty.
    """
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TopicViewSet(viewsets.ModelViewSet):
    """
    A topic is used to categorize documents.
    One document may have several topics.
    """
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer


class DocTopicViewSet(viewsets.ModelViewSet):
    """
    The many to many data structure that connects documents to topics.
    """
    queryset = DocTopic.objects.all()
    serializer_class = DocTopicSerializer
