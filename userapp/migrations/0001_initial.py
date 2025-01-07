# Generated by Django 5.1.4 on 2025-01-06 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "full_name",
                    models.CharField(max_length=100, verbose_name="User Name"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("password", models.CharField(max_length=128, verbose_name="Password")),
                (
                    "phone_number",
                    models.CharField(max_length=15, verbose_name="Phone Number"),
                ),
                ("age", models.CharField(max_length=15, verbose_name="age")),
                ("address", models.TextField(verbose_name="Address")),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profiles/",
                        verbose_name="Upload Profile",
                    ),
                ),
                (
                    "otp",
                    models.CharField(
                        default="000000",
                        help_text="Enter OTP for verification",
                        max_length=6,
                    ),
                ),
                (
                    "otp_status",
                    models.CharField(
                        default="Not Verified", help_text="OTP status", max_length=15
                    ),
                ),
                ("status", models.CharField(default="Pending", max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="UserFeedback",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.IntegerField()),
                ("additional_comments", models.TextField()),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userapp.user"
                    ),
                ),
            ],
            options={
                "db_table": "user_feedback",
            },
        ),
    ]