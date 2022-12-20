from datetime import timezone
from django.db import models
import uuid
# from django.contrib.auth.validators import UnicodeUsernameValidator
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin,UserManager
# from django.utils.translation import gettext_lazy as _
# from django.utils import timezone
# from django.contrib.auth.models import Group
# from django.core.exceptions import PermissionDenied
# from django.contrib import auth



# # Used uuid in models 

class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=50)

    

# class MyUserManager(UserManager):
#      def _create_user(self, username, email, password, **extra_fields):
#         """
#         Create and save a user with the given username, email, and password.
#         """
#         if not username:
#             raise ValueError("The given username must be set")
#         email = self.normalize_email(email)
#         # Lookup the real model class from the global app registry so this
#         # manager method can be used in migrations. This is fine because
#         # managers are by definition working on the real model.
#         GlobalUserModel = apps.get_model(
#             self.model._meta.app_label, self.model._meta.object_name
#         )
#         username = GlobalUserModel.normalize_username(username)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#      def create_user(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(username, email, password, **extra_fields)

#      def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)

#         if extra_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must have is_staff=True.")
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must have is_superuser=True.")

#         return self._create_user(username, email, password, **extra_fields)


# class User(AbstractBaseUser,PermissionsMixin):
#     """
#     Add the fields and methods necessary to support the Group and Permission
#     models using the ModelBackend.
#     """

#     is_superuser = models.BooleanField(
#         _("superuser status"),
#         default=False,
#         help_text=_(
#             "Designates that this user has all permissions without "
#             "explicitly assigning them."
#         ),
#     )
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_("groups"),
#         blank=True,
#         help_text=_(
#             "The groups this user belongs to. A user will get all permissions "
#             "granted to each of their groups."
#         ),
#         related_name="user_set",
#         related_query_name="user",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_("user permissions"),
#         blank=True,
#         help_text=_("Specific permissions for this user."),
#         related_name="user_set",
#         related_query_name="user",
#     )

#     class Meta:
#         abstract = True

#     def get_user_permissions(self, obj=None):
#         """
#         Return a list of permission strings that this user has directly.
#         Query all available auth backends. If an object is passed in,
#         return only permissions matching this object.
#         """
#         return _user_get_permissions(self, obj, "user")

#     def get_group_permissions(self, obj=None):
#         """
#         Return a list of permission strings that this user has through their
#         groups. Query all available auth backends. If an object is passed in,
#         return only permissions matching this object.
#         """
#         return _user_get_permissions(self, obj, "group")

#     def get_all_permissions(self, obj=None):
#         return _user_get_permissions(self, obj, "all")

#     def has_perm(self, perm, obj=None):
#         """
#         Return True if the user has the specified permission. Query all
#         available auth backends, but return immediately if any backend returns
#         True. Thus, a user who has permission from a single auth backend is
#         assumed to have permission in general. If an object is provided, check
#         permissions for that object.
#         """
#         # Active superusers have all permissions.
#         if self.is_active and self.is_superuser:
#             return True

#         # Otherwise we need to check the backends.
#         return _user_has_perm(self, perm, obj)

#     def has_perms(self, perm_list, obj=None):
#         """
#         Return True if the user has each of the specified permissions. If
#         object is passed, check if the user has all required perms for it.
#         """
#         if not is_iterable(perm_list) or isinstance(perm_list, str):
#             raise ValueError("perm_list must be an iterable of permissions.")
#         return all(self.has_perm(perm, obj) for perm in perm_list)

#     def has_module_perms(self, app_label):
#         """
#         Return True if the user has any permissions in the given app label.
#         Use similar logic as has_perm(), above.
#         """
#         # Active superusers have all permissions.
#         if self.is_active and self.is_superuser:
#             return True

#         return _user_has_module_perms(self, app_label)


# class AbstractUser(AbstractBaseUser, PermissionsMixin):
#     """
#     An abstract base class implementing a fully featured User model with
#     admin-compliant permissions.

#     Username and password are required. Other fields are optional.
#     """

#     username_validator = UnicodeUsernameValidator()

#     username = models.CharField(
#         _("username"),
#         max_length=150,
#         unique=True,
#         help_text=_(
#             "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
#         ),
#         validators=[username_validator],
#         error_messages={
#             "unique": _("A user with that username already exists."),
#         },
#     )
  
#     email = models.EmailField(_("email address"), blank=False,unique=True)
#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin site."),
#     )
#     is_active = models.BooleanField(
#         _("active"),
#         default=True,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )
#     date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
#     email_verified=models.BooleanField(
#         _("email_verified"),
#         default=False,
#         help_text=_(
#             "Designates whether this user should be treated as active. "
#             "Unselect this instead of deleting accounts."
#         ),
#     )

#     objects = MyUserManager()

#     EMAIL_FIELD = "email"
#     USERNAME_FIELD = "username"
#     REQUIRED_FIELDS = ["email"]



#     def token(self):
#         return ''

    
class Place(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)    


class Todo(models.Model):
    OPEN = 'Open'
    CLOSED = 'Closed'
    UPCOMING = "Upcoming"
    GRADED = "Graded"

    PREDICTION_STATUS = (
        (OPEN, OPEN),
        (CLOSED, CLOSED),
        (UPCOMING, UPCOMING),
        (GRADED, GRADED),
    )

    status = models.CharField(
        choices=PREDICTION_STATUS,
        max_length=25,
        default=OPEN
    )


def __str__(self):
    print (self.status)
   
   

def update_status(self):
    if self.status == 'Open':
        
        self.status = 'Closed'
    elif self.status == 'closed':
        self.status = 'Open'
    self.save()


class Test(models.Model):
    name=models.CharField(max_length=100)

