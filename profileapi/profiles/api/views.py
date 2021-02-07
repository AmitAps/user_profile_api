# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from profiles.models import Profile
# from profiles.api.serializers import ProfileSerializer
#
#
# class ProfileList(generics.ListAPIView):
#     """
#     https://www.django-rest-framework.org/api-guide/generic-views/
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]




# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.viewsets import ReadOnlyModelViewSet
# from profiles.models import Profile
# from profiles.api.serializers import ProfileSerializer
#
#
# class ProfileViewSet(ReadOnlyModelViewSet):
#     """
#     https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
#     """
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]


#working with mixins

from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
#https://www.django-rest-framework.org/api-guide/filtering/
from rest_framework.viewsets import ModelViewSet

from profiles.models import Profile, ProfileStatus
from profiles.api.permissions import IsOwnProfileOrReadOnly, IsOwnerOrReadOnly
from profiles.api.serializers import ProfileSerializer, ProfileStatusSerializer, ProfileAvatarSerializer



class AvatarUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProfileAvatarSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        profile_object = self.request.user.profile
        return profile_object




class ProfileViewSet(mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    https://www.django-rest-framework.org/api-guide/viewsets/#genericviewset
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated, IsOwnProfileOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['city']


class ProfileStatusViewSet(ModelViewSet):
    serializer_class = ProfileStatusSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        queryset = ProfileStatus.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        return queryset


    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)
