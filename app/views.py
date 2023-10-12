from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app.authorization import verify_user_token , sign_token
from app.helper import validate_id

@method_decorator(csrf_exempt, name="dispatch")
class serverStatus(APIView):
    def get(self, request):
        return Response(
            {
                "success":True,
                "message": "Server is running"
            },
            status=status.HTTP_200_OK,
        )

@method_decorator(csrf_exempt, name="dispatch")
class auth(APIView):
    """get jwt token for authorization"""
    def post(self, request):
        print(request.data.get("company_id"))
        if not validate_id(request.data.get("company_id")):
            return Response("something went wrong ok!", status.HTTP_400_BAD_REQUEST)
        user = {
            "username": request.data.get("username"),
            "portfolio": request.data.get("portfolio"),
            "data_type": request.data.get("data_type"),
            "company_id": request.data.get("company_id"),
        }
        return sign_token(user)
    
@method_decorator(csrf_exempt, name="dispatch")
class SecureEndPoint(APIView):
    @verify_user_token
    def post(self, request, user):
        name = request.data.get('name')
        email = request.data.get('email')

        return Response({
            "success": True,
            "message": "sample output",
            "name": name,
            "email": email
        })

    @verify_user_token
    def get(self, request, user):
        return Response({
            "success": True,
            "message": "sample output",
            "name": "Manish",
            "email": "manish@gmail.com"
        })