# Generated for the starter project.
import uuid
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Complaint",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ticket_id", models.CharField(editable=False, max_length=12, unique=True)),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(blank=True, max_length=20)),
                ("category", models.CharField(choices=[("Garbage overflow","Garbage overflow"),("Missed collection","Missed collection"),("Illegal dumping","Illegal dumping"),("Street litter","Street litter"),("Blocked drain","Blocked drain"),("Other","Other")], max_length=40)),
                ("address", models.CharField(max_length=240)),
                ("area", models.CharField(blank=True, max_length=120)),
                ("description", models.TextField()),
                ("photo", models.ImageField(blank=True, null=True, upload_to="complaints/")),
                ("status", models.CharField(choices=[("Pending","Pending"),("In Progress","In Progress"),("Resolved","Resolved")], default="Pending", max_length=20)),
                ("admin_note", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
