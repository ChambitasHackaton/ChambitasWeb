from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from string import join
from oficios.models import Oficio

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, is_superuser, is_active, is_staff):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            password=password,
            is_active=is_active,
            is_superuser=is_superuser,
            is_staff=is_staff,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self, email,password=None):
        return self._create_user(email, password, False, True, False)

    def create_superuser(self, email, password):
        return self._create_user(email, password, True, True, True)

class MyUser(AbstractBaseUser):

    DELEGACIONES_CHOICES = (
        ('Alvaro Obregon', 'Alvaro Obregon'),
        ('Azcapotzalco', 'Azcapotzalco'),
        ('Benito Juarez', 'Benito Juarez'),
        ('Coyoacan', 'Coyoacan'),
        ('Cuajimalpa De Morelos', 'Cuajimalpa De Morelos'),
        ('Cuauhtemoc', 'Cuauhtemoc'),	
        ('Gustavo A Madero', 'Gustavo A. Madero'),
        ('Iztacalco', 'Iztacalco'),
        ('Iztapalapa', 'Iztapalapa'),
        ('La Magdalena Contreras', 'La Magdalena Contreras'),
        ('Miguel Hidalgo', 'Miguel Hidalgo'),
        ('Milpa Alta', 'Milpa Alta'),
        ('Tlahuac', 'Tlahuac'),
        ('Tlalpan', 'Tlalpan'),
        ('Venustiano Carranza', 'Venustiano Carranza'),
        ('Xochimilco', 'Xochimilco'),
    )

    first_name = models.CharField(max_length=200, blank=True, help_text="The first name of the user.")
    last_name = models.CharField(max_length=200, blank=True, help_text="The last name of the user.")
    telephone = models.IntegerField(null=True)
    delegacion = models.CharField(max_length=20, choices=DELEGACIONES_CHOICES)
    zip_code = models.CharField(max_length=5)
    credencial = models.CharField(null=True, max_length=18)
    oficio = models.ForeignKey(Oficio, blank=True, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True, 
        verbose_name="Active"
    )
    is_staff = models.BooleanField(
    	default=True,
    	verbose_name='Staff Status')
    is_superuser = models.BooleanField(
        default=True, 
        verbose_name="Superuser"
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        if self.first_name == "" and self.last_name == "":
            return self.email
        else:
            return self.first_name + " " + self.last_name
    get_full_name.short_description = 'Name'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True