# payments/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PaymentModel
from .serializers import PaymentSerializer
from Members.models import MemberModel

class PayFeeView(APIView):

    def post(self, request):
        phone = request.data.get('phone')

        # 🔍 Search member by phone
        member = MemberModel.objects.filter(
            phone=phone,
            is_active=True
        ).first()

        if not member:
            return Response(
                {'message': 'Member not found'},
                status=status.HTTP_404_NOT_FOUND
            )

        data = request.data.copy()
        data['member'] = member.id

        serializer = PaymentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Fee paid successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            'message': 'Payment failed',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
