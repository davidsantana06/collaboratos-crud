from typing import List
from app.models import Collaborator


def validate_collaborator_participation(participation: float) -> bool:
    return participation <= 100 - sum(c.participation for c in Collaborator.find_all())


def find_all_collaboratos() -> List[Collaborator]:
    return Collaborator.find_all()


def find_collaborator_by_id(collaborator_id: int) -> Collaborator:
    return Collaborator.find_by_id(collaborator_id)


def create_collaborator(first_name: str, last_name: str, participation: float) -> None:
    collaborator = Collaborator(first_name, last_name, participation)
    Collaborator.save(collaborator)


def delete_collaborator(collaborator: Collaborator) -> None:
    Collaborator.delete(collaborator)
