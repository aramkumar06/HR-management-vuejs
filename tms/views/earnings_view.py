from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from tms.models import Earning
from tms.serializers import EarningSerializer
from datetime import datetime


class EarningsView(viewsets.ViewSet):
    serializer_class = EarningSerializer

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        # TODO
        # should display only this month earning
        # expected parameters
        #   project_id
        #   week
        #   month
        #   year
        # if not specified use current week and current year
        # all time is utc time
        #
        project_id = request.GET.get('project_id', None)
        client_id = request.GET.get('client_id', None)
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

        if project_id is not None:
            project_query = " AND tp.id = " + project_id
        else:
            project_query = ""

        if client_id is not None:
            client_query = " AND tc.id = " + client_id
        else:
            client_query = ""

        if account_id is not None:
            account_query = " AND ta.id = " + account_id
        else:
            account_query = ""

        if week is not None:
            week_query = " AND te.week_of_year = " + week
        else:
            week_query = ""

        if month is not None:
            month_query = """
            INNER JOIN LATERAL (
                SELECT *
                FROM tms_book AS tb
                WHERE te.year = tb.year 
                AND te.week_of_year = ANY(tb.weeks)
                AND tb.month = %s
                LIMIT 1
            ) x ON TRUE
            """ % (month, )
        else:
            month_query = ""

        if year is not None:
            year_query = " AND te.year = " + year
        else:
            year_query = ""

        raw_query = """
            SELECT
                te.id AS id
              , te.cost AS cost  
              , te.year AS year
              , te.week_of_year AS week_of_year
              , te.status AS status
              , ts.name AS site_name
              , ta.first_name AS account_first_name
              , ta.last_name AS account_last_name
              , tc.first_name AS client_first_name
              , tc.last_name AS client_last_name
              , tp.title AS project_title 
            FROM
              tms_earning AS te
            INNER JOIN tms_project AS tp ON te.project_id = tp.id
            INNER JOIN tms_client AS tc ON tp.client_id = tc.id
            INNER JOIN tms_account AS ta ON tc.account_id = ta.id
            INNER JOIN tms_site AS ts ON ta.site_id = ts.id
            INNER JOIN tms_user AS tu ON tp.user_in_charge_id = tu.id
            %s
            WHERE te.deleted_at IS NULL
            %s
            %s
            %s
            %s
            %s
        ;
        """ % (month_query, project_query, client_query, account_query, week_query, year_query)
        earnings = Earning.objects.raw(raw_query)
        ret = []
        summary = 0.0
        for earning in earnings:
            ret.append({
                "id": earning.id,
                "cost": earning.cost,
                "year": earning.year,
                "week_of_year": earning.week_of_year,
                "status": earning.status,
                "site_name": earning.site_name,
                "account_first_name": earning.account_first_name,
                "account_last_name": earning.account_last_name,
                "client_first_name": earning.client_first_name,
                "client_last_name": earning.client_last_name,
                "project_title": earning.project_title
            })
            summary += earning.cost

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
