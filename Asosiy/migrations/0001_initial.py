# Generated by Django 4.2.1 on 2023-05-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sarlavha', models.CharField(max_length=100)),
                ('batafsil', models.CharField(max_length=100)),
                ('holat', models.CharField(choices=[('bajaridi', 'bajarildi'), ('bajarilmadi', 'bajarilmadi')], max_length=100)),
                ('vaqt', models.DateField()),
            ],
        ),
    ]
