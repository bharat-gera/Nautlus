from django.db import models
from django.contrib.auth.hashers import check_password, make_password,is_password_usable
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

class PersonManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        create and save user
        """
        if not email:
            raise ValueError('Users can be only created using a email')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        create and save superuser
        """
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Person(PermissionsMixin):
    
    email = models.EmailField(_('Email address'), max_length=255, unique=True,)
    password = models.CharField(_('Password'), max_length=128,
                                validators=[MinLengthValidator(6)])

    name = models.CharField(_('Name'), max_length=255)

    
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Admin'), default=False)
    
    is_email_verified = models.BooleanField(_('Email Verified'), default=False)
    is_contact_verified = models.BooleanField(_('Contact Verified'),
                                              default=False)
    
    date_joined = models.DateField(_('Date_signal Joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), default=timezone.now)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        # managed = False

    REQUIRED_FIELDS = []
    objects = PersonManager()

    USERNAME_FIELD = 'email'
    
    def get_full_name(self):
        
        if self.name is not None: 
            return self.name
        else:
            self.name = ''
            return self.name 
            
    def get_username(self):
        "Return the identifying username for this User"
        return getattr(self, self.USERNAME_FIELD)

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

    def natural_key(self):
        return (self.get_username(),)

    def is_anonymous(self):
        """
        Always returns False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """
        Returns a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def set_unusable_password(self):
        self.password = make_password(None)

    def has_usable_password(self):
        return is_password_usable(self.password)

def profile_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = 'user_id_' + str(instance.owner.id) + '.' + ext
    return '/'.join(['person/profile-image', str(instance.owner.id), filename])

class Profile(models.Model):
    
    owner = models.OneToOneField('person.Person', unique=True,
                                 related_name='profile')
    
    contact_num = models.CharField(_("Phone Number"), max_length=255, null=True, unique=True)
    about_yourself = models.TextField(_("About Yourself"),max_length=150,blank=True,null=True)
    
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return "owner_name:%s"%(self.owner.name)
    
class ProfileImage(models.Model):
    owner = models.OneToOneField('person.Person', unique=True,
                                 related_name='profile_image')
    image = models.ImageField(upload_to=profile_image_path, blank=True, null=True,default='media/person/profile-image/default.jpg')
