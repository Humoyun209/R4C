from robots.models import Robot
from rest_framework.serializers import ModelSerializer


class RobotSerializer(ModelSerializer):
    class Meta:
        model = Robot
        fields = ['model', 'version', 'created']
    
    def create(self, validated_data):
        validated_data['serial'] = f"{validated_data.get('model')}-{validated_data.get('version')}"
        robot = Robot.objects.create(**validated_data)
        return robot
