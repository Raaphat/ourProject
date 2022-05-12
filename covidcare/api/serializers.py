from django.dispatch import receiver
from rest_framework import serializers
from covido.models import Profile, Doctor, Patient, Review, Message, Symptom, Prescription, ChestDetails

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SymptomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symptom
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class ChestDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChestDetails
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    # reviews is a child table
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = '__all__'
    
    # obj is the object that we are gonna be serializing which is this doctor.
    def get_reviews(self, obj):
        # All of doctor's profile reviews
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        # return a query set of serialized reviews 
        return serializer.data

class PatientSerializer(serializers.ModelSerializer):

    patientDoctor = DoctorSerializer(many=False)

    prescription = serializers.SerializerMethodField()
    symptoms = serializers.SerializerMethodField()
    chestStatus = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = '__all__'

    def get_prescription(self, obj):
        prescription = obj.prescription_set.all()
        serializer = PrescriptionSerializer(prescription, many=True)
        return serializer.data
    
    def get_symptoms(self, obj):
        symptoms = obj.symptom_set.all()
        serializer = SymptomSerializer(symptoms, many=True)
        return serializer.data

    def get_chestStatus(self, obj):
        chestStatus = obj.chestdetails_set.all()
        serializer = ChestDetailsSerializer(chestStatus, many=True)
        return serializer.data

class MessageSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer(many=False)
    receiver = ProfileSerializer(many=False)

    class Meta:
        model = Message
        fields = '__all__'
