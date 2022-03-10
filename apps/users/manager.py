from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,  phone_number,email, password=None):
        if not email:
            raise ValueError("user most have a email")
        user = self.model(
            email=self.normalize_email(email),
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user