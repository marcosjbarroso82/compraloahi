from django.template import Library, Node
from apps.comment_notification.models import CommentNotification
from django.contrib.auth.models import User

register = Library()


class UserUnrepliedCommentNotificationCount(Node):
    def render(self, context):
        notifications = CommentNotification.objects.all().filter(receiver=context['user'], type='not_replied')
        return str(notifications.count())

def get_user_comment_unreplied_notification_count(parser, token):
    return UserUnrepliedCommentNotificationCount()

class UserUnrepliedCommentNotification(Node):
    def render(self, context):
        notifications = CommentNotification.objects.all().filter(receiver=context['user'], type='not_replied')
        context['not_replied_notifications'] = notifications
        return ""


def get_user_comment_unreplied_notification(parser, token):
    return UserUnrepliedCommentNotification()

get_user_comment_unreplied_notification = register.tag(get_user_comment_unreplied_notification)
get_user_comment_unreplied_notification_count = register.tag(get_user_comment_unreplied_notification_count)