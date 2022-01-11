from rest_framework import serializers
# from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from docs.models import Document, Folder, Topic, DocTopic
from django.contrib.auth.models import User


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    parent_name = serializers.ReadOnlyField(source='parent.name')
    docs = serializers.HyperlinkedRelatedField(
        many=True, view_name='document-detail', read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Folder
        fields = ['id', 'url', 'name',
                  'parent_name', 'parent',
                  'docs',
                  'owner']


class DocSerializer(serializers.HyperlinkedModelSerializer):
    folder_name = serializers.ReadOnlyField(source='folder.name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Document
        fields = ['id', 'url', 'name', 'document',
                  'folder_name', 'folder',
                  'topics',
                  'owner']


class TopicSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Topic
        fields = ['id', 'url', 'name', 'short_desc', 'description', 'docs']


class DocTopicSerializer(serializers.HyperlinkedModelSerializer):
    docs = DocSerializer(read_only=True, many=True)
    topics = TopicSerializer(read_only=True, many=True)
    # doc_name = serializers.ReadOnlyField(source='document.name')

    class Meta:
        model = DocTopic
        # fields = "__all__"
        fields = ['id', 'url', 'created',
                  'doc_id', 'topic_id',
                  'docs', 'topics']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    docs = serializers.HyperlinkedRelatedField(
        many=True, view_name='doc-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'docs']
