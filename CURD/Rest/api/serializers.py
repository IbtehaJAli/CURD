from rest_framework.serializers import ModelSerializer
from ..models import student
class idk(ModelSerializer):
    class Meta:
        model= student
        fields=[
            'id',
            'name',
            'rollNumber',
            'mail'
        ]
