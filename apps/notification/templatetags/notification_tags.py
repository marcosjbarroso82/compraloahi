from django.template import Library, Node
from apps.notification.models import Notification

register = Library()

class NotificationUnreadCount(Node):
    def render(self, context):
        notifications = Notification.objects.filter(receiver=context['user'], read=None)
        return str(notifications.count())

def get_notifications_unread_count(parser, token):
    return NotificationUnreadCount()

class NotificacionUnreadList(Node):
    def render(self, context):
        notifications = Notification.objects.filter(receiver=context['user'], read=None)
        context['notifications'] = notifications
        return ""


def get_notificacions_unread_list(parser, token):
    return NotificacionUnreadList()

get_notificacions_unread_list = register.tag(get_notificacions_unread_list)
get_notifications_unread_count = register.tag(get_notifications_unread_count)