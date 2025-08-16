from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, username, phone, password=None,
                    is_staff=False,
                    is_active=True,
                    is_superuser=False,
                    **extra_fields):
        user = self.model(
            username=username,
            phone=phone,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(str(password))
        user.save()
        return user

    def create_superuser(self, username, phone, password=None, **extra_fields):
        return self.create_user(
            username=username,
            phone=phone,
            password=password,
            is_superuser=True,
            is_staff=True,
            **extra_fields
        )