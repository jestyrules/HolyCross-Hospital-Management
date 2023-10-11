from django.db import models


# Create your models here.
class Appoinmentdb(models.Model):
    Department = models.CharField(max_length=50, null=True, blank=True)
    DrName = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=60, unique=True, null=True, blank=True)
    Date = models.CharField(max_length=60, null=True, blank=True)
    Time = models.CharField(max_length=50, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True, unique=True)


class Registerdb(models.Model):
    Username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)


class Blogdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=60, blank=True, null=True)
    Subject = models.CharField(max_length=500, null=True, blank=True)
    Message = models.CharField(max_length=500, null=True, blank=True)


class Profiledb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    Birthday = models.CharField(max_length=50, null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Image = models.ImageField(upload_to="ProfileImage")


class Appointmentdb(models.Model):
    DrName = models.CharField(max_length=50, null=True, blank=True)
    Registrations = models.IntegerField(null=True, blank=True)
    Username = models.CharField(max_length=50,null=True, blank=True)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True,blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Date = models.CharField(max_length=50, null=True, blank=True)
    Time = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.Registrations, self.DrName}"
