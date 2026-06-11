from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserModel(AbstractUser):
    USER_TYPE = [
        ('JobSeeker', 'JobSeeker'),
        ('Recruiter', 'Recruiter')
    ]
    display_name = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, choices=USER_TYPE)

    def __str__(self):
        return self.username
    

class RecruiterModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ImageField(upload_to='media/profile', null=True, blank=True)

    def __str__(self):
        return self.name
    
class SkillModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name or "Unnamed Skill"

class JobSeekerModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    skill = models.ManyToManyField(SkillModel)
    resume = models.FileField(upload_to='media/resume', null=True, blank=True)

    def __str__(self):
        return self.name

class JobModel(models.Model):
    CATAGORY = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship')
    ]
    user = models.ForeignKey(RecruiterModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    catagory = models.CharField(max_length=100, choices=CATAGORY)
    description = models.TextField()
    skills = models.ManyToManyField(SkillModel)

    def __str__(self):
        return f"{self.title}"
    

class ApplyJobModel(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('ShortList', 'ShortList'),
        ('Rejected', 'Rejected')
    ]
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    job_seeker = models.ForeignKey(JobSeekerModel, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS)