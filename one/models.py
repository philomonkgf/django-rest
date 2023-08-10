from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class Makeuser(BaseUserManager):
    def create_user(self,username,email,password,*args,**kwargs):
        if not email:
            raise ValueError('should should have email')
        
        if not username:
            raise ValueError('user should have username')
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    
    def create_superuser(self,username,email,password,*args,**kwargs):
        
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)
        return user
    



class Newuser(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25)
    bio = models.ImageField()
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now=True)
    date_login = models.DateTimeField(auto_now_add=True)
    
    
    USERNAME_FIELD = ('email')
    REQUIRED_FIELDS = ['username']
    object = Makeuser()
    
    




class Task(models.Model):
    name = models.ForeignKey(Newuser,on_delete=models.CASCADE)
    taskname = models.CharField(max_length=15)
    taskimage = models.ImageField()
    abouttask = models.TextField()
    task_create = models.DateTimeField(auto_now=True)
    task_edit = models.DateTimeField(auto_now_add=True)