from rest_framework import serializers
from .models import Message

from rest_framework import serializers
from .models import Message, Insight

from rest_framework import serializers
from .models import Message, Insight

from rest_framework import serializers
from .models import Message, Insight

from rest_framework import serializers
from .models import Message, Insight

class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = ['description', 'business_value', 'sql']

class MessageSerializer(serializers.ModelSerializer):
    insights = InsightSerializer(many=True, read_only=True)  # Incluye insights relacionados

    class Meta:
        model = Message
        fields = ['id', 'sender', 'content', 'timestamp', 'prompt', 'insights']


from rest_framework import serializers
from .models import APIConfiguration

class APIConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIConfiguration
        fields = '__all__'
