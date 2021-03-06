# Generated by Django 2.1.5 on 2019-01-13 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_staff', models.BooleanField(db_index=True, default=False, verbose_name='Is Staff')),
                ('is_superuser', models.BooleanField(db_index=True, default=False, verbose_name='Is Superuser')),
                ('full_name', models.CharField(blank=True, default='', max_length=256, verbose_name='Full Name')),
                ('ld_number', models.IntegerField(blank=True, null=True, verbose_name='L/D Number')),
                ('position', models.CharField(blank=True, max_length=68, null=True, verbose_name='Position')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('hired_date', models.DateField(blank=True, null=True, verbose_name='Hired Date')),
                ('end_of_contract', models.DateField(blank=True, null=True, verbose_name='End of Contract')),
                ('education', models.CharField(blank=True, max_length=32, null=True, verbose_name='Education')),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone Number')),
                ('phone_number2', models.CharField(blank=True, max_length=32, null=True, verbose_name='Phone Number 2')),
                ('has_card', models.BooleanField(default=False, verbose_name='Has Card')),
                ('has_key', models.BooleanField(default=False, verbose_name='Has Key')),
                ('skype', models.CharField(blank=True, max_length=32, null=True, verbose_name='Skype')),
                ('working_hours', models.IntegerField(default=8, verbose_name='Working Hours')),
                ('assessment_date', models.DateField(blank=True, null=True, verbose_name='Assessment Date')),
                ('assessment_plan', models.TextField(blank=True, null=True, verbose_name='Assessment Plan')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'ordering': ['-modified'],
            },
        ),
    ]
