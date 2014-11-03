from django.conf.urls import patterns, url

from .views import WriteModalView

urlpatterns = patterns('',
                       url(r'^write_message/$', 'message.views.writeMessageModal',
                           name="write-modal-message"),

                       )
