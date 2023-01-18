"""
user api endpoints module
"""
import logging
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status, serializers
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django_filters import rest_framework as filters
from library.viewsets import ModelViewSet
from library.throttle import OTPMinuteRateThrottle, OTPHourRateThrottle
from .user_serializers import (
    UserSerializer,
    AuthTokenSerializer,
    OtpSerializer,
    PartySerializer,
    ChangePasswordSerializer,
)
from .profile_serializers import ProfileSerializer
from .user_models import Otp
from .profile_models import Party, Profile, Vote

User = get_user_model()
_logger = logging.getLogger("midlancer.api.user.user")


class OtpViewSet(ModelViewSet):
    """
    Otp endpoint Viewset
    """

    queryset = Otp.objects.all()
    serializer_class = OtpSerializer
    permission_classes = (permissions.AllowAny,)
    http_method_names = ["post"]
    throttle_classes = [OTPMinuteRateThrottle, OTPHourRateThrottle]


class PartyViewSet(ModelViewSet):
    """
    Party endpoint Viewset
    """

    queryset = Party.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = PartySerializer
    logger = _logger


class LoginView(generics.CreateAPIView):
    """
    User login endpoint Viewset
    """

    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        return user, profile and token if username/password is valid
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid(raise_exception=False):
            if "password" in request.data:
                request.data["password"] = "**********"
            _logger.error("Login failed %s", request.data)
            raise serializers.ValidationError(serializer.errors)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        data = {"id": user.id, "token": token.key, "profile": None, "party": None}
        if hasattr(user, "party"):
            data["party"] = user.party.id
            profile = ProfileSerializer(
                Profile.objects.filter(party=user.party),
                context={"request": request},
                many=True,
            ).data
            if len(profile) > 0:
                data["profile"] = profile[0]
        if "password" in request.data:
            request.data["password"] = "**********"
        _logger.info("Loged in %s.", request.data)
        return Response(data)


class UserViewSet(ModelViewSet):
    """
    user api endpoint
    """

    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ("mobile", "party")
    logger = _logger
    throttle_classes = [OTPMinuteRateThrottle, OTPHourRateThrottle]

    def update(self, request, *args, **kwargs):
        """
        user can only update his instance
        """
        instance = self.get_object()
        if not request.user.is_authenticated or instance != request.user:
            return Response(
                {"error": "Permission Denied"}, status=status.HTTP_400_BAD_REQUEST
            )
        return super().update(request, args, kwargs)

    def destroy(self, request, *args, **kwargs):
        """
        set user active=false on user delete
        """
        instance = self.get_object()
        if not request.user.is_authenticated or instance != request.user:
            return Response(
                {"error": "Permission Denied"}, status=status.HTTP_400_BAD_REQUEST
            )
        instance.is_active = False
        instance.save()

        return super().update(request, args, kwargs)


class ChangePasswordView(generics.UpdateAPIView):
    """
    change user password
    """

    queryset = User.objects.all()
    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        """
        return user instance
        """
        return self.request.user


class VoteViewSet(ModelViewSet):
    """
    vote api endpoint
    """

    queryset = Vote.objects.all()
    serializer_class = Vote
    permission_classes = [permissions.IsAuthenticated]
    logger = _logger
