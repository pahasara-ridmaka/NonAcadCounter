from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default='')
    username = models.CharField( max_length=30)
    comment = models.TextField()
    commented_at = models.DateTimeField(  auto_now_add=True)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)

    def __str__(self) -> str:
        if len(self.comment) > 10:
            return self.comment[:10]
        else: 
            return self.comment
