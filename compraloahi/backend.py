from django.utils.decorators import method_decorator
from haystack.backends.elasticsearch_backend import ElasticsearchSearchBackend, ElasticsearchSearchEngine
from haystack.backends import BaseEngine
from haystack.backends import log_query
from urllib3.exceptions import ProtocolError, ConnectionError


class RobustElasticSearchBackend(ElasticsearchSearchBackend):
    """A robust backend that doesn't crash when no connection is available"""

    def mute_error(f):

        def error_wrapper(self, *args, **kwargs):
            try:
                return f(self, *args, **kwargs)
            except TransportError:
                self.log.warn('Connection Error: elasticsearch communication error')
        return error_wrapper

    def __init__(self, connectionalias, **options):
        super(RobustElasticSearchBackend, self).__init__(connectionalias, **options)

    @mute_error
    def update(self, indexer, iterable, commit=True):
        super(RobustElasticSearchBackend, self).update(indexer, iterable, commit)

    @mute_error
    def remove(self, obj, commit=True):
        super(RobustElasticSearchBackend, self).remove(obj, commit)

    @mute_error
    def clear(self, models=[], commit=True):
        super(RobustElasticSearchBackend, self).clear(models, commit)

class RobustElasticSearchEngine(ElasticsearchSearchEngine):
    backend = RobustElasticSearchBackend