from django.db.models import Q
from django.shortcuts import get_object_or_404
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
    # ✅ Get members (PAGINATED + SEARCH + MEMBERSHIP FILTER)
    def get(self, request):
        search_query = request.GET.get('search', '')       # ?search=abc
        membership_filter = request.GET.get('membership', '')  # ?membership=golden

        members = MemberModel.objects.filter(is_active=True).order_by('-id')

        # 🔹 Search logic
        if search_query:
            members = members.filter(
                Q(name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(phone__icontains=search_query)
            )

        # 🔹 Membership filter
        if membership_filter and membership_filter.lower() != 'all':
            members = members.filter(membership=membership_filter.lower())

        paginator = MemberPagination()
        paginated_members = paginator.paginate_queryset(members, request)

        serializer = MemberSerializer(paginated_members, many=True)

        return paginator.get_paginated_response({
            "message": "Members retrieved successfully",
            "data": serializer.data
        })





# 🔹 Additional views (Retrieve, Update, Delete) can be added similarly
class MemberEditView(APIView):

    #Update an Existing Expense
    def put(self, request, pk):
        member = MemberModel.objects.get(id=pk)
        serializer = MemberSerializer(member, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message' : 'Member updated successfully',
                'data' : serializer.data
            },
            status=status.HTTP_200_OK)
            
        return Response({
            'message' : 'Member update failed',
            'errors' : serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)
        
    #Patch method for partial update
    def patch(self, request, pk):
        member = get_object_or_404(MemberModel, id=pk)
        serializer = MemberSerializer(
            member, data=request.data, partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message' : 'Member partially updated successfully',
                'data' : serializer.data
            },
            status=status.HTTP_200_OK)
            
        return Response({
            'message' : 'Member partially update failed',
            'errors' : serializer.errors
        },
                        status=status.HTTP_400_BAD_REQUEST)
        
    #Delete an existing member
    def delete(self, request, pk):
        member = get_object_or_404(MemberModel, id=pk)
        member.is_active = False
        member.save()
        
        return Response({
            'message' : 'Member deleted successfully'
        },
                        status=status.HTTP_200_OK)