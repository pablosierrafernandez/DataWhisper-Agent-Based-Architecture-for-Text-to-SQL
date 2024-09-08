from django.db import models

from django.db import models

from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=255)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    prompt = models.TextField(null=True, blank=True)  
    sql = models.TextField(null=True, blank=True)  
    def __str__(self):
        return f"{self.sender}: {self.content[:50]}"  



class Insight(models.Model):
    message = models.ForeignKey(Message, related_name='insights', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    business_value = models.CharField(max_length=255, null=True, blank=True)
    sql = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.description



class APIConfiguration(models.Model):
  
    hostname = models.CharField(max_length=255)
    database = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.IntegerField()
    openai_api_key = models.CharField(max_length=255)
    huggingface_api_key = models.CharField(max_length=255, default=None)

    opcion = models.BooleanField(default=False)
    model_name = models.CharField(max_length=200, blank=True, default='')
    num_insights = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if APIConfiguration.objects.exists() and not self.pk:
            APIConfiguration.objects.all().delete()
        super(APIConfiguration, self).save(*args, **kwargs)
        APIConfiguration.load_configuration()

    @classmethod
    def load_configuration(cls):
        config = cls.objects.first()
        if config:
            cls._global_config = {
                'hostname': config.hostname,
                'database': config.database,
                'username': config.username,
                'password': config.password,
                'port': config.port,
                'openai_api_key': config.openai_api_key,
                'opcion': config.opcion,
                'num_insights': config.num_insights,
                'model_name': config.model_name,
            }

           
            if config.huggingface_api_key:
                cls._global_config['huggingface_api_key'] = config.huggingface_api_key

        else:
            raise Exception("No APIConfiguration found.")

    @classmethod
    def get_global_config(cls):
        if not hasattr(cls, '_global_config'):
            cls.load_configuration()
        return cls._global_config
