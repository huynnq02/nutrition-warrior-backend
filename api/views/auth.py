from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from ..serializers.user import UserSerializer
import cloudinary
import cloudinary.uploader
from ..models.user import User
from ..config import *
import bcrypt

from django.core.mail import send_mail
from ..models.otp import OTP
from ..serializers.otp import OTPSerializer
from datetime import datetime, timedelta
import random


@api_view(['POST'])
def create_user(request):
    """
    Create a new user.

    Required POST parameters:
    - email: The email of the user.
    - password: The password of the user.

    Returns:
    Response: The HTTP response indicating the success or failure of the operation.

    Raises:
    Exception: If any error occurs while creating the user.
    """
    try:
        email = request.data.get('email')
        print(email)
        if User.objects.filter(email=email).count() > 0:
            return Response({'success': False, 'message': 'Email already exists'}, status=status.HTTP_409_CONFLICT)

        password = request.data.get('password')
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        request.data['password'] = hashed_password
        
        user = User(**request.data)
        user.save()

        return Response({'success': True, 'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def update_user(request, id):
    """
    Update an existing user.

    Required PUT parameters:
    - Any field(s) that need to be updated, except 'id'.
    - If the 'picture' field is provided, it will be uploaded to Cloudinary and the URL will be stored in 'profile_picture' field of the user.

    Returns:
    Response: The HTTP response indicating the success or failure of the operation.

    Raises:
    User.DoesNotExist: If the user with the specified ID does not exist.
    Exception: If any error occurs while updating the user.
    """
    try:
        user = User.objects.get(id=id)

        # Update the user fields based on the data provided in the request body
        for key, value in request.data.items():
            if key == 'id':
                continue
            if key == 'picture':
                # Upload the picture to Cloudinary and get the URL
                upload_result = cloudinary.uploader.upload(value)
                profile_picture_url = upload_result['secure_url']
                setattr(user, 'profile_picture', profile_picture_url)
            else:
                setattr(user, key, value)

        user.save()
        user_data = UserSerializer(user).data
        return Response({'success': True, 'message': 'User update successful', 'data': user_data}, status=status.HTTP_200_OK)

    except User.DoesNotExist:
        return Response({'success': False, 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def login_user(request):
    """
    Authenticate and login a user.

    Required POST parameters:
    - email: The email of the user.
    - password: The password of the user.

    Returns:
    Response: The HTTP response indicating the success or failure of the operation.

    Raises:
    User.DoesNotExist: If the user with the specified email does not exist.
    Exception: If any error occurs while authenticating and logging in the user.
    """
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.get(email=email)
        is_match = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        if is_match:    
            if not user.first_login:
                user.first_login = datetime.datetime.now()
                user.save()
            user_data = UserSerializer(user).data
            # Password is correct, authentication successful
            return Response({'success': True, 'message': 'Login successful', 'data': user_data}, status=200)
        else:
            # Password is incorrect
            return Response({'success': False, 'message': 'Incorrect password'}, status=401)

    except User.DoesNotExist:
        # User not found
        return Response({'success': False, 'message': 'User not found'}, status=404)

    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)

@api_view(['POST'])
def reset_password(request):
    """
    """
    try:
        email = request.data.get('email') 
        user = User.objects.get(email=email)
        if user:
            otp_code = str(random.randint(10000,99999))
            expiration_time = datetime.now() + timedelta(minutes=2)
            otp_data = {
                'email': email, 
                'otp_code':otp_code, 
                'expiration_time':expiration_time
                }
            serializer = OTPSerializer(data=otp_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response({'success': False,'message': 'User not found'},status=status.HTTP_404_NOT_FOUND)
        
        subject = "Password Reset OTP"
        message = f'Your OTP is {otp_code}'
        recipient_list = [email]

        send_mail(subject, message, None, recipient_list)

        return Response({'sucess': False, 'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)
    
@api_view(['POST'])
def auth_otp(request):
    """
    """
    try:
        otp_code = request.data.get('otp') 
        email = request.data.get('email') 
        otp = OTP.objects(email=email,otp_code=otp_code).first()
        if otp:
            check_expire = otp.expiration_time > datetime.now()
            if check_expire: 
                return Response({'success': True,'message': 'OTP is valid'}, status=status.HTTP_200_OK)
        return Response({'success':False,'message': 'OTP is invalid'},status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)
    
@api_view(['POST'])
def change_password(request):
    """
    """
    try:
        email = request.data.get('email') 
        new_password = request.data.get('password') 

        user = User.objects.get(email=email)
        if user:
            hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user.password = hashed_password
            user.save()
            return Response({'success': True,'message': 'Reset password successfully'}, status=status.HTTP_200_OK)
        return Response({'success':False,'message': 'Reset password failed'},status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({'success': False, 'message': str(e)}, status=500)
    