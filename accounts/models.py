from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccount(BaseUserManager):
    def create_user(self, username, email, password):

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    username = models.CharField(max_length=11, unique=True, verbose_name="使用者帳號")
    email = models.EmailField(unique=True, verbose_name="信箱")
    phone_number = models.CharField(max_length=10, verbose_name="手機號碼")
    password = models.CharField(max_length=20, verbose_name="密碼")
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccount()

    class Meta:
        verbose_name = "使用者"
        verbose_name_plural = "使用者"

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
    
