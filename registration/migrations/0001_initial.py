# Generated by Django 4.0.2 on 2022-02-28 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagementModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Student', 'Student'), ('Teacher', 'Teacher')], max_length=10)),
            ],
        ),
    ]
