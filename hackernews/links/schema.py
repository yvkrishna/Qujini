import graphene
from graphene_django import DjangoObjectType
from .models import Link

class LinkType(DjangoObjectType):
    class Meta:
        model=Link   

class Query(graphene.ObjectType):
    links=graphene.List(LinkType)

    def resolve_links(self,info,**kwargs):
        return Link.objects.all()

class CreateLink(graphene.Mutation):
    id=graphene.Int()
    url=graphene.String()
    discription=graphene.String()

    class Arguments:
        url = graphene.String()
        discription = graphene.String()

    def mutate(self, info, url, discription):
        link = Link(url=url, discription=discription)
        link.save()

        return CreateLink(
            id=link.id,
            url=link.url,
            discription=link.discription,
        )

class Mutation(graphene.ObjectType):
    Create_Link=CreateLink.Field()
