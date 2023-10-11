from django.db import models


# Create your models here.
class Deptdb(models.Model):
    DeptName = models.CharField(max_length=50, blank=True, null=True)
    Description = models.CharField(max_length=500, blank=True, null=True)
    Image = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return f"{self.DeptName}"


class Doctordb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Experience = models.CharField(max_length=50, null=True, blank=True)
    Education = models.CharField(max_length=200, null=True, blank=True)
    Registrations = models.CharField(unique=True, max_length=40, null=True, blank=True)
    Timing = models.CharField(max_length=50, null=True, blank=True)
    Language = models.CharField(max_length=100, null=True, blank=True)
    About = models.CharField(max_length=100, null=True, blank=True)
    Gender = models.CharField(max_length=40, null=True, blank=True)
    Image = models.ImageField(upload_to="dr-img", null=True, blank=True)



