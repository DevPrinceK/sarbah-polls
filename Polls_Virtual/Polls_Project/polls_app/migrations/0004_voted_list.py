# Generated by Django 3.2.7 on 2021-10-04 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls_app', '0003_alter_electorate_pass_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voted_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('std_id', models.CharField(max_length=8)),
                ('pass_key', models.CharField(max_length=100)),
            ],
        ),
    ]
