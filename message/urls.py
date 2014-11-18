from django.conf.urls import patterns, url

from postman.views import InboxView, ArchivesView, SentView, TrashView, MessageView, ReplyView, ConversationView, \
    ArchiveView, DeleteView, UndeleteView
from .views import CustomWriteView

urlpatterns = patterns('',
                        # View Postman Inbox (AJAX)
                        url(r'^ajax-inbox/$',
                            InboxView.as_view(template_name='message/inbox.html'),
                        name='message-ajax-inbox'),

                        # View Postman send (AJAX)
                        url(r'^ajax-sent/$',
                            SentView.as_view(template_name='message/sent.html'),
                        name='message-ajax-sent'),

                        # View Postman archives (AJAX)
                        url(r'^ajax-archives/$',
                            ArchivesView.as_view(template_name='message/archives.html'),
                        name='message-ajax-archives'),

                        # View Postman Trash (AJAX)
                        url(r'^ajax-trash/$',
                            TrashView.as_view(template_name='message/trash.html'),
                        name='message-ajax-trash'),

                        # Message Detail view (AJAX)
                        url(r'^ajax-view/(?P<message_id>[\d]+)/$', MessageView.as_view(template_name='message/view.html'),
                            name='message-ajax-view'),

                        # Thread detail view (AJAX)
                        url(r'^ajax-view/t/(?P<thread_id>[\d]+)/$', ConversationView.as_view(template_name='message/view.html'),
                            name='postman_view_conversation'),

                        # Message Reply view (AJAX)
                        url(r'^ajax-reply/(?P<message_id>[\d]+)/$', ReplyView.as_view(template_name='message/reply.html'),
                            name='message-ajax-reply'),

                        # Write Message (AJAX + MODAL)
                        url(r'^ajax-write/(?:(?P<recipients>[^/#]+)/)?$',
                            CustomWriteView.as_view(), name='message-ajax-write'),

                        #url(r'^archives/(?:(?P<option>'+OPTIONS+')/)?$', ArchivesView.as_view(), name='postman_archives'),
                        #url(r'^trash/(?:(?P<option>'+OPTIONS+')/)?$', TrashView.as_view(), name='postman_trash'),


                        url(r'^archive/$', ArchiveView.as_view(), name='postman_archive'),
                        url(r'^delete/$', DeleteView.as_view(), name='postman_delete'),
                        url(r'^undelete/$', UndeleteView.as_view(), name='postman_undelete'),


                       )

