import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from core.models import User
from openedx.core.djangoapps.oauth_dispatch.jwt import create_jwt_for_user
from django.contrib.auth.models import User



class ResponseSuccess(Response):
    def __init__(self, data=None, http_status=None, content_type=None):
        _status = http_status or status.HTTP_200_OK
        data = data or {}
        reply = {"response": {"success": True}}
        reply['response'].update(data)
        super().__init__(data=reply, status=_status,
                                              content_type=content_type)



class UsersAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        results = [
            {'id': user.id, 'name': user.name}
            for user in users
        ]
        return Response(json.dumps(results) content_type='application/json')


class RefreshToken(APIView):
    def post(self, request):
        token = request.data.get('token')
        username = request.data.get('username')
        user = User.objects.get(username=username)
        token = create_jwt_for_user(user)
        return Response(json.dumps({
            'token': str(token),

        }), content_type='application/json')
