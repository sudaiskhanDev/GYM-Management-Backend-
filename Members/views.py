from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from .models import MemberModel
from .serializers import MemberSerializer


# 🔹 Custom Pagination Class
class MemberPagination(PageNumberPagination):
    page_size = 10                      # default members per page
    page_size_query_param = 'limit'     # ?limit=20
    max_page_size = 50


# 🔹 Member Create + List API
class MemberCreateView(APIView):

    # ✅ Create a new member
    def post(self, request):
        serializer = MemberSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Member created successfully",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "message": "Member creation failed",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    # ✅ Get members (PAGINATED)
    def get(self, request):
        members = MemberModel.objects.filter(
            is_active=True
        ).order_by('-id')

        paginator = MemberPagination()
        paginated_members = paginator.paginate_queryset(members, request)

        serializer = MemberSerializer(paginated_members, many=True) 

        return paginator.get_paginated_response({
            "message": "Members retrieved successfully",
            "data": serializer.data
        })







# from rest_framework.views import APIView
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
# from rest_framework import status
# from .models import MemberModel
# from .serializers import MemberSerializer

# class MemberPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'limit'
#     max_page_size = 50

# #Member, API View
# class MemberCreateView(APIView):
    
#     # Create a new member
#     def post(self, request):
#      serializer = MemberSerializer(data=request.data)
#      if serializer.is_valid():
#         serializer.save()
#         return Response(
#             {"message": "Member created successfully", "data": serializer.data},
#             status=status.HTTP_201_CREATED
#         )

#     # serializer.errors is already dict
#      return Response(
#         {
#             "message": "Member creation failed",
#             "errors": serializer.errors  # <--- changed key from 'data' to 'errors'
#         },
#         status=status.HTTP_400_BAD_REQUEST
#     )

    
#     # Get all members
#     def get(self, request):
#      members = MemberModel.objects.filter(is_active=True).order_by('-id')

#      paginator = MemberPagination()
#      paginated_members = paginator.paginate_queryset(members, request)

#      serializer = MemberSerializer(paginated_members, many=True)

#      return paginator.get_paginated_response({
#         "message": "Members retrieved successfully",
#         "data": serializer.data
#     })
