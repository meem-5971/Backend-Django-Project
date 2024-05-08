# Generated by Django 5.0.4 on 2024-05-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('completion', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('category', models.ManyToManyField(to='category.category')),
            ],
        ),
    ]
