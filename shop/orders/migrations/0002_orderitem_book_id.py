# Generated by Django 4.1.1 on 2022-09-17 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
