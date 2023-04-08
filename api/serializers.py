from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    create = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    
    
    class Meta:
        model = Todo
        fields = ["id", "title","memo", "create", "completed"]
        


class TodoToggleCompleteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ["id"]
        read_only_fields = ["title","memo", "create", "completed" ]
        
        