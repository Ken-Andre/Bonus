import jpype
import os
jpype.startJVM()
from asposecells.api import Workbook

base_path = "../"
init = 0  # Commencer à partir de X1_promo_list.xlsx

for counter in range(init, init+5):
    xlsx_path = f"{base_path}X{counter}_promo_list.xlsx"
    json_path = f"X{counter}_promo_list.json"

    try:
        workbook = Workbook(xlsx_path)
        workbook.save(json_path)
    except Exception as e:
        print(f"X{counter}_promo_list.xlsx didn't exist. Error: {e}")

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
