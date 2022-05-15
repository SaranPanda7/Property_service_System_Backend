from ast import Return
from email import message
import json
from multiprocessing import context
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .twilio_client import verifications, verification_checks
from .utils import *


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

        if service_type == "other_services":

            serializer = AddOtherServicesSerializer(data=json_data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            context = {"error": serializer.errors}
            return Response(context, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':

        property_tracing = GetAllPropertyTracingSerializer(
            PropertyTracing.objects.all(), many=True)

        maintainance_lease = GetAllMaintainanceAndLeaseSerializer(
            MaintainanceAndLease.objects.all(), many=True)

        legal_issues = GetAllLegalIssuesSerializer(
            LegalIssues.objects.all(), many=True)

        property_monitoring = GetAllPropertyMonitoringSerializer(
            PropertyMonitoring.objects.all(), many=True)

        investment_advice = GetAllInvestmentAdviceSerializer(
            InvestmentAdvice.objects.all(), many=True)

        other_services = GetAllOtherServicesSerializer(
            OtherServices.objects.all(), many=True)

        context = {'message': "showing data from services",
                   'all_service_requests': property_tracing.data + maintainance_lease.data + legal_issues.data + property_monitoring.data + investment_advice.data + other_services.data
                   }
        return Response(context, status=status.HTTP_202_ACCEPTED)


@api_view(['GET', 'POST'])
def assign_agent_for_service_request(request):

    if request.method == 'POST':
        data = request.data
        print(data)

        try:
            user = Users.objects.get(id=data["id"])
            token = data["token"] == "true"
            user_role = data["role"] == "admin"

        except Users.DoesNotExist:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if user and token and user_role:

            json_data = request.data

            service_type = json_data['service_name']
            service_id = json_data['service_id']
            print(service_type)
            print(service_id)

            if service_type == "propertyTracing":
                print("its property tracing service")

                service_request = PropertyTracing.objects.get(
                    service_id=json_data['service_id'])
                print(service_request)

                service_request.agent_id = json_data['agent_id']
                service_request.save()

                context = {"request updated"}

                return Response(context, status=status.HTTP_201_CREATED)

            if service_type == "maintainanceAndLease":
                print("its maintainance and lease service")

                service_request = MaintainanceAndLease.objects.get(
                    service_id=json_data['service_id'])
                print(service_request)

                service_request.agent_id = json_data['agent_id']
                service_request.save()

                context = {"request updated"}

                return Response(context, status=status.HTTP_201_CREATED)

            if service_type == "legalIssues":
                print("its legal issues service")

                service_request = LegalIssues.objects.get(
                    service_id=json_data['service_id'])
                print(service_request)

                service_request.agent_id = json_data['agent_id']
                service_request.save()

                context = {"request updated"}

                return Response(context, status=status.HTTP_201_CREATED)

            if service_type == "propertyMonitoring":
                print("its property monitoring service")

                service_request = PropertyMonitoring.objects.get(
                    service_id=json_data['service_id'])
                print(service_request)

                service_request.agent_id = json_data['agent_id']
                service_request.save()

                context = {"request updated"}

                return Response(context, status=status.HTTP_201_CREATED)

            if service_type == "investmentAdvice":
                print("its investment advice service")

                service_request = InvestmentAdvice.objects.get(
                    service_id=json_data['service_id'])
                print(service_request)

                service_request.agent_id = json_data['agent_id']
                service_request.save()

                context = {"request updated"}

                return Response(context, status=status.HTTP_201_CREATED)

            if service_type == "otherServices":
                print("its other service")

                service_request = OtherServices.objects.get(
                    service_id=json_data['service_id'])
                print(service_request)

                service_request.agent_id = json_data['agent_id']
                service_request.save()

                context = {"request updated"}

                return Response(context, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def fetch_service_requests_by_user_id(request):

    if request.method == 'POST':
        data = request.data

        try:
            user = Users.objects.get(phone_number=data["phone_number"])
            token = data["token"] == "true"
            uid = data['id']
        except Users.DoesNotExist:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if user and token:

            property_tracing = GetAllPropertyTracingSerializer(
                PropertyTracing.objects.filter(user_id=uid), many=True)

            maintainance_lease = GetAllMaintainanceAndLeaseSerializer(
                MaintainanceAndLease.objects.filter(user_id=uid), many=True)

            legal_issues = GetAllLegalIssuesSerializer(
                LegalIssues.objects.filter(user_id=uid), many=True)

            property_monitoring = GetAllPropertyMonitoringSerializer(
                PropertyMonitoring.objects.filter(user_id=uid), many=True)

            investment_advice = GetAllInvestmentAdviceSerializer(
                InvestmentAdvice.objects.filter(user_id=uid), many=True)

            other_services = GetAllOtherServicesSerializer(
                OtherServices.objects.filter(user_id=uid), many=True)

            context = {"data": property_tracing.data + maintainance_lease.data + legal_issues.data + property_monitoring.data + investment_advice.data + other_services.data
                       }

            return Response(context)
        else:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def fetch_service_requests_for_admin(request):

    if request.method == 'POST':
        data = request.data

        try:
            user = Users.objects.get(phone_number=data["phone_number"])
            token = data["token"] == "true"
            role = data["role"] == "admin"
        except Users.DoesNotExist:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if user and token and role:

            property_tracing = GetAllPropertyTracingSerializer(
                PropertyTracing.objects.all(), many=True)

            maintainance_lease = GetAllMaintainanceAndLeaseSerializer(
                MaintainanceAndLease.objects.all(), many=True)

            legal_issues = GetAllLegalIssuesSerializer(
                LegalIssues.objects.all(), many=True)

            property_monitoring = GetAllPropertyMonitoringSerializer(
                PropertyMonitoring.objects.all(), many=True)

            investment_advice = GetAllInvestmentAdviceSerializer(
                InvestmentAdvice.objects.all(), many=True)

            other_services = GetAllOtherServicesSerializer(
                OtherServices.objects.all(), many=True)

            context = {"data": property_tracing.data + maintainance_lease.data + legal_issues.data + property_monitoring.data + investment_advice.data + other_services.data
                       }

            return Response(context)
        else:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def fetch_all_users(request):

    if request.method == 'POST':
        data = request.data
        print(data)

        try:
            user = Users.objects.get(id=data["id"])
            token = data["token"] == "true"
            user_role = data["role"] == "admin"
            role_data = Roles.objects.get(role="agent")

        except Users.DoesNotExist:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if user and token and user_role:

            users_data = UserSerializer(
                Users.objects.filter(role_id=role_data.id), many=True)

            context = {"data": users_data.data}

            return Response(context)

        else:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def create_user(request):

    if request.method == 'POST':
        data = request.data
        print(data)

        try:
            user = Users.objects.get(id=data["id"])
            token = data["token"] == "true"
            user_role = data["user_role"] == "admin"
            role_data = Roles.objects.only('id').get(role="agent")

        except Users.DoesNotExist:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)

        if user and token and user_role:

            user_data = Users.objects.create(
                phone_number=data["phone_number"], full_name=data["full_name"], email=data["email"], address=data["address"], role=role_data)

            context = {"user created"}

            return Response(context, status=status.HTTP_201_CREATED)

        else:
            context = {"message": "Unauthorized Acess"}
            return Response(context, status=status.HTTP_401_UNAUTHORIZED)
