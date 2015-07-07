from . import models
from rest_framework import serializers

import pdb

class SkipField(Exception):
    pass

class CustomBooleanField(serializers.BooleanField):

    def to_internal_value(self, data):
        raise SkipField()

    def to_representation(self, value):
        return True


class MsgSerializer(serializers.ModelSerializer):
    is_new = serializers.BooleanField()
    sender_deleted = serializers.BooleanField()
    recipient_deleted = serializers.BooleanField()
    is_replied = serializers.BooleanField(read_only=True)

    class Meta:
        model = models.Msg
        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'sender', 'moderation_status',
                            'parent', 'thread', 'moderation_reason', 'moderation_date')


    def __init__(self, *args, **kwargs):
        super(MsgSerializer, self).__init__(*args, **kwargs)
        user = kwargs['context']['request'].user
        action = self.context['view'].action

        # Filter fields depending on whether it's a sender or a recipient
        not_allowed_to_show = ()
        # pdb.set_trace()
        user_type = None
        try:
            if user == self.instance.recipient:
                user_type = 'recipient'
            elif user == self.instance.sender:
                user_type = 'sender'
        except:
            pass

        # not_allowed_to_show = ('recipient', )
        # not_allowed_to_show = ('recipient',)

        if user_type == 'recipient' or action == 'inbox':
            not_allowed_to_show = ('recipient', 'sender_archived', 'sender_deleted_at', 'sender', 'sender_deleted',
                                    'moderation_status', 'recipient_deleted_at', 'moderation_reason', 'moderation_date')
        elif user_type == 'sender' or action == 'sent':
            not_allowed_to_show = ( 'read_at', 'is_new', 'replied_at', 'is_replied', 'recipient_deleted',
                                    'recipient_archived', 'recipient_deleted_at', 'recipient')

        if action != 'create':
            # Set what fields should be updatable by sender
            self.fields['subject'].read_only = True
            self.fields['body'].read_only = True

        for field_name in not_allowed_to_show:
            self.fields.pop(field_name)


            # self.context['request'].data
            # self.context['request'].method
            #
            # self.context['view']
            # self.context['view']
            # self.context['view'].action   # ['list',
            # self.context['view'].list
            # self.context['view'].