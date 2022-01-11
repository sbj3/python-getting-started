from django.db import models


class Folder(models.Model):
    """
    A folder is alanogous to a file system folder.  It can have a parent
    folder or multiple child folders.
    """
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self', related_name='folders', null=True, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='folders',
                              on_delete=models.RESTRICT)

    class Meta:
        ordering = ['name']


class Topic(models.Model):
    """
    A topic is a category used for research or grouping of documents.
    """
    name = models.CharField(max_length=30)
    short_desc = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=1000, blank=True, default='')
    docs = models.ManyToManyField('Document', through='DocTopic')
    created = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey('auth.User', related_name='topics',
    #                           on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']


class Document(models.Model):
    """
    A document is a file stored in the system.

    This model assumes it will be stored in the database.  If at a lter stage
    the files are stored in a file system, the document field would be removed
    and the file would then be stored and retrieved from the actual folder
    of the file system.
    """
    name = models.CharField(max_length=100)
    document = models.BinaryField()
    folder = models.ForeignKey(Folder, related_name='docs',
                               on_delete=models.RESTRICT)
    topics = models.ManyToManyField(Topic, through='DocTopic')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='docs',
                              on_delete=models.RESTRICT)

    class Meta:
        ordering = ['name']


class DocTopic(models.Model):
    doc_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    # owner = models.ForeignKey('auth.User', related_name='doctopics',
    #                           on_delete=models.CASCADE)

    class Meta:
        unique_together = ('doc_id', 'topic_id')
        ordering = ['doc_id']
        # order_by = 'doc_id'
