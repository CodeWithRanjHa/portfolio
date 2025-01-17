# Generated by Django 5.0.6 on 2024-08-23 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_projectimage_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pictures',
        ),
        migrations.AddField(
            model_name='project',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.DeleteModel(
            name='ProjectImage',
        ),
    ]
