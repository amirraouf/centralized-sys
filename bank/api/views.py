from __future__ import print_function, unicode_literals

from django.http.response import Http404
from .serializers import AccountDataSerializer
from bank.models import (
    BankAccount,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .lock import lock


class BankAccountDataRetrieveAPIView(RetrieveAPIView):
    queryset = BankAccount.objects.all()
    lookup_url_kwarg = 'account_id'
    serializer_class = AccountDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self, account_id):
        try:
            return BankAccount.objects.get(user_id=account_id)
        except BankAccount.DoesNotExist:
            raise Http404

    @lock
    def get(self, request,account_id, format=None):
        file_data = self.get_object(account_id=account_id)
        serialized_load = AccountDataSerializer(file_data)
        return Response(serialized_load.data.get('credit'))
