from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import CustomUser
from users.serializers import UserSerializer


@api_view(['GET'])
def user_detail(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    serializer_context = {'request': request}
    serializer = UserSerializer(instance=user, context=serializer_context)
    return Response(serializer.data)
