from __future__ import absolute_import

from django.conf.urls import *
from . import views

from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^faq/$',
        views.TopicList.as_view(),
        name='faq_topic_list'),
    url(r'^$',
        views.FaqIndexView.as_view(),
        name='faq_index'),
    url(r'^search/$',
        views.SearchView.as_view(),
        name='faq_search'),

    url(r'^questions/$',
        views.QuestionOverviewList.as_view(),
        name='faq_question_list',),

    url(r'^detail/(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/helpful$',
        views.QuestionHelpfulVote.as_view(),
        name='question_helpful'
    ),
    url(r'^submit/$',
        views.SubmitFAQ.as_view(),
        name='faq_submit',
    ),
    url(r'^submit/thanks/$',
        views.SubmitFAQThanks.as_view(),
        name='faq_submit_thanks',
    ),
    url(r'^(?P<slug>[\w-]+)/$',
        views.TopicDetail.as_view(),
        name='faq_topic_detail',
    ),
    # url(r'^(?P<topic_slug>[\w-]+)/(?P<slug>[\w-]+)/$',
    #     views.QuestionDetail.as_view(),
    #     name='faq_question_detail',
    # ),
)