from .models import User, UserDetails
from django.contrib.auth.hashers import make_password

def signup_verify(data):
    try:
        email = data['email']
        username = data['username']
        phone_number = data['phone_number']
        pass1 = data['pass1']
        pass2 = data['pass2']
        location = data['location']
        company_name = data['company_name']
        brand=data['brand']
        client_type = data['client_type']
        avg_revenue = data['avg_revenue']

        if(pass1 == pass2):
            current_user = User.objects.create(
                username=username,
                email=email,
                password=make_password(pass1),
            )
            UserDetails.objects.create(
                user=current_user,
                phone_number=phone_number,
                address=location,
                company_name=company_name,
                brand=brand,
                client_type=client_type,
                avg_revenue=avg_revenue,
            )
            return True,current_user
        else:
            return "password not match"

    except:
        return False