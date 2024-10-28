from django.db import models
from django.contrib.auth import get_user_model


class Message(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="message_sender")
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)
    
class Answer(models.Model):
    sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="answer_sender")
    receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)