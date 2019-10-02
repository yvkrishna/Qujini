import graphene
import Questions.schema

class Mutation(Questions.schema.Mutation,graphene.ObjectType):
    pass

class Query(Questions.schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)