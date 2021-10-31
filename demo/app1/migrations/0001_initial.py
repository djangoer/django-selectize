# Generated by Django 3.2.8 on 2021-10-30 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('ratings', models.IntegerField(choices=[(0, 'Bad'), (1, 'Average'), (2, 'Good'), (3, 'Outstanding')], default=1)),
                ('publications', models.ManyToManyField(to='app1.Publication')),
            ],
        ),
    ]
