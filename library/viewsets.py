import logging
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework import status
from rest_framework import viewsets

_logger = logging.getLogger('midlancer.api')

class ModelViewSet(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    logger = _logger

    def finalize_response(self, request, response, *args, **kwargs):
        user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
        if user_ip_address:
            ip = user_ip_address.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        pk = kwargs['pk'] if 'pk' in kwargs else None
        msg = "- {} - {:5s} - {} - User({}) - Obj({}) - {}".format(ip,
                                                 request.method,
                                                 response.status_code,
                                                 request.user.username,
                                                 pk,
                                                 request.path)
        if status.is_success(response.status_code):
            self.logger.info(msg)
        else:
            self.logger.warning(msg)
        return super(ModelViewSet, self).finalize_response(request, response, args, kwargs)

