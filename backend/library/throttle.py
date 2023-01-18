from rest_framework.throttling import AnonRateThrottle

class OTPMinuteRateThrottle(AnonRateThrottle):
    scope = 'otp_minute'

class OTPHourRateThrottle(AnonRateThrottle):
    scope = 'otp_hour'

