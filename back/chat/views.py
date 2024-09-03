import json
import os
import dotenv
from django.conf import settings
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import APIConfiguration, Message, Insight
from .serializers import APIConfigurationSerializer, InsightSerializer, MessageSerializer
from .scripts.main import main as run_main_script


class APIConfigurationView(APIView):

    def get(self, request):
        try:
            config = APIConfiguration.objects.first()
            serializer = APIConfigurationSerializer(config)
            return Response(serializer.data)
        except APIConfiguration.DoesNotExist:
            return Response({'error': 'No configuration found.'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        config = APIConfiguration.objects.first()
        if config:
            serializer = APIConfigurationSerializer(config, data=request.data)
        else:
            serializer = APIConfigurationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by('timestamp')
    serializer_class = MessageSerializer








class RunScriptView(APIView):
    def post(self, request, *args, **kwargs):
        prompt = request.data.get('prompt')
        if not prompt:
            return Response({'error': 'Prompt is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ejecuta la lógica del script principal
        result, cost = run_main_script(prompt)
        
        if result == 'OK':
            # Cargar el resultado principal de la consulta
            json_path = os.path.join(settings.BASE_DIR, 'final_response.json')
            with open(json_path, 'r') as json_file:
                data = json.load(json_file)
            
            # Cargar los insights asociados a la consulta
            insights_path = os.path.join(settings.BASE_DIR, 'generated_insights.json')
            with open(insights_path, 'r') as insights_file:
                insights_data = json.load(insights_file)

            # Guardar el mensaje principal en la base de datos
            message = Message.objects.create(
                sender="System",
                content=json.dumps(data),  # Asegúrate de convertir los datos a JSON
                prompt=prompt  # Guarda el prompt del usuario
            )

            # Guardar los insights en la base de datos asociados al mensaje
            for insight in insights_data:
                Insight.objects.create(
                    message=message,
                    description=insight.get('description'),
                    business_value=insight.get('business_value'),
                    sql=insight.get('sql')
                )

            # Serializar el mensaje con los insights
            serializer = MessageSerializer(message)
            insights = Insight.objects.filter(message=message)
            insights_serializer = InsightSerializer(insights, many=True)

         
            response_data = serializer.data
            response_data['insights'] = insights_serializer.data
            response_data['cost'] = cost
            return Response(response_data, status=status.HTTP_201_CREATED)
        
        else:
            return Response({'error': 'Script execution failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ClearMessagesView(APIView):
    def delete(self, request):
        Message.objects.all().delete()
        return Response({'status': 'Messages cleared'}, status=status.HTTP_204_NO_CONTENT)
