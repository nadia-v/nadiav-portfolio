# Generated by Django 3.0.3 on 2020-05-25 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpage.Project')),
            ],
        ),
    ]
