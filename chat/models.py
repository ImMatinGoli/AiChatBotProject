from django.db import models
from django.conf import settings

class Conversation(models.Model):
    # وضعیت‌های مدل هوش مصنوعی (برای انتخاب API)
    MODEL_CHOICES = [
        ('gpt-4o', 'GPT-4o'),
        ('gpt-3.5-turbo', 'GPT-3.5 Turbo'),
        ('gemini-pro', 'Gemini Pro'),  # <--- این خط اضافه شد
        ('llama-2', 'Llama 2 (Local)'),  # <--- مثلا یه مدل لوکال
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversations')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name="عنوان مکالمه")
    ai_model = models.CharField(max_length=50, choices=MODEL_CHOICES, default='gpt-3.5-turbo', verbose_name="مدل انتخاب شده")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # برای اینکه بفهمیم آخرین تغییر کی بوده

    class Meta:
        ordering = ['-updated_at'] # مکالمات جدیدتر اول نشون داده بشن

    def __str__(self):
        return self.title or f"مکالمه {self.id}"


class Message(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
        ('system', 'System'), # اگه بخوایم پرامپت اولیه مخفی بدیم
    ]

    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField(verbose_name="متن پیام")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at'] # پیام‌ها به ترتیب زمان ارسال نشون داده بشن

    def __str__(self):
        return f"{self.role}: {self.content[:30]}..."