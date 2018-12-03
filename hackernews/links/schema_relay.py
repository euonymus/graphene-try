import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Link, Vote

# graphene-django:      https://github.com/graphql-python/graphene-django/blob/master/docs/filtering.rst
class LinkNode(DjangoObjectType):
    class Meta:
        model = Link
        filter_fields = ['url', 'description']
        interfaces = (graphene.relay.Node, )

# django-filter 1.1.0:  https://django-filter.readthedocs.io/en/1.1.0/guide/usage.html#the-filter
class LinkFilter(django_filters.FilterSet):
    # filter types: https://docs.djangoproject.com/en/dev/ref/models/querysets/#field-lookups
    # Do case-insensitive lookups on 'url'
    url = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Link
        fields = ['url', 'description']

class VoteNode(DjangoObjectType):
    class Meta:
        model = Vote
        interfaces = (graphene.relay.Node,)

class RelayQuery(graphene.ObjectType):
    relay_link = graphene.relay.Node.Field(LinkNode)
    relay_links = DjangoFilterConnectionField(LinkNode, filterset_class=LinkFilter)





class RelayCreateLink(graphene.relay.ClientIDMutation):
    link = graphene.Field(LinkNode)

    class Input:
        url = graphene.String()
        description = graphene.String()

    def mutate_and_get_payload(root, info, **input):
        user = info.context.user or None

        link = Link(
            url=input.get('url'),
            description=input.get('description'),
            posted_by=user,
        )
        link.save()

        return RelayCreateLink(link=link)

class RelayMutation(graphene.AbstractType):
    relay_create_link = RelayCreateLink.Field()
