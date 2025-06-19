from django.db import models
from django.core.validators import MinValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Adjust, SmartResize,ResizeToFit

# Create your models here.
class HairCut(models.Model):
    name = models.CharField("Name",max_length=255)
    small_description = models.CharField("Small description",max_length=100)
    price = models.FloatField(default=0,validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Corte de cabello"
        verbose_name_plural = "Cortes de cabellos"

    def __str__(self):
        return self.name

class Gallery(models.Model):
    name = models.CharField("Name",max_length=255)
    image = ProcessedImageField(upload_to='gallery',
                                           format='WEBP',
                                           options={'quality': 85})

    class Meta:
        verbose_name = "Gallería"
        verbose_name_plural = "Gallería"

    def __str__(self):
        return self.name

    
