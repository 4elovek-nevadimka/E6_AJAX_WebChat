from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to='user_avatars/', default='user_avatars/default.png', blank=True)

    def __str__(self):
        return f'{self.user.username}'


class Message(models.Model):
    sender = models.ForeignKey(
        UserProfile, related_name='messages', on_delete=models.CASCADE)
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.user.username


class Room(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=128, blank=True)
    participants = models.ManyToManyField(
        UserProfile, related_name='rooms', blank=True)
    messages = models.ManyToManyField(Message, blank=True)

    def save(self, *args, **kwargs):
        # if not self.id:
        #     self.title = f"Room #{Room.objects.count() + 1}"
        super(Room, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return f'/chat/{self.id}'

    def __str__(self):
        return self.title
