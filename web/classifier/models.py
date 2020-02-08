from django.db import models


class ImageFile(models.Model):
    """Individual image tracks image data
    """
    name = models.TextField(blank=True)
    datasource = models.ForeignKey('classifier.ClassificationType', related_name='classifier_classification_type', on_delete=models.CASCADE)
    anchor_x = models.IntegerField(null=False)
    anchor_y = models.IntegerField(null=False)
    length_x = models.IntegerField(null=False)
    length_y = models.IntegerField(null=False)

    # Audit Fields.
    created_ts = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_ts = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True)


class DataSource(models.Model):
    """For tracking data sources
    """
    name = models.TextField(blank=True)


class ClassificationType(models.Model):
    """Classification Type
    """
    name = models.TextField(blank=True)

    # Audit Fields.
    created_ts = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_ts = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True)
