from typing import List
from pydantic import BaseModel


class Etudiant(BaseModel):
    # _id: dict
    matricule: str
    admissionNumber: int
    promotion: str
    nom: str
    prenom: str
    campus: str
    email: str
    nationalite: str
    sexe: str
    active: bool
    createdAt: dict
    updatedAt: dict
    createdBy: str
    updatedBy: str
    _class: str


class EtudiantsList(BaseModel):
    students: List[Etudiant]
