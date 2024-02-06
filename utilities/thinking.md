#etudiants.json


    _id: Un identifiant unique pour l'étudiant.
    matricule: Le matricule de l'étudiant.
    admissionNumber: Le numéro d'admission de l'étudiant.
    promotion: La promotion à laquelle l'étudiant appartient.
    nom et prenom: Le nom et le prénom de l'étudiant.
    campus: Le campus où l'étudiant est inscrit.
    email: L'adresse e-mail de l'étudiant.
    nationalite:La nationalité de l'étudiant.
    sexe: le sexe de l'étudiant.
    active: Un indicateur de statut actif pour l'étudiant.
    createdAt et updatedAt: Les horodatages de création et de mise à jour de l'enregistrement.
    createdBy et updatedBy: Les personnes qui ont créé et mis à jour l'enregistrement.

#note-ue.json

    _id: Un identifiant unique pour la note d'UE.
    ueName: Le nom de l'unité d'enseignement.
    academicYear: L'année académique à laquelle la note est associée.
    student: Le numéro d'admission de l'étudiant associé à cette note d'UE.
    level: Le niveau de l'étudiant.
    noteEvaluations: Une liste d'objets représentant les évaluations de la note d'UE de l'etudiant, chacun comprenant une évaluation, comprenant son nom, son crédit et son code, ainsi que la note obtenue.
    archived: Un indicateur indiquant si la note d'UE est archivée.
    createdAt et updatedAt: Les horodatages de création et de mise à jour de l'enregistrement.
    createdBy et updatedBy: Les personnes qui ont créé et mis à jour l'enregistrement.

si un étudiant est supprimé dans le fichier etudiants.json, mettre à jour ou supprimer toutes les références à cet étudiant dans le fichier note-ue.json pour éviter des incohérences.

#Propositions
    juste inclure l'object_id l'etudiant