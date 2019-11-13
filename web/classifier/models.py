from django.db import models


class ImageFile(models.Model):
    """For tracking Image data
    """

    name = models.TextField(blank=True)
    file_hash = models.TextField(blank=True)
    # Audit Fields.
    created_ts = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, blank=True)
    updated_ts = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=100, blank=True)


class DataSource(models.Model):
    """For tracking data sources
    """

    name = models.TextField(blank=True)
