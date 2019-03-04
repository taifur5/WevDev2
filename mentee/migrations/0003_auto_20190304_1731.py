# Generated by Django 2.1.5 on 2019-03-04 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentee', '0002_auto_20190304_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentee',
            name='interests',
        ),
        migrations.AddField(
            model_name='mentee',
            name='interests',
            field=models.ManyToManyField(related_name='interested_mentee', to='mentee.Subject'),
        ),
        migrations.RemoveField(
            model_name='mentor',
            name='interests',
        ),
        migrations.AddField(
            model_name='mentor',
            name='interests',
            field=models.ManyToManyField(related_name='interested_mentor', to='mentee.Subject'),
        ),
    ]