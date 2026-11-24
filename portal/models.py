import uuid
from django.conf import settings
from django.db import models

class Complaint(models.Model):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
    ]
    CATEGORY_CHOICES = [
        ("Garbage overflow", "Garbage overflow"),
        ("Missed collection", "Missed collection"),
        ("Illegal dumping", "Illegal dumping"),
        ("Street litter", "Street litter"),
        ("Blocked drain", "Blocked drain"),
        ("Other", "Other"),
    ]
    ticket_id = models.CharField(max_length=12, unique=True, editable=False)
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)
    address = models.CharField(max_length=240)
    area = models.CharField(max_length=120, blank=True)
    description = models.TextField()
    photo = models.ImageField(upload_to="complaints/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Pending")
    admin_note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = uuid.uuid4().hex[:10].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_id} — {self.category}"
