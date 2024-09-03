from django.contrib import admin
from .models import Message, Insight, APIConfiguration

from django.contrib import admin
from .models import Message, Insight

from django.contrib import admin
from .models import Message, Insight

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'content', 'timestamp', 'prompt')
    search_fields = ('sender', 'content', 'prompt')
    list_filter = ('sender', 'timestamp')
    ordering = ('-timestamp',)

@admin.register(Insight)
class InsightAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'description', 'business_value', 'sql')
    search_fields = ('description', 'business_value', 'sql')
    list_filter = ('message', 'business_value')
    ordering = ('message',)


@admin.register(APIConfiguration)
class APIConfigurationAdmin(admin.ModelAdmin):
    pass

