import urllib, json
import logging
# import googleToken as googleToken
from django.utils import dateparse
from rest_framework.response import Response
from rest_framework import status
from .models import AppUser, Token
from .serializers import UserLoginSerializer, UserRegisterSerializer

"""
Verifies a specified facebookID and Token derived from client side.
"""


def verify_facebook_token(facebookID, facebookToken):
    if facebookID == "" or facebookToken == "":
        return False
    try:
        url = ("https://graph.facebook.com/v2.2/me?access_token=%s" % facebookToken)

        response = urllib.urlopen(url)

        data = json.loads(response.read())

        if data["id"] == facebookID:
            return True
        else:
            return False
    except Exception as e:
        return False

    return False


def verify_google_token(googleId, googleToken):
    if googleId == "" or googleToken == "":
        return False
    try:
        # url = ("https://graph.facebook.com/v2.2/me?access_token=%s" % googleToken)
        url = ("https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s" % googleToken)

        response = urllib.urlopen(url)

        data = json.loads(response.read())

        if data["id"] == googleId:
            return True
        else:
            return False
    except Exception as e:
        return False

    return False


"""
Verifies a specified username and password and returns, if found, user object
"""


def verify_user_with_email_password(email, password):
    try:
        user = AppUser.objects.get(email=email, is_active=True)
    except AppUser.DoesNotExist:
        return False

    if user.check_password(password):
        return user


"""
Checks the system for the user with the specified facebook id
"""


def get_user_with_facebook_id(facebook_id):
    try:
        return AppUser.objects.get(facebook_id=facebook_id, is_active=True)
    except Exception as e:
        return False

"""
Checks the system for the user with the specified google id
"""

def get_user_with_google_id(google_id):
    try:
        return AppUser.objects.get(google_id=google_id, is_active=True)
    except Exception as e:
        return False


"""
Check the user with the data
"""


def get_user_with_data(data):
    try:

        if "facebook_id" in data:
            return AppUser.objects.get(facebook_id=data['facebook_id'], is_active=True)
        elif "google_id" in data:
            return AppUser.objects.get(google_id=data['google_id'], is_active=True)
        elif "email" in data:
            return AppUser.objects.get(email__contains=data['email'].lower(), is_active=True)
        else:
            return False
    except:
        try:
            return get_user_with_email(data['email'])
        except:
            return False


"""
Checks the system for the user with the specified email id
"""


def get_user_with_email(email):
    try:
        return AppUser.objects.filter(email__iexact=email)[0]
    except Exception as e:
        return False


def get_user_with_mobile(mobile):
    try:
        return AppUser.objects.get(mobile=mobile)
    except Exception as e:
        return False


"""
Generates a token to be returned in the serializer to the client
"""


def regenerate_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token


"""
Generates a response based on a user login
"""


def getAuthenticationResponseForUser(user):
    if user:
        token = regenerate_token(user)
        serializer = UserLoginSerializer({"token": token.key, "user": user}, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


"""
Generates a response based on a user registration
"""


def getRegistrationResponseForUser(user):
    if user:
        token = regenerate_token(user)
        serializer = UserRegisterSerializer({"token": token.key})
        response = {
            "status": True,
            "status_code": 200,
            "code": 1,
            "message": "Successfully Logged In...",
            "data": serializer.data
        }
        logging.info('Successfully loggedIn with mobile number: %s', response)
        return Response(response, status=status.HTTP_201_CREATED)
    else:
        response = {
            "status": False,
            "status_code": 200,
            "code": 0,
            "message": "Something Went Wrong..."
        }
        logging.error('Failed to loggedIn: %s', response)
        return Response(response)

"""
Creates user
"""

def create_user(data):
    print(data)
    user = AppUser()
    # user.username = data.get('username', "")
    user.first_name = data.get('first_name', "")
    # user.last_name = data.get('last_name', "")
    if data.get('email', None):
        user.email = data['email'].lower()
    else:
        user.email = "{}@invalid.com".format(data.get('mobile'))
    if data.get('mobile', None):
        user.mobile = data.get('mobile', "")
        print(user.mobile)
    if data.get('password', None):
        user.password = data['password']
    try:
        user.save()
        print(user)
        return user
    except Exception as e:
        return False
    return False
