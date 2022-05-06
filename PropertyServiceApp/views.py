from email import message
import json
from multiprocessing import context
from rest_framework.parsers import JSONParser
from .models import Roles, User, Users, PropertyTracing
from .serializers import UserSerializer, GetAllPropertyTracingSerializer, AddPropertyTracingSerializer, AddMaintainanceAndLeaseSerializer, AddLegalIssuesSerializer, AddPropertyMonitoringSerializer, AddInvestmentAdviceSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .twilio_client import verifications, verification_checks
from .utils import propertyTracingDataProcessor


@api_view(['GET', 'POST'])
def all_users(request):
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def registration(request):
    print(request.data)
    if request.method == "POST":
        data = request.data
        phone_number = data["phone_number"]

        if not Users.objects.filter(phone_number=data["phone_number"]).exists():

            send_otp = verifications(phone_number)

            if send_otp:
                context = {"message": "OTP SENT TO MOBILE NUMBER..."}
                return Response(context)
            else:
                context = {"message": "Enter correct mobile number."}
                return Response(context)

        else:
            context = {"message": "User Allready Exist Go To Login..."}
            return Response(context)


@api_view(['POST'])
def verify_registration(request):
    print(request.data)
    if request.method == "POST":
        data = request.data
        phone_number = data["phone_number"]
        otp = data["otp"]
        full_name = data["full_name"]
        email = data["email"]
        address = data["address"]

        if not Users.objects.filter(phone_number=data["phone_number"]).exists():

            verification = verification_checks(phone_number, otp)

            if verification.status == 'approved':
                print("OTP Verified Successfully.")
                user = Users.objects.create(
                    phone_number=phone_number, full_name=full_name, email=email, address=address)
                context = {"message": "User Registered Successfully..."}
                return Response(context)

            else:
                print("Incorrect OTP.")
                context = {"message": "Incorrect OTP"}
                return Response(context)

        else:
            context = {"message": "User Allready Exist Go To Login..."}
            return Response(context)


@api_view(['GET', 'PUT', 'DELETE'])
def update_user(request):

    try:
        user = Users.objects.all()
    except Users.DoesNotExist:
        return Response("No Users Found...")

    if request.method == 'GET':
        serializer = UserSerializer(user, many=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method == 'PUT':
        data = request.data
        get_user = Users.objects.get(phone_number=data["phone_number"])
        serializer = UserSerializer(get_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        get_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def login(request):
    print(request.data)
    if request.method == 'POST':
        data = request.data

        try:
            user = Users.objects.get(phone_number=data["phone_number"])
        except Users.DoesNotExist:
            context = {"message": "User Doesn't Exist, Go to Registeration..."}
            return Response(context)

        if user:
            send_otp = verifications(data["phone_number"])
            if send_otp:
                print("OTP send to mobile number...")
                context = {
                    "message": "OTP SENT TO REGISTERED MOBILE NUMBER..."}
                return Response(context)
        else:
            context = {"message": "User Doesn't Exist, Go to Registeration..."}
            return Response(context)
    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def verify_login(request):

    if request.method == 'POST':
        data = request.data
        try:
            user = Users.objects.get(phone_number=data["phone_number"])
            print('Your user id is : ', user.id)
        except Users.DoesNotExist:
            context = {"message": "User Doesn't Exist Go to Registeration..."}
            return Response(context)
        if user:
            verification = verification_checks(
                data["phone_number"], data["otp"])

            if verification.status == 'approved':
                print("OTP Verified Successfully.")
                serializer = UserSerializer(user)
                context = {"message": "User Login Success...",
                           "data": serializer.data}
                return Response(context)
            else:
                context = {"message": "Invalid OTP."}
                return Response(context)
        else:
            context = {"message": "User Not Exist Go to Registeration..."}
            return Response(context)

    else:
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def dashboard(request):
    if request.method == 'POST':
        data = request.data

        try:
            user = Users.objects.get(phone_number=data["phone_number"])
            token = data["token"] == "true"
        except Users.DoesNotExist:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if user and token:
            serializer = UserSerializer(user)
            context = {"message": "User found", "data": serializer.data}
            return Response(context)
        else:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET', 'POST'])
def create_service_request(request):

    if request.method == 'POST':

        json_data = request.data["data"]

        service_type = json_data['service']

        if service_type == "property_tracing":

            serializer = AddPropertyTracingSerializer(data=json_data)

        if service_type == "maintainance_and_lease":

            serializer = AddMaintainanceAndLeaseSerializer(data=json_data)

        if service_type == "legal_issues":

            serializer = AddLegalIssuesSerializer(data=json_data)

        if service_type == "property_monitoring":

            serializer = AddPropertyMonitoringSerializer(data=json_data)

        if service_type == "investment_advice":

            serializer = AddInvestmentAdviceSerializer(data=json_data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            context = {"error": serializer.errors}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':

        property_tracing_requests = PropertyTracing.objects.all()

        serializer = GetAllPropertyTracingSerializer(
            property_tracing_requests, many=True)
        context = {'message': "showing data from services",
                   'data': serializer.data}
        return Response(context, status=status.HTTP_202_ACCEPTED)
