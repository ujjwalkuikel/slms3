from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.



def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(instance.user.username, ext)
    return os.path.join(upload_to, filename)

#user models
class all_users(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    bio = models.CharField(max_length=100,blank=True)
    profile_pic = models.ImageField(upload_to= path_and_rename , verbose_name="profile_picture", blank=True)

    teacher= 'teacher'
    student = 'student'
    user_types = [
        (teacher,'teacher'),
        (student,'student'),  
    ]
    user_types = models.CharField(max_length=10, choices=user_types,default=student)


    class5 = 'class5'
    class6 = 'class6'
    class7 = 'class7'
    class8 = 'class8'
    class9 = 'class9'
    class10 = 'class10'
    faculty='faculty'
    class_list = [
        (class5,'class5'),
        (class6,'class6'),
        (class7,'class7'),
        (class8,'class8'),
        (class9,'class9'),
        (class10,'class10'),
        (faculty,'faculty'),
    ]
    class_list = models.CharField(max_length=10, choices=class_list,default=class5)

    def __str__(self):
        return self.user.username

