from django.db import models

# Create your models here.


class registerdetails(models.Model):
    Name = models.CharField(max_length=20)
    Designation = models.CharField(max_length=20)
    Gender = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Team = models.CharField(max_length=20)
    Teamlead = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Contact = models.CharField(max_length=20)
    Picture = models.FileField()



class assignproject(models.Model):
    Project_Name = models.CharField(max_length=40, null=True)
    Project = models.FileField()
    Deadline = models.DateField(null=True)


    def __str__(self):
        return self.Project_Name


class assignprojecttoteam(models.Model):
    Project_Name = models.CharField(max_length=40)
    Project = models.FileField()
    Deadline = models.DateField()
    Team = models.CharField(max_length=20, default='')
    Teamlead = models.CharField(max_length=20, default='')
    Project_Report = models.FileField(null=True)
    Status = models.BooleanField(default=False)
    Verification = models.BooleanField(default=False)
    Submit = models.BooleanField(default=False)


class createteam(models.Model):
    Team_Name = models.CharField(max_length=20)
    Manager = models.CharField(max_length=20)

