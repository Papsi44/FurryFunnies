# Generated by Django 5.1.2 on 2024-10-29 00:17

import django.core.validators
import furryFunnies.authors.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_rename_password_author_passcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(max_length=40, validators=[django.core.validators.MinLengthValidator(4), furryFunnies.authors.validators.LettersOnlyValidator()]),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2), furryFunnies.authors.validators.LettersOnlyValidator()]),
        ),
        migrations.AlterField(
            model_name='author',
            name='passcode',
            field=models.CharField(help_text='Your passcode must be a combination of 6 digits', validators=[furryFunnies.authors.validators.LengthPassValidator()]),
        ),
    ]
