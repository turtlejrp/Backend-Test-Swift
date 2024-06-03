# Generated by Django 5.0.6 on 2024-06-02 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='ชื่อโรงเรียน',
            new_name='abbreviation_name',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='ที่อยู่',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='ตัวย่อชื่อโรงเรียน',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom_year', models.IntegerField()),
                ('classroom_room', models.IntegerField()),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.school')),
            ],
        ),
    ]
