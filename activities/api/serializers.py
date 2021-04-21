from rest_framework import serializers
from activities.models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [
            'pk',
            'activity',
            'project',
            'to_do_date',
            'end_date',
            'is_done',
            'user'
        ]
        read_only_fields = [
            'user',
            'pk'
        ]