from pyexpat import model
import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError
from .models import Roles, Users
from .twilio_client import verifications, verification_checks
from graphql import GraphQLError



class RoleType(DjangoObjectType):
    class Meta:
        model = Roles
        fields = "__all__"


class UserType(DjangoObjectType):

    role = graphene.Field(RoleType)

    class Meta:
        model = Users
        fields = '__all__'

    def resolve_role(self, info):
        return self.role


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())
    user_login = graphene.Field(UserType, phone_number=graphene.String())
    verify_user = graphene.Field(UserType, phone_number=graphene.String(), token=graphene.String())


    def resolve_all_users(root, info, **kwargs):
        return Users.objects.all()


    def resolve_user(root, info, id):
        try:
            return Users.objects.get(pk=id)
        except Users.DoesNotExist:
            return None

    def resolve_user_login(root, info, phone_number):
        user = Users.objects.get(phone_number=phone_number)
        if user:
            verifications(phone_number)
            raise GraphQLError("OTP Sent to mobile number.")            
        else:
            raise GraphQLError("User Doesn't Exist.")


    def resolve_verify_user(root, info, phone_number, token):

        verification = verification_checks(phone_number, token)

        if verification.status == 'approved':
            print("OTP Verified Successfully.")
            return (Users.objects.get(phone_number=phone_number))
        else:
            raise GraphQLError("Invalid OTP.")


class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    phone_number = graphene.String()
    full_name = graphene.String()
    email = graphene.String()
    role = graphene.String()
    otp = graphene.String()
    address = graphene.String()



class Register(graphene.Mutation):
    class Arguments:
        user_data = UserInput()
    
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data):
        if not Users.objects.filter(phone_number=user_data.phone_number).exists():

            send_otp = verifications(user_data.phone_number)

            if send_otp:
                raise GraphQLError("OTP Send to mobile number.")
            else:
                raise GraphQLError("Enter correct mobile number.")
                       
        else:
            raise GraphQLError("User allready Regiseted Go to Login.") 


            
class VerifyRegister(graphene.Mutation):
    class Arguments:
        user_data = UserInput()
    
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data):
        if not Users.objects.filter(phone_number=user_data.phone_number).exists():

            verification = verification_checks(user_data.phone_number, user_data.otp)

            if verification.status == 'approved':
                print("OTP Verified Successfully.")
                
                user = Users.objects.create( 
                    phone_number=user_data.phone_number,
                )
                return Register(user=user)
                
            else:
                print("Incorrect OTP.")
                raise GraphQLError("incorrect OTP")
                       
        else:
            raise GraphQLError("User allready Regiseted.") 


class ContinueRegistration(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required = True)
    
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data=None):
        user_instance = Users.objects.get(phone_number=user_data.phone_number)

        if user_instance:
            user_instance.phone_number = user_data.phone_number
            user_instance.full_name = user_data.full_name
            user_instance.email = user_data.email
            user_instance.save()

            return ContinueRegistration(user=user_instance)            
        return ContinueRegistration(user=None)



class UserRegistration(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required = True)
    
    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data=None):
        user_instance = Users( 
            phone_number=user_data.phone_number,
            full_name=user_data.full_name,
            email=user_data.email,
        )
        user_instance.save()
        return UserRegistration(user=user_instance)


class UpdateUser(graphene.Mutation):
    class Arguments:
        user_data = UserInput(required=True)

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, user_data=None):

        user_instance = Users.objects.get(pk=user_data.id)

        if user_instance:
            user_instance.phone_number = user_data.phone_number
            user_instance.full_name = user_data.full_name
            user_instance.email = user_data.email
            user_instance.save()

            return UpdateUser(user=user_instance)            
        return UpdateUser(user=None)
        


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.Field(UserType)

    @staticmethod
    def mutate(root, info, id):
        user_instance = Users.objects.get(pk=id)
        user_instance.delete()

        return GraphQLError("User Deleted")



class Mutation(graphene.ObjectType):
    user_registration = UserRegistration.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    register = Register.Field()
    verifyRegister = VerifyRegister.Field()
    continueRegistration = ContinueRegistration.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)