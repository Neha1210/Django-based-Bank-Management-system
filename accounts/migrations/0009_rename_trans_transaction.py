# Generated by Django 4.0 on 2022-03-17 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_trans_delete_transaction'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='trans',
            new_name='transaction',
        ),
    ]
