from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation, Message
from .ai_service import generate_response


@login_required(login_url='account_login')
def chat_view(request, conversation_id=None):
    user = request.user

    # 1. گرفتن لیست مکالمات برای سایدبار (اگر کانتکست پروسسور نداری)
    # اگر کانتکست پروسسور رو ست کردی، این خط لازم نیست ولی بودنش ضرری نداره
    conversations = Conversation.objects.filter(user=user).order_by('-updated_at')

    # 2. متغیرهای پیش‌فرض
    current_conversation = None
    messages = []

    # 3. اگر ID مکالمه توی URL بود:
    if conversation_id:
        current_conversation = get_object_or_404(Conversation, id=conversation_id, user=user)
        messages = current_conversation.messages.all()

    # --- هندل کردن پست (ارسال پیام جدید) ---
    if request.method == 'POST':
        content = request.POST.get('message')
        # گرفتن مدل از فرم (یا پیش‌فرض gpt-4o)
        selected_model = request.POST.get('model', 'gpt-4o')

        if content:
            if not current_conversation:
                # مکالمه جدید
                title = content[:30] + "..." if len(content) > 30 else content
                current_conversation = Conversation.objects.create(
                    user=user,
                    title=title,
                    ai_model=selected_model  # ذخیره مدلی که کاربر انتخاب کرده
                )
            else:
                # اگر مکالمه قبلا بوده، می‌تونیم مدلش رو آپدیت کنیم یا ثابت نگه داریم
                # اینجا فرض میکنیم مدل همونیه که قبلا بوده (مگر اینکه بخوای عوض بشه)
                pass

            # ذخیره پیام کاربر
            Message.objects.create(
                conversation=current_conversation,
                role='user',
                content=content
            )

            # --- تغییر اصلی اینجاست ---
            # قبلاً بود: reply = generate_response(content)
            # الان باید بگیم با چه مدلی جواب بده:
            reply = generate_response(content, current_conversation.ai_model)

            # ذخیره پیام ربات
            Message.objects.create(
                conversation=current_conversation,
                role='assistant',
                content=reply
            )

            # آپدیت زمان مکالمه
            current_conversation.save()

            return redirect('conversation_detail', conversation_id=current_conversation.id)

    context = {
        'conversations': conversations,
        'current_conversation': current_conversation,
        'messages': messages,
    }

    return render(request, 'chat/chat_page.html', context)