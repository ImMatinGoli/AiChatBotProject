from .models import Conversation

def user_conversations(request):
    if request.user.is_authenticated:
        # لیست مکالمات کاربر رو میگیره و مرتب میکنه
        conversations = Conversation.objects.filter(user=request.user).order_by('-updated_at')
        return {'conversations': conversations}
    return {'conversations': []}