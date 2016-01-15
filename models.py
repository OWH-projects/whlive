from django.db import models
from django.template.defaultfilters import slugify

class Show(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='whlive/', max_length=100, null=True, blank=True)
    show_url = models.CharField("Show URL", max_length=200, null=True, blank=True)
    nameslug = models.CharField(max_length=200, null=True, blank=True, editable=False)
    
    def __unicode__(self):
        return self.name

    def save(self):
        self.nameslug = slugify(self.name)
        super(Show, self).save()
   	
		
class Segment(models.Model):
    show = models.ForeignKey(Show)
    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    mp3_link = models.CharField(max_length=200, blank=True)
    nameslug = models.CharField(max_length=100, null=True, blank=True, editable=False)

    def __unicode__(self):
        return self.name

    def save(self):
        self.nameslug = slugify(self.name)
        super(Segment, self).save()
		
		
class Schedule(models.Model):
    show = models.ForeignKey(Show)
    text = models.TextField()
    date = models.DateField(blank=True, null=True)