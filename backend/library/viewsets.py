"""
Library view
"""
import logging
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from rest_framework import status
from rest_framework import viewsets

_logger = logging.getLogger("midlancer.api")


class ModelViewSet(viewsets.ModelViewSet):
    """
    Library model view
    """

    throttle_classes = [UserRateThrottle, AnonRateThrottle]
    logger = _logger

    def finalize_response(self, request, response, *args, **kwargs):
        user_ip_address = request.META.get("HTTP_X_FORWARDED_FOR")
        if user_ip_address:
            ip_address = user_ip_address.split(",")[0]
        else:
            ip_address = request.META.get("REMOTE_ADDR")
        primary_key = kwargs["pk"] if "pk" in kwargs else None
        msg = f"- {ip_address} - {request.method:5s} - {response.status_code} - User({request.user.username}) - Obj({primary_key}) - {request.path}".format()
        if status.is_success(response.status_code):
            self.logger.info(msg)
        else:
            self.logger.warning(msg)
        return super(ModelViewSet, self).finalize_response(
            request, response, args, kwargs
        )
