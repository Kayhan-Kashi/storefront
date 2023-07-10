from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # Type (product, video, article)
    # ID
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # if object type is removed we wantto remove all associated tags
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    # using this field we can read an acutual object that particular tag is applied to 
    


