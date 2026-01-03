from django.contrib import admin
from .models import Conversation, Message

class MessageInline(admin.TabularInline):
    model = Message
    extra = 0 # فیلد اضافه خالی نشون نده

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'ai_model', 'created_at')
    inlines = [MessageInline] # اینجوری پیام‌های هر چت رو توی صفحه خودش می‌بینیم

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('conversation', 'role', 'content', 'created_at')