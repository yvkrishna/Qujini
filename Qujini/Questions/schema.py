
import graphene
from graphene_django import DjangoObjectType
from django.contrib.auth.models import User
from .models import Question,Type,Topic,Question_Bank

# class MakeNewUser(graphene.ObjectType):

class QType(DjangoObjectType):
    class Meta:
        model=Question

class QTypesType(DjangoObjectType):
    class Meta:
        model=Type

class QTopicsType(DjangoObjectType):
    class Meta:
        model=Topic

class QBank(DjangoObjectType):
    class Meta:
        model=Question_Bank

class Query(graphene.ObjectType):
    Questions=graphene.List(QType)
    question_get=graphene.Field(QBank,question=graphene.String()
                                 ,min_mark=graphene.Int()
                                 ,max_mark=graphene.Int()
                                 ,difficulty=graphene.String()
                                 ,questionType=graphene.String()
                                 ,topic=graphene.String())

    def resolve_Questions(self, info, **kwargs):
        return Question.objects.all()
    
    def resolve_question_get(self, info, **kwargs):
        min_mark=kwargs.get('min_mark')
        max_mark=kwargs.get('max_mark')
        difficulty=kwargs.get('difficulty')
        questionType=kwargs.get('questionType')
        topic=kwargs.get('topic')

        if  min_mark is not None and max_mark is not None and difficulty is not None and questionType is not None and topic is not None:
            a=Question_Bank.objects.filter(question_type__name=questionType)[0]
            b=a.question_topic.filter()[0]
            return Question_Bank.objects.filter(min_mark=min_mark,max_mark=max_mark,difficulty=difficulty,question_type=a.question_type,question_topic=b).all()
        
        return None


class MakeQuestionPaper(graphene.Mutation):
    author=graphene.String()
    difficulty=graphene.String()
    min_marks=graphene.Int()
    max_marks=graphene.Int()
    date=graphene.types.datetime.Date()
    topic=graphene.String()
    type=graphene.String()
    question=graphene.String()

    class Arguments:
        author=graphene.String()
        difficulty=graphene.String()
        min_marks=graphene.Int()
        max_marks=graphene.Int()
        date=graphene.types.datetime.Date()
        topic=graphene.String()
        type=graphene.String()
        question=graphene.String()  
        
    def mutate(self, info,author, difficulty, min_marks, max_marks, date, topic, type):
        cnt1=0
        a=User.objects.get(username=author)
        tt=Topic(name=topic)
        tt.save()
        cnt1=len(Type.objects.filter(name=type))
        if cnt1==0:
            t=Type(name=type)
            t.save()
        typ=Type.objects.get(name=type)
        q=Question.objects.create(author=a,difficulty=difficulty,min_marks=min_marks,max_marks=max_marks,date=date, questionType=typ)
        q.save()
        q.topic.add(tt)
        
        return MakeQuestionPaper(author=a,difficulty=difficulty,min_marks=min_marks,max_marks=max_marks,date=date, type=typ ,topic=topic)

class Mutation(graphene.ObjectType):
    create_questionpaper = MakeQuestionPaper.Field()