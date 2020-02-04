from django.conf import settings
from graphene_django import DjangoObjectType
import graphene
from .models import Room, Player


class RoomType(DjangoObjectType):

    class Meta:
        model = Room
        interfaces = (graphene.relay.Node,)


class PlayerType(DjangoObjectType):

    class Meta:
        model = Player
        interfaces = (graphene.relay.Node)


class Query(graphene.ObjectType):

    rooms = graphene.List(RoomType)
    players = graphene.List(PlayerType)

    def resolve_rooms(self, info):
        return Room.Objects.all()

    def resolve_players(self, info):
        return Player.Objects.all()


schema = graphene.Schema(query=Query)
