from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from activities.models import Activity
from .serializers import ActivitySerializer
from .permissions import IsOwnerOrReadOnly

class ActivitiesRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field            = 'pk'
    serializer_class        = ActivitySerializer
    authentication_classes  = [SessionAuthentication, BasicAuthentication]
    permission_classes      = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)


class ActivitiesView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'
    serializer_class    = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
