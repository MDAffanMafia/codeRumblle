# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
    #  myapp/models.py
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class ExampleModel(DjangoCassandraModel):
        example_id   = columns.UUID(primary_key=True, default=uuid.uuid4)
        example_type = columns.Integer(index=True)
        created_at   = columns.DateTime()
        description  = columns.Text(required=False)

#login classs
class User(DjangoCassandraModel):
        user_id=columns.UUID(primary_key=True,default=uuid.uuid4)
        username=columns.Text(required=True)
        password=columns.Text(required=True)
        wins=columns.Integer()
        matches=columns.Integer()
        rank=columns.Integer()
                

class Questions(DjangoCassandraModel):
        question_id=columns.UUID(primary_key=True,default=uuid.uuid4)
        question_name=columns.Text(required=True)
        difficulty=columns.Text(required=True) 
        link=columns.Bytes(required=True) 
        noOfUsersAttemp=columns.Integer(default=0)
        noOFUsersAccept=columns.Integer(default=0) 
class Questions1(DjangoCassandraModel):
        question_id=columns.UUID(primary_key=True,default=uuid.uuid4)
        question_name=columns.Text(required=True)
        difficulty=columns.Text(required=True) 
        link=columns.Text(required=True) 
class Questions2(DjangoCassandraModel):
        question_id=columns.UUID(primary_key=True,default=uuid.uuid4)
        question_name=columns.Text(required=True)
        difficulty=columns.Text(required=True) 
        link=columns.Text(required=True)         
              
              
