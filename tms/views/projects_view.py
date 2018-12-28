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
        projects = Project.objects.filter(user_id__exact=request.user.id)
        serializer = self.serializer_class(projects, many=True)
        response = Response({
            'success': True,
            'projects': serializer.data
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
