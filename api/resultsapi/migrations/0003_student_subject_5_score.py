# Generated by Django 4.2.4 on 2023-12-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resultsapi", "0002_remove_student_password"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="subject_5_score",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
