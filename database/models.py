from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.

class Evaluation(models.Model):
    def get_default_keywords():
        return list(['none'])
    title = models.CharField(max_length=50, blank=True, default=None)
    start_date = models.DateField(blank=True, default=None)
    end_date = models.DateField(blank=True,default=None)
    NRO = models.CharField(blank=True,max_length=50, default=None)
    evaluator = models.CharField(blank=True,max_length=50, default=None)
    cause_area = models.CharField(blank=True,max_length=50, default=None)
    keywords = ArrayField(
        models.CharField(max_length=20, blank=True, default=None),
        size=50,
        default=get_default_keywords
    )
    executive_summary = models.TextField(blank=True,default=None)
    link = models.CharField(max_length=200, blank=True,default=None)
    embed_link = models.CharField(max_length=200,blank=True, default=None)
    def __str__(self):
        return "NRO: {NRO}, evaluator: {evaluator}, date: {date}".format(NRO=self.NRO, evaluator=self.evaluator, date=self.start_date)



