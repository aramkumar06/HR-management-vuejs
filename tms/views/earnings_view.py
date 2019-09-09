import os
import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
from tms.serializers import EarningSerializer
from tms.services.earning_service import *


class EarningsView(viewsets.ViewSet):
    serializer_class = EarningSerializer

    def check_object_permissions(self, request, obj):
        if self.action == 'get_pending_earnings' or self.action == 'approve':
            pass
        else:
            if obj.user_id != request.user.id:
                raise PermissionDenied()

    def list(self, request):
        # TODO
        # should display only this month earning
        # expected parameters
        #   month
        #   year
        # if not specified use current week and current year
        # all time is utc time
        #
        account_id = request.GET.get('account_id', None)
        month = request.GET.get('month', None)
        year = request.GET.get('year', None)
        if month is None and year is None:
            response = Response({
                'success': False,
                'error_message': 'Month or Year should be provided'
            })

            return response

        if year is None and month is not None:
            response = Response({
                'success': False,
                'error_message': 'Month is provided but Year is not provided'
            })

            return response

        ret, summary = get_earnings(account_id, year, month, request.user.id)

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
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            if request.user.id != earning.earned_by_id and request.user.role_id != delegate_role_id:
                raise PermissionDenied()

            if earning.approved_by_id is not None and earning.approved_date is not None:
                raise PermissionDenied()

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
                'message': 'no such a earning'
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
            if earning.approved_by_id is not None and earning.approved_date is not None:
                raise PermissionDenied()

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

    @action(detail=False, methods=['post'])
    def get_pending_earnings(self, request):
        # TODO
        # permission check
        #
        team_id = request.data.get('team_id', None)
        try:
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            if request.user.role_id != delegate_role_id:
                raise PermissionDenied()

            ret = get_pending_earnings(team_id)

            response = Response({
                'success': True,
                'pending_earnings': ret,
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    @action(detail=False, methods=['post'])
    def get_delegation_month_earnings(self, request):
        # TODO
        # permission check
        # need to filter with user_id and account_id
        try:
            delegate_role_id = int(os.getenv('ROLE_DELEGATE_ID'))
            year = request.data.get('year', None)
            month = request.data.get('month', None)
            user_id = request.data.get('user_id', None)
            account_id = request.data.get('account_id', None)
            if request.user.role_id != delegate_role_id:
                raise PermissionDenied()

            ret = get_delegation_month_earnings(year, month)

            response = Response({
                'success': True,
                'earnings': ret,
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        # TODO
        # permission check
        #
        try:
            earning = Earning.objects.get(pk=pk)
            earning.approved_by = request.user
            earning.approved_date = datetime.datetime.utcnow()
            earning.save()

            ret = get_pending_earnings(request.user.team_id)

            response = Response({
                'success': True,
                'pending_earnings': ret,
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

    @action(detail=True, methods=['post'])
    def delete(self, request, pk=None):
        # TODO
        # permission check
        #
        try:
            earning = Earning.objects.get(pk=pk)
            if earning.earned_by.id != request.user.id:
                raise PermissionDenied()

            if earning.approved_by is not None or earning.approved_date is not None:
                raise PermissionDenied()

            earning.deleted_at = datetime.datetime.utcnow()
            earning.save()

            response = Response({
                'success': True,
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

