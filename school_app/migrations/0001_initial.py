# Generated by Django 4.2.6 on 2023-10-17 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=150)),
                ('cep', models.CharField(max_length=10)),
                ('estado', models.CharField(max_length=20)),
                ('regiao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolSubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Prefiro não dizer', 'Prefiro não dizer'), ('Outro', 'Outro')], max_length=100)),
                ('corouraca', models.CharField(choices=[('Amarelo', 'Amarelo'), ('Branco', 'Branco'), ('Indegena', 'Indegena'), ('Pardo', 'Pardo'), ('Preto', 'Preto')], max_length=100)),
                ('disciplina', models.ManyToManyField(related_name='teacher', to='school_app.schoolsubject')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.school')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.DateField()),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Prefiro não dizer', 'Prefiro não dizer'), ('Outro', 'Outro')], max_length=100)),
                ('corouraca', models.CharField(choices=[('Amarelo', 'Amarelo'), ('Branco', 'Branco'), ('Indegena', 'Indegena'), ('Pardo', 'Pardo'), ('Preto', 'Preto')], max_length=100)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.school')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.class')),
            ],
        ),
        migrations.AddField(
            model_name='schoolsubject',
            name='professor',
            field=models.ManyToManyField(related_name='subjects', to='school_app.teacher'),
        ),
        migrations.AddField(
            model_name='schoolsubject',
            name='student',
            field=models.ManyToManyField(related_name='subjects', to='school_app.student'),
        ),
        migrations.CreateModel(
            name='SchoolBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.school')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('licao', models.FileField(upload_to='licoes/')),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.class')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='professor',
            field=models.ManyToManyField(related_name='turma', to='school_app.teacher'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('1° Bimestre', '1° Bimestre'), ('2° Bimestre', '2° Bimestre'), ('3° Bimestre', '3° Bimestre'), ('4° Bimestre', '4° Bimestre')], max_length=200)),
                ('ano_letivo', models.DateField()),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_app.student')),
            ],
        ),
    ]
