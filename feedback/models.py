
# feedback/models.py
from django.db import models
from django.core.exceptions import ValidationError

def validate_message_length(value):
    num_words = len(value.split())
    if num_words < 4:
        raise ValidationError("Not enough words!")

class Feedback(models.Model):
    TOPIC_CHOICES = [
        ('general', 'General'),
        ('bug', 'Bug Report'),
        ('feature', 'Feature Request'),
    ]

    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    message = models.TextField(validators=[validate_message_length])
    sender = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.topic