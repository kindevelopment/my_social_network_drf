from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ParseError


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_num,  email, password, **extra_fields):
        if not username:
            raise ParseError('Укажите никнейм пользователя')
        else:
            user = self.model(username=username, **extra_fields)

        if not email:
            raise ParseError('Укажите email')
        else:
            email = self.normalize_email(email)
            user.email = email

        if not phone_num:
            raise ParseError('Укажите номер-телефона')
        else:
            user.phone_num = phone_num
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, phone_num=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, phone_num, email, password, **extra_fields)

    def create_superuser(self, username, phone_num=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if not extra_fields.get("is_staff"):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get("is_superuser"):
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, phone_num, email, password, **extra_fields)