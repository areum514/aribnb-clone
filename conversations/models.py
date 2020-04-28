from django.db import models
from core import models as core_models

# Create your models here.
class Conversation(core_models.TimeStampedMode):
    """Conversation modle definition"""

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_message(self):
        return self.messages.count()

    count_message.short_description = "Number of messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedMode):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    converstation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says:{self.message}"
