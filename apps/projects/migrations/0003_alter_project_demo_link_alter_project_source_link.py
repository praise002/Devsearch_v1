# Generated by Django 5.1 on 2024-08-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_feedback_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='source_link',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]