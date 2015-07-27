from django.template import Library, Node
from apps.msg.models import Msg

register = Library()

class MsgUnreadCount(Node):
    def render(self, context):
        msgs = Msg.objects.filter(recipient=context['user'], read_at=None)
        return str(msgs.count())

def get_msgs_unread_count(parser, token):
    return MsgUnreadCount()

class MsgUnreadList(Node):
    def render(self, context):
        notifications = Msg.objects.filter(recipient=context['user'], read_at=None)
        context['msgs'] = notifications
        return ""

def get_msgs_unread_list(parser, token):
    return MsgUnreadList()

get_msgs_unread_list = register.tag(get_msgs_unread_list)
get_msgs_unread_count = register.tag(get_msgs_unread_count)