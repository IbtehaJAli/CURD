from rest_framework.generics import(
ListAPIView, UpdateAPIView, RetrieveAPIView,DestroyAPIView,CreateAPIView)
from ..models import student
from .serializers import idk
class Listview(ListAPIView):
    queryset = student.objects.all()
    serializer_class = idk
class update(UpdateAPIView):
    queryset = student.objects.all()
    serializer_class = idk
    lookup_field = 'pk'
class destroy(DestroyAPIView):
    queryset = student.objects.all()
    serializer_class = idk
    lookup_field = 'pk'
class create(CreateAPIView):
    queryset = student.objects.all()
    serializer_class = idk
    lookup_field = 'pk'
class displayData(RetrieveAPIView):
    queryset = student.objects.all()
    serializer_class = idk
    lookup_field = 'pk'