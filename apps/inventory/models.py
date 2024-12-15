from django.db import models
from core.models import BaseModel

class CategoryType(models.TextChoices):
    RAW_MATERIAL = 'RAW_MATERIAL', 'Raw Material'
    ASSET = 'ASSET', 'Asset'
    OTHER = 'OTHER', 'Other'

class MeasurementType(models.TextChoices):
    LENGTH = 'LENGTH', 'Length'
    MASS = 'MASS', 'Mass'
    VOLUME = 'VOLUME', 'Volume'
    PIECE = 'PIECE', 'Piece'

class Category(BaseModel):
    name = models.CharField(max_length=255)
    category_type = models.CharField(max_length=50, choices=CategoryType.choices)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Item(BaseModel):
    item_code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    measurement_type = models.CharField(max_length=50, choices=MeasurementType.choices)
    is_expirable = models.BooleanField(default=False)
    reorder_point = models.PositiveIntegerField()
    remark = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

