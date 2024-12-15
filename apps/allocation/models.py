from django.db import models
from core.models import BaseModel
from inventory.models import Item

class Region(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Zone(BaseModel):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='zones')

    def __str__(self):
        return f"{self.name} - {self.region.name}"

class Woreda(BaseModel):
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='woredas')

    def __str__(self):
        return f"{self.name} - {self.zone.name}"

class KifleKetema(BaseModel):
    name = models.CharField(max_length=255)
    woreda = models.ForeignKey(Woreda, on_delete=models.CASCADE, related_name='kifle_ketemas')

    def __str__(self):
        return f"{self.name} - {self.woreda.name}"

class Allocation(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='allocations')
    quantity = models.PositiveIntegerField()
    allocated_to = models.ForeignKey(
        Woreda, on_delete=models.CASCADE, null=True, blank=True, related_name='allocations'
    )
    kifle_ketema = models.ForeignKey(
        KifleKetema, on_delete=models.CASCADE, null=True, blank=True, related_name='allocations'
    )
    allocated_date = models.DateField()

    def __str__(self):
        return f"{self.quantity} {self.item.name} allocated"
