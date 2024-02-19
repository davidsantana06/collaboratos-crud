from datetime import datetime
from flask_sqlalchemy.model import Model
from flask_wtf import FlaskForm
from re import findall
from sqlalchemy import (
    Column, ColumnElement, DateTime, Float, Integer, String, UnaryExpression,
    and_
)
from sqlalchemy.ext.declarative import declared_attr
from typing import List

from .extensions import database


# BASES/MIXINS #

class _Entity(Model):
    @declared_attr
    def __tablename__(cls):
        cls_name_words = findall(r'[A-Z][a-z]*', cls.__name__)
        table_name = '_'.join(cls_name_words).lower()
        return table_name
    
    @declared_attr
    def created_at(cls):
        return Column(DateTime(True), nullable=False, default=datetime.now())

    @declared_attr
    def updated_at(cls):
        return Column(DateTime(True), nullable=False, default=datetime.now(), onupdate=datetime.now())

    @staticmethod
    def save(entity: '_Entity') -> None:
        try:
            database.session.add(entity)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _find_first(cls, filter_clauses: List[ColumnElement[bool]]) -> '_Entity':
        return cls.query.filter(and_(*filter_clauses)).first()

    @classmethod
    def _find_all(cls, filter_clauses: List[ColumnElement[bool]] = [], group_clauses: List[UnaryExpression] = [], order_clauses: List[UnaryExpression] = []) -> List['_Entity']:
        query = cls.query.filter(and_(*filter_clauses))

        if group_clauses:
            query = query.group_by(*group_clauses)

        if order_clauses:
            query = query.order_by(*order_clauses)

        return query.all()


class _DeletableEntity(_Entity):
    @declared_attr
    def status(cls):
        return Column(Integer, nullable=False, default=1)

    @staticmethod
    def delete(entity: '_DeletableEntity') -> None:
        try:
            entity.status = 0
            database.session.add(entity)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @classmethod
    def _find_first(cls, filter_clauses: List[ColumnElement[bool]]) -> '_DeletableEntity':
        return super()._find_first([*filter_clauses, cls.status == 1])

    @classmethod
    def _find_all(cls, filter_clauses: List[ColumnElement[bool]] = [], group_clauses: List[UnaryExpression] = [], order_clauses: List[UnaryExpression] = []) -> List['_DeletableEntity']:
        return super()._find_all([*filter_clauses, cls.status == 1], group_clauses, order_clauses)


class _PopulateMixin:
    def populate_form(self, form: FlaskForm) -> None:
        for field in form:
            if hasattr(self, field.name):
                field.data = getattr(self, field.name)

    def populate_obj(self, obj: object) -> None:
        for attr in obj.__dict__:
            if hasattr(self, attr):
                value = getattr(self, attr)
                setattr(obj, attr, value)


# MODELS #

class Collaborator(database.Model, _DeletableEntity, _PopulateMixin):
    id = Column(Integer(), autoincrement=True, unique=True, nullable=False, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    participation = Column(Float(1), nullable=False)

    def __init__(self, first_name: str, last_name: str, participation: float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.participation = participation

    @staticmethod
    def save(collaborator: 'Collaborator') -> None:
        _DeletableEntity.save(collaborator)

    @staticmethod
    def delete(collaborator: 'Collaborator') -> None:
        _DeletableEntity.delete(collaborator)

    @classmethod
    def find_all(cls) -> List['Collaborator']:
        return cls._find_all(order_clauses=[cls.created_at])
