from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager): 

    def create_user(self, email, name,password=None,**extrafields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email = email,name=name, **extrafields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extrafields):
        extrafields.setdefault('is_staff', True)
        extrafields.setdefault('is_superuser', True)
        extrafields.setdefault('is_active', True)

        if extrafields.get('is_staff') is not True:
            raise ValueError('superuser must have is_Staff=True.')
        if extrafields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True.')
        return self.create_user(email, password, **extrafields)
    

    # use_in_migrations=True
    # def _create_user(self,email,password,**extrafields):
    #     if not email:
    #         raise ValueError("The given email must be set")
    #     email = self.normalize_email(email)
    #     user = self.model(email = email, **extrafields)
    #     user.set_password(password)
    #     user.save(using=self._db)
    #     return user