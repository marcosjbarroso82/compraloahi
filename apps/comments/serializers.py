from django_comments_xtd.models import XtdComment

from rest_framework import serializers


class XtdCommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    class Meta:
        model = XtdComment
        exclude = ('ip_address', 'is_public', 'content_type', 'is_removed', 'site', 'user')
        read_only_fields = ('submit_date',)
        ordering = ('submit_date',)

    def get_user(self, obj):
        return obj.user.username

    def get_children(self, obj):
        try:
            return XtdComment.objects.filter(parent_id=obj.id).exclude(pk=obj.id).count()
        except:
            return 0
