# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278
from django import template

from apps.interest_group.models import Membership, MemberShipRequest

register = template.Library()


def check_user(func):
    def wrapper(user, group, *args, **kwargs):
        if not user.is_authenticated():
            return False

        if user == group.owner:
            return True

        return func(user, group, *args, **kwargs)

    return wrapper


@check_user
def has_show_permissions(user, group):
    try:
        Membership.objects.get(group=group, user=user)
        return True
    except Membership.DoesNotExist:
        return False

@check_user
def is_owner_group(user, group):
    if group.owner == user:
        return True
    else:
        return False

@check_user
def is_admin_group(user, group):
    try:
        membership =Membership.objects.get(user=user, group=group)
        if membership.role == 0:
            return True
    except Membership.DoesNotExist:
        pass

    return False

@check_user
def is_join_requested(user, group):
    try:
        MemberShipRequest.objects.get(user=user, group=group, status=0)
        return True
    except MemberShipRequest.DoesNotExist:
        return False

register.filter('has_show_permissions', has_show_permissions)
register.filter('is_owner_group', is_owner_group)
register.filter('is_admin_group', is_admin_group)
register.filter('is_join_requested', is_join_requested)