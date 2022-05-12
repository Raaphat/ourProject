from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# these are used when we want to make a restriction
# that means only an authenticated user can access something, or only the adminstrator can access some other things
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from covido.models import Doctor, Patient, Review, Message, Symptom, Prescription, ChestDetails
from .serializers import DoctorSerializer, PatientSerializer, ReviewSerializer, MessageSerializer, SymptomSerializer, PrescriptionSerializer, ChestDetailsSerializer

def getRoutes(request):
    routes = [
        {'GET': '/api/doctors'},
        {'GET': '/api/doctor/id'},
        {'GET': '/api/patients'},
        {'GET': '/api/patient/id'},
        {'GET': '/api/messages'},
    ]

    return JsonResponse(routes, safe=False)

# the user has to be logged in to get the available doctors
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getDoctors(request):
    print('USER:', request.user)
    doctors = Doctor.objects.all()
    # we need to serialize these items before we can return them
    serializer = DoctorSerializer(doctors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(doctor, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getPatients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPatient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getReviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

# I am gonna remove Profile table to avoid that error
@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSymptoms(request):
    symptoms = Symptom.objects.all()
    serializer = SymptomSerializer(symptoms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPrescriptions(request):
    prescriptions = Prescription.objects.all()
    serializer = PrescriptionSerializer(prescriptions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getChestDetails(request):
    chestObjects = ChestDetails.objects.all()
    serializer = ChestDetailsSerializer(chestObjects, many=True)
    return Response(serializer.data)

'''
@api_view(['POST'])
def addItem(request):
    # sending the data that was sent from the front end on that POST request to Serializer class to be serialized
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
'''