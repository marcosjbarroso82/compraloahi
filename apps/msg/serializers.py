from . import models
from rest_framework import serializers

import pdb

class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Msg

        read_only_fields = ('sent_at', 'read_at', 'replied_at', 'sender_archived', 'recipient_archived', 'sender_deleted_at',
                            'recipient_deleted_at', 'sender', 'moderation_status',
                            'parent', 'thread', 'moderation_reason', 'moderation_date')

    def __init__(self, *args, **kwargs):
        super(MsgSerializer, self).__init__(*args, **kwargs)
        user = kwargs['context']['request'].user
        action = self.context['view'].action
        # pdb.set_trace()
        print("============")
        print(self.context['view'].action)
        # Filter fields depending on whether it's a sender or a recipient
        not_allowed_to_show = ()

        try:
            if  user == self.instance.recipient:
                print("Im the recipient")
                not_allowed_to_show = ('sender_archived', 'sender_deleted_at', 'sender',
                               'moderation_status', 'recipient_deleted_at', 'moderation_reason', 'moderation_date')
                # Set what fields should updatable by the recipient
            elif user == self.instance.sender:
                print("Im the sender")
                not_allowed_to_show = ('read_at', 'recipient_archived', 'recipient_deleted_at', 'recipient')
                # Set what fields should be updatable by sender
                # pdb.set_trace()
                self.fields['subject'].read_only = True
                self.fields['body'].read_only = True
                self.fields['sender_archived'].read_only = False

        except:
            pass

        if(action == 'update' or action == 'partial_update'):
            print("we're UPDATING")



        for field_name in not_allowed_to_show:
            self.fields.pop(field_name)

        action = self.context['view'].action
        # TODO: Modify fields to make them writable

        # self.context['request'].data
        # self.context['request'].method
        #
        # self.context['view']
        # self.context['view']
        # self.context['view'].action   # ['list',
        # self.context['view'].list
        # self.context['view'].