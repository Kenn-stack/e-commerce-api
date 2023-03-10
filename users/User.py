from __future__ import unicode_literals

# from django.db import models
from djongo import models
from django.core.mail import send_mail
from django.contrib.auth.models import  PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with given email and password
        """
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_("staff status"), default=False)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')






