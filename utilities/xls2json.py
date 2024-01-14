import jpype
import json
jpype.startJVM()
from asposecells.api import Workbook

base_path = "../"
init = 1  # Commencer à partir de X1_promo_list.xlsx

for counter in range(init, init+5):
    xlsx_path = f"{base_path}X{counter}_promo_list.xlsx"
    json_path = f"X{counter}_promo_list.json"

    try:
        workbook = Workbook(xlsx_path)
        workbook.save(json_path)
    except Exception as e:
        print(f"X{counter}_promo_list.xlsx didn't exist. Error: {e}")

    input_file_path = f"X{counter}_promo_list.json"
    output_file_path = f"X{counter}_etudiant.json"

    with open(input_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    # Transformation pour remplir les valeurs manquantes avec une chaîne vide
    transformed_data = [
        {
            "_id": {"$oid": ""},
            "matricule": student.get("Matricule", ""),
            "admissionNumber": 0,
            "promotion": f"X202{counter}",  # Remplacez avec la vraie année si nécessaire
            "nom": student.get("Nom", ""),
            "prenom": student.get("Prénom", ""),
            "campus": student.get("Campus", ""),
            "email": student.get("Email", ""),
            "nationalite": "",
            "sexe": "",
            "active": False,
            "createdAt": {"$date": {"$numberLong": "0"}},
            "updatedAt": {"$date": {"$numberLong": "0"}},
            "createdBy": "",
            "updatedBy": "",
            "_class": "com.kychas.groupemanagement.models.Student"
        }
        for student in data
    ]

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(transformed_data, output_file, indent=2)

    print(f"Transformed {input_file_path} and saved to {output_file_path}")

jpype.shutdownJVM()
# import jpype
# import asposecells
# jpype.startJVM()
# from asposecells.api import Workbook
#
# # Create an instance of the Workbook class.
# workbook = Workbook()
#
# # Insert the words Hello World! into a cell accessed.
# workbook.getWorksheets().get(0).getCells().get("A1").putValue("Hello World")
#
# # Save as XLS file
# workbook.save("output.xls")
#
# # Save as XLSX file
# workbook.save("output.xlsx")
#
# # Save as ods file
# workbook.save("output.json")
#
# jpype.shutdownJVM()
