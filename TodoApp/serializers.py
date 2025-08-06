from rest_framework import serializers
from .models import Todo

class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id','user','Title','CompletionDate','completionStatus','IsDelete']
        read_only_fields = ['id', 'created_at']

