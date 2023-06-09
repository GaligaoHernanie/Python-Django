
from django.db import models
from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
        
class info(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthdate = models.DateField(verbose_name="Birthdate")
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
        
    def __str__(self):
        return f"{self.first_name} {self.middle_name}.  {self.last_name}"

