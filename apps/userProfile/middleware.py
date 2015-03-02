from .models import UserProfile
from django.http import HttpResponseRedirect



def hasnt_profile(next_url=""):
    if next_url != '' and next_url != '/' : url = '?next=' + next_url
    else: url = ''
    return HttpResponseRedirect('/accounts/profile/create/' + url)

class ValidProfileCreatedMiddleware(object):

    def process_request(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated() \
                and hasattr(request, 'path') and request.path != '/accounts/profile/create/':
            try:
                user_profile = UserProfile.objects.get(user = request.user)
                if user_profile and user_profile.birth_date and request.user.first_name != '' and request.user.last_name != '':
                    return None
                else:
                    return hasnt_profile(request.path)
            except UserProfile.DoesNotExist:
                return hasnt_profile(request.path)
        else:
            return None

