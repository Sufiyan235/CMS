from django.db import models
from account.models import Account
# Create your models here.

class New_Folder(models.Model):
    pass


class File(models.Model):
    file_name = models.CharField(max_length=100,null=True,blank=True)
    has_access = models.ManyToManyField(Account)
    file = models.FileField(upload_to="All Files",null=True,blank=True)

    def __str__(self):
        return f"{self.file_name}"


    def has_access_to(self):
        return ",".join([str(p) for p in self.has_access.all()])  