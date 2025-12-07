import uuid
from django.db import models
from django.contrib.auth.models import User

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
       ("approve", "Approve"),
        ("pending", "Pending"),
        ("reject", "Reject"),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employees")
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.CharField(max_length=300)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reason

