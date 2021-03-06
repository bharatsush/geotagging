from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class GeoData_table(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    image  = models.CharField(max_length=200)
    lat = models.FloatField(blank=False, null=False)
    lng = models.FloatField(blank=False, null=False)


    class Meta:
        ordering = ('created',)