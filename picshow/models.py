from django.db import models
import uuid

class Picture(models.Model):
    COLOR_CHOICES = [
        ('red', 'Elv: 0-1500 mm'),
        ('blue', 'Elv: 1500-3000 mm'),
        ('yellow', 'Elv: 3000-4500 mm'),
        ('brown', 'Elv: 4500-6000 mm'),
        ('green', 'Elv: 6000-7500 mm'),
        ('orange', 'Elv: 7500-9000 mm'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)    
    Img_name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='pictures/')
    shape = models.CharField(max_length=50)
    x_cor = models.CharField(max_length=50)
    y_cor = models.CharField(max_length=50)
    z_cor = models.CharField(max_length=50)
    Prefillcolor = models.CharField(
        max_length=50,
        choices=COLOR_CHOICES,
        default='red'  
    )
    Date = models.DateField()

    def __str__(self):
        return f"Image: {self.Img_name} at {self.Date}"



