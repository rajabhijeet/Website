from django.db import models
from django.conf import settings


class Profile(models.Model):
    objects: None = True
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    data_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(default='default.png', upload_to='users/%Y/%m/%d', blank=True)

@property
def __str__(self):
    return f'Profile for user {self.user.Username}'
