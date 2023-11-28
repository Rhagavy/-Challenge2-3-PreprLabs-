from django.db import models
import uuid
from django.contrib.auth.models import User, AbstractUser
# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    first_name = models.CharField(max_length=200,blank=False,null=False)
    last_name = models.CharField(max_length=100,blank=False,null=False)
    user_type = models.CharField(max_length=100,blank=False,null=False)
    language = models.CharField(max_length=100,blank=False,null=False)
    # dateOfBirth = models.DateField(default="1995-01-01")
    # postSecondaryInstitution = models.CharField(max_length = 300, default="Brock University")
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email
    
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)
    owner = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    projectName = models.CharField(max_length=200,blank=False,null=False)
    projectOverview = models.CharField(max_length=500,blank=False,null=False)
    bannerImage = models.ImageField(upload_to='',blank=False, null=False)
    startDate = models.DateField(default="2024-01-01")
    recruitingStatus = models.CharField(max_length=200,blank=False,null=False)
    slug = models.CharField(max_length=200,blank=False,null=False)
    type = models.CharField(max_length=200,blank=False,null=False)
    category = models.CharField(max_length=200,blank=False,null=False)
    stage = models.CharField(max_length=200,blank=False,null=False)
    projectStatus = models.CharField(max_length=200,blank=False,null=False)

    def __str__(self):
        return self.projectName