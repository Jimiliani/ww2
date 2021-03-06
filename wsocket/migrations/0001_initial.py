# Generated by Django 3.1.7 on 2021-02-26 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='GameCell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('cell_type', models.CharField(choices=[('0', 'Вода'), ('1', 'Остров'), ('-1', 'Уничтожено')], default='0', max_length=2)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cells', to='wsocket.gamefield')),
            ],
        ),
        migrations.CreateModel(
            name='FakeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('channel_name', models.CharField(max_length=50)),
                ('country', models.CharField(choices=[('USA', 'Тупые пендосы'), ('Japan', 'Аниме')], max_length=5)),
                ('game_field', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='wsocket.gamefield')),
                ('room', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enemy', to='wsocket.fakeuser')),
            ],
        ),
    ]
