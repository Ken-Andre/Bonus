from typing import List, Optional
from pydantic import BaseModel, Field


class Metadata(BaseModel):
    created: dict
    updated: dict
    _class: str


class Etudiant(BaseModel):
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
    metadata: Metadata


class EtudiantsList(BaseModel):
    students: List[Etudiant]
