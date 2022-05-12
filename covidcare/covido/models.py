from django.db import models
import uuid
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Profile(models.Model):
    EGYPT_CITIES = (
        ('Cairo', 'Cairo'),
        ('Alexandria', 'Alexandria'),
        ('Giza', 'Giza'),
        ('Shubra', 'Shubra El Kheima'),
        ('Port_Said', 'Port Said'),
        ('Suez', 'Suez'),
        ('Mahalla', 'Mahalla (Gharbia)'),
        ('Luxor', 'Luxor'),
        ('Mansoura', 'Mansoura (Dakahlia)'),
        ('Tanta', 'Tanta (Gharbia)'),
        ('Asyut', 'Asyut'),
        ('Ismailia', 'Ismailia'),
        ('Faiyum', 'Faiyum'),
        ('Zagazig', 'Zagazig (Sharqia)'),
        ('Damietta', 'Damietta'),
        ('Aswan', 'Aswan'),
        ('Minya', 'Minya'),
        ('Damanhur', 'Damanhur (Beheira)'),
        ('Beni_Suef', 'Beni Suef'),
        ('Hurghada', 'Hurghada (Red Sea)'),
        ('Qena', 'Qena'),
        ('Sohag', 'Sohag'),
        ('Shibin', 'Shibin El Kom (Monufia)'),
        ('Banha', 'Banha (Qalyubia)'),
        ('Arish', 'Arish (North Sinai)'),
    )
    # if a user is deleted, their associated profile will be deleted, too.
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True, choices=EGYPT_CITIES)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, null=True, blank=True, unique=True) # Validators should be a list
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

# TO-DO: Make a try-catch block on the doctor's profile_image #

class Doctor(Profile):
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='static/images/doctors/profiles', default='resources/images/doctor-default.jpg')
    identification = models.ImageField(null=True, blank=True, upload_to='static/images/doctors/identification')
    social_website = models.CharField(max_length=200, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    doctor_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['created']

class Patient(Profile):
    patientDoctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctor_patient_set')
    profile_image = models.ImageField(null=True, blank=True, upload_to='static/images/patients/', default='resources/images/patient-default.png')
    patient_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)

    def __str__(self):
        return str(self.name)

# TO-Do: calculate total reviewers and the ratio between upvotes and downvotes #

class Review(models.Model):
    # The first element in each tuple is the actual value to be set on the model,
    # and the second one is the human-readable name.
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    owner = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) 
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    
    class Meta:
        # a user can leave only one review to each doctor
        # so we can never have more than one review with the same patient on the same doctor's profile in the database
        unique_together = [['owner', 'doctor']]

    def __str__(self):
        return self.value

class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="receiver")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    # Note:'blank' attribute default's value is False
    body = models.TextField()
    # if the message has been sent, it is obviously has not been read
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    message_id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    
    def __str__(self):
        return self.subject
    
    # when the user opens his inpox, he should see the unread messages first
    # if there are not unread messages, the newer created messages will be at the top
    class Meta:
        ordering = ['is_read', '-created']

class Symptom(models.Model):
    
    owner = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    tired = models.BooleanField(default=False)
    taste = models.BooleanField(default=False)
    smell = models.BooleanField(default=False)
    difficulty_breathing = models.BooleanField(default=False)
    chest_pain = models.BooleanField(default=False)
    speech_loss = models.BooleanField(default=False)
    diarrhoea = models.BooleanField(default=False)
    aches = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    sore_throat = models.BooleanField(default=False)

    def __str__(self):
        return str(self.owner)

class Prescription(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=True)
    owner = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    medication_name = models.CharField(max_length=200, blank=True, null=True)
    dose = models.CharField(max_length=200, blank=True, null=True)
    times_per_day = models.IntegerField(blank=True, null=True)
    additional_tips = models.TextField()
    dosage_time = models.TimeField()
    dosage_date = models.DateField()
    first_dose_date = models.DateField()
    last_dose_date = models.DateField()

    def __str__(self):
        return str(self.medication_name)


class ChestDetails(models.Model):
    COVID_RESULT = (
        ('positive', 'Positive'),
        ('negative', 'Negative'),
    )
    owner = models.ForeignKey(
        Patient, on_delete=models.CASCADE, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                         primary_key=True, editable=True)
    status = models.CharField(max_length=10, choices=COVID_RESULT) # boolean
    release_date = models.DateTimeField(auto_now_add=True)
    
    # TO-DO
    # live_location = models.CharField(max_length=200, blank=True, null=True) #

    def __str__(self):
        return str(self.status)