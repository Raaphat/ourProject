# Generated by Django 4.0.4 on 2022-05-06 19:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Giza', 'Giza'), ('Shubra', 'Shubra El Kheima'), ('Port_Said', 'Port Said'), ('Suez', 'Suez'), ('Mahalla', 'Mahalla (Gharbia)'), ('Luxor', 'Luxor'), ('Mansoura', 'Mansoura (Dakahlia)'), ('Tanta', 'Tanta (Gharbia)'), ('Asyut', 'Asyut'), ('Ismailia', 'Ismailia'), ('Faiyum', 'Faiyum'), ('Zagazig', 'Zagazig (Sharqia)'), ('Damietta', 'Damietta'), ('Aswan', 'Aswan'), ('Minya', 'Minya'), ('Damanhur', 'Damanhur (Beheira)'), ('Beni_Suef', 'Beni Suef'), ('Hurghada', 'Hurghada (Red Sea)'), ('Qena', 'Qena'), ('Sohag', 'Sohag'), ('Shibin', 'Shibin El Kom (Monufia)'), ('Banha', 'Banha (Qalyubia)'), ('Arish', 'Arish (North Sinai)')], max_length=200, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='covido.profile')),
                ('short_intro', models.CharField(blank=True, max_length=200, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='images/doctors/doctor-default.jpg', null=True, upload_to='doctors/')),
                ('identification', models.ImageField(blank=True, null=True, upload_to='images/doctors/')),
                ('social_website', models.CharField(blank=True, max_length=200, null=True)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['created'],
            },
            bases=('covido.profile',),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('profile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='covido.profile')),
                ('profile_image', models.ImageField(blank=True, default='images/patients/patient-default.png', null=True, upload_to='doctors/')),
                ('patient_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('patientDoctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_patient_set', to='covido.doctor')),
            ],
            bases=('covido.profile',),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=200, null=True)),
                ('subject', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField()),
                ('is_read', models.BooleanField(default=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to='covido.profile')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sender', to='covido.profile')),
            ],
            options={
                'ordering': ['is_read', '-created'],
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('fever', models.BooleanField(default=False)),
                ('cough', models.BooleanField(default=False)),
                ('tired', models.BooleanField(default=False)),
                ('taste', models.BooleanField(default=False)),
                ('smell', models.BooleanField(default=False)),
                ('difficulty_breathing', models.BooleanField(default=False)),
                ('chest_pain', models.BooleanField(default=False)),
                ('speech_loss', models.BooleanField(default=False)),
                ('diarrhoea', models.BooleanField(default=False)),
                ('aches', models.BooleanField(default=False)),
                ('headache', models.BooleanField(default=False)),
                ('sore_throat', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covido.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('medication_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dose', models.CharField(blank=True, max_length=200, null=True)),
                ('times_per_day', models.IntegerField(blank=True, null=True)),
                ('additional_tips', models.TextField()),
                ('dosage_time', models.TimeField()),
                ('dosage_date', models.DateField()),
                ('first_dose_date', models.DateField()),
                ('last_dose_date', models.DateField()),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covido.patient')),
            ],
        ),
        migrations.CreateModel(
            name='ChestDetails',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative')], max_length=10)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='covido.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('body', models.TextField(blank=True, null=True)),
                ('value', models.CharField(choices=[('up', 'Up Vote'), ('down', 'Down Vote')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='covido.doctor')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='covido.patient')),
            ],
            options={
                'unique_together': {('owner', 'doctor')},
            },
        ),
    ]