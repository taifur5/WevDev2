# Generated by Django 2.1.5 on 2019-05-08 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0002_auto_20190505_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='mentee',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='interests',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
