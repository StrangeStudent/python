# Generated by Django 3.2.6 on 2021-08-06 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone number')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone', to='phonebook.person')),
            ],
        ),
    ]
