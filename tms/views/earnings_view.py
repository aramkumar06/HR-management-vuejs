from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from tms.serializers import EarningSerializer
from tms.services.earning_service import *


class EarningsView(viewsets.ViewSet):
    serializer_class = EarningSerializer

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        # TODO
        # should display only this month earning
        # expected parameters
        #   week
        #   month
        #   year
        # if not specified use current week and current year
        # all time is utc time
        #
        account_id = request.GET.get('account_id', None)
        week = request.GET.get('week', None)
        month = request.GET.get('month', None)
        year = request.GET.get('year', None)
        if month is None and year is None:
            response = Response({
                'success': False,
                'error_message': 'Month or Year should be provided'
            })

            return response

        ret, summary = get_earnings(account_id, year, month, week)

        response = Response({
            'success': True,
            'earnings': ret,
            'summary': summary,
        })

        return response

    def create(self, request):
        # TODO
        #   should validate permission
        #   should validate whether week is in current month or not
        #
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid()
        if serializer.errors:
            response = Response({
                'success': False,
                'message': serializer.errors
            })
        else:
            serializer.save()
            response = Response({
                'success': True,
                'message': 'successfully created!'
            })

        return response

    def retrieve(self, request, pk=None):
        try:
            earning = Earning.objects.get(pk=pk)
            serializer = self.serializer_class(earning)
            response = Response({
                'success': True,
                'earning': serializer.data
            })
        except Earning.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a earnings'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def update(self, request, pk=None):
        try:
            earning = Earning.objects.get(pk=pk)
            self.check_object_permissions(request, earning)
            serializer = self.serializer_class(data=request.data, instance=earning)
            serializer.is_valid(raise_exception=True)
            if serializer.errors:
                response = Response({
                    'success': False,
                    'message': serializer.errors
                })
            else:
                serializer.save()
                response = Response({
                    'success': True,
                    'message': 'successfully updated!'
                })
        except Earning.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a earnings'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        try:
            earning = Earning.objects.get(pk=pk)
            self.check_object_permissions(request, earning)
            earning.delete()
            response = Response({
                'success': True,
                'id': earning.id
            })
        except Earning.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a earnings'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response
