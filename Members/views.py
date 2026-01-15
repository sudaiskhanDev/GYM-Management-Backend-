from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MemberModel
from .serializers import MemberSerializer


#Member, API View
class MemberCreateView(APIView):
    
    # Create a new member
    def post(self, request):
     serializer = MemberSerializer(data=request.data)
     if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Member created successfully", "data": serializer.data},
            status=status.HTTP_201_CREATED
        )

    # serializer.errors is already dict
     return Response(
        {
            "message": "Member creation failed",
            "errors": serializer.errors  # <--- changed key from 'data' to 'errors'
        },
        status=status.HTTP_400_BAD_REQUEST
    )

    
    # Get all members
    def get(self, request):
        members = MemberModel.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response({"message": "Members retrieved successfully", "data":serializer.data}, status=status.HTTP_200_OK)
      