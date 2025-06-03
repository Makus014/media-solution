
from django.db import models

"""

"""
class DatabaseConnector(models.Model):

    title = models.CharField(max_length=255)
    content = models.JSONField(default=dict)
    keywords = models.JSONField()
    analyzed_by = models.CharField(max_length=100)
    image_url = models.URLField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_creation = models.DateField()


    trend_score = models.IntegerField(default=0)
    trend_explanation = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = 'news'
    
    def __str__(self):
        return self.title
    
    

