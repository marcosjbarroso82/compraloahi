from django.conf.urls import patterns, url

from postman.views import MessageView, InboxView, ArchivesView, SentView, TrashView


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
                        # View Postman Tash (AJAX)
                        url(r'^ajax-trash/$',
                            TrashView.as_view(template_name='message/trash.html'),
                        name='message-ajax-trash'),
                       )
