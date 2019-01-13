# Generated by Django 2.1.5 on 2019-01-13 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Name')),
                ('category', models.CharField(blank=True, choices=[('programming_language', 'Programming Language'), ('database', 'Database'), ('cloud_technology', 'Cloud Technology'), ('testing_tool', 'Testing Tool'), ('frameworks', 'Frameworks'), ('other', 'Other')], db_index=True, max_length=32, null=True, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Skills',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserSkillModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UserSkills',
                'ordering': ['skill'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='skills',
            field=models.ManyToManyField(through='users.UserSkillModel', to='users.Skill'),
        ),
        migrations.AlterUniqueTogether(
            name='userskillmodel',
            unique_together={('user', 'skill')},
        ),
    ]
