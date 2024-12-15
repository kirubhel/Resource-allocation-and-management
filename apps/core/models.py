
from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    row_status = models.BooleanField(default=True)

    class Meta:
        abstract = True
