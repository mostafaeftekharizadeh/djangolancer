import logging
from rest_framework import viewsets

_logger = logging.getLogger('midlancer.api')
class ModelViewSet(viewsets.ModelViewSet):
    logger = _logger

    def finalize_response(self, request, response, *args, **kwargs):
        pk = kwargs['pk'] if 'pk' in kwargs else None
        self.logger.info("- {} - {} - User({}) - Obj({}) - {}".format(request.method,
                                                 response.status_code,
                                                 request.user.username,
                                                 pk,
                                                 request.path))
        return super(ModelViewSet, self).finalize_response(request, response, args, kwargs)
