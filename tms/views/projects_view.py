from rest_framework import viewsets
from rest_framework.response import Response
from django.core.exceptions import PermissionDenied
from tms.models import Project
from tms.serializers import ProjectSerializer


class ProjectsView(viewsets.ViewSet):
    serializer_class = ProjectSerializer

    def check_object_permissions(self, request, obj):
        if obj.user_id != request.user.id:
            raise PermissionDenied()

    def list(self, request):
        raw_query = """
            SELECT
                tp.id           AS id
              , tp.title        AS title
              , tp.start_date   AS start_date
              , tp.project_type AS project_type
              , tp.status       AS status
              , tc.first_name   AS client_first_name
              , tc.last_name    AS client_last_name
              , ta.first_name   AS account_first_name
              , ta.last_name    AS account_last_name
              , ts.name         AS site_name
            FROM
              tms_project AS tp
            INNER JOIN tms_client AS tc ON tp.client_id = tc.id
            INNER JOIN tms_account AS ta ON tc.account_id = ta.id
            INNER JOIN tms_site AS ts ON tc.site_id = ts.id
            WHERE tp.user_in_charge_id = {user_id}
              AND tp.status = 'ST'
        """.format(
            user_id=request.user.id
        )
        client_id = request.GET.get('client_id', None)
        account_id = request.GET.get('account_id', None)
        if client_id is not None:
            raw_query = raw_query + " WHERE tp.id = " + client_id

        if account_id is not None:
            raw_query = raw_query + " WHERE tp.id = " + account_id

        projects = Project.objects.raw(raw_query)
        ret = []
        for project in projects:
            ret.append({
                "id":                   project.id,
                "title":                project.title,
                "start_date":           project.start_date,
                "project_type":         project.project_type,
                "status":               project.status,
                "client_first_name":    project.client_first_name,
                "client_last_name":     project.client_last_name,
                "account_first_name":   project.account_first_name,
                "account_last_name":    project.account_last_name,
                "site_name":            project.site_name
            })

        response = Response({
            'success': True,
            'projects': ret
        })

        return response

    def create(self, request):
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
            project = Project.objects.get(pk=pk)
            serializer = self.serializer_class(project)
            response = Response({
                'success': True,
                'project': serializer.data
            })
        except Project.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a project'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response

    def update(self, request, pk=None):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(request, project)
            serializer = self.serializer_class(data=request.data, instance=project)
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
        except Project.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a project'
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
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(request, project)
            project.delete()
            response = Response({
                'success': True,
                'id': project.id
            })
        except Project.DoesNotExist:
            response = Response({
                'success': False,
                'message': 'no such a project'
            })
        except PermissionDenied:
            response = Response({
                'success': False,
                'message': 'no permission'
            })

        return response
