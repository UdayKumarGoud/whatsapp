from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.db.models.signals import post_save
from django.core import signing
# from rest_framework.authtoken.models import Token
import binascii
import os, uuid
from six import python_2_unicode_compatible

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True

@python_2_unicode_compatible
class Token(TimeStampedModel):
    """
    The authorization token model based on Mac Address (not user)
    """
    key = models.CharField(max_length=40, primary_key=True)
    user = models.OneToOneField('users.AppUser', related_name='auth_token', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key

class AppUser(TimeStampedModel):
    first_name = models.CharField(max_length=255,blank=True)                                     
    last_name = models.CharField(max_length=255, blank=True) 
    password = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=255,blank=True)
    email = models.EmailField(max_length=255, unique=True)                      
    mobile = models.CharField(max_length=255, unique=True)                       
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True)
    is_logged_in = models.BooleanField(default=False)
    is_finovera_registered = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.mobile
    
    def user_agent(self, request):
        return request.user_agent.os.family
    
    def loggedIn(sender, user, **kwargs):
        """
        A signal receiver which updates the last_login date for
        the user logging in.
        """
        if user.is_logged_in == False:
            user.is_logged_in = True
        else:
            user.is_logged_in = False
        user.save(update_fields=["is_logged_in"])
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_anonymous(self):
        return False


@receiver(post_save, sender=AppUser)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)  
