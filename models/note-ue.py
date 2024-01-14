from typing import List
from pydantic import BaseModel

class Evaluation(BaseModel):
    evalname: str
    credit: int
    code: str

class NoteEvaluation(BaseModel):
    evaluation: Evaluation
    note: str

class NoteTeachingUnit(BaseModel):
    _id: dict
    ueName: str
    academicYear: str
    student: str
    level: int
    noteEvaluations: List[NoteEvaluation]
    archived: bool
    createdAt: dict
    updatedAt: dict
    createdBy: str
    updatedBy: str
    _class: str


