from django.db import models

# Create your models here.
class StatusPR(models.Model): 
    status = models.CharField(max_length=255)
    def __str__(self):
        return self.status



class PR(models.Model): 
    tgl_pr = models.DateField()
    partnumber = models.CharField(max_length=255, blank=True, unique=False)
    partname = models.CharField(max_length=255)
    qty = models.IntegerField()
    deskripsi = models.CharField(max_length=255, blank=True)
    status = models.ForeignKey(StatusPR, on_delete=models.CASCADE)
    #status = models.CharField(max_length=255, null=True, blank=True)
    #delete = models.CharField(max_length=255, default=False)

