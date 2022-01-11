from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from docs import views

from docs.views import DocViewSet, FolderViewSet, TopicViewSet, DocTopicViewSet
from docs.views import UserViewSet
from docs.views import api_root


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'docs', views.DocViewSet)
router.register(r'topics', views.TopicViewSet)
router.register(r'doctopics', views.DocTopicViewSet)
router.register(r'folders', views.FolderViewSet)

doc_list = DocViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
doc_detail = DocViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

doctopic_list = DocTopicViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
doctopic_detail = DocTopicViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

folder_list = FolderViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
folder_detail = FolderViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

topic_list = TopicViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
topic_detail = TopicViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})


# API endpoints

"""
There needs to be a search endpoint for each of documents, folders and topics.
"""
urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('docs/', doc_list, name='document-list'),
    path('docs/<int:pk>/', doc_detail, name='document-detail'),
    path('folders/', folder_list, name='folder-list'),
    path('folders/<int:pk>/', folder_detail, name='folder-detail'),
    path('topics/', topic_list, name='topic-list'),
    path('topics/<int:pk>/', topic_detail, name='topic-detail'),
    path('doctopics/', doctopic_list, name='doctopic-list'),
    path('doctopics/<int:pk>/', doctopic_detail, name='doctopic-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail'),
])

urlpaterns = format_suffix_patterns(urlpatterns)

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
