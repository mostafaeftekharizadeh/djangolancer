"""
throttle
"""
from rest_framework.throttling import AnonRateThrottle


class OTPMinuteRateThrottle(AnonRateThrottle):
    """
    OTPMinuteRate
    """

    scope = "otp_minute"


class OTPHourRateThrottle(AnonRateThrottle):
    """
    OTPHourRate
    """

    scope = "otp_hour"
