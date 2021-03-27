from django.db import models
from django.conf import settings
from django.urls import reverse


class Activity(models.Model):
    activity    = models.CharField(max_length=50)
    to_do_date  = models.DateTimeField()
    is_done     = models.BooleanField(default= False, blank=True)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('activity-detail', kwargs={'pk': self.pk})
    

