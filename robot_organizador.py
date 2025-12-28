import os
import shutil

ruta = os.path.expanduser("~/Downloads")
os.chdir(ruta)

for archivo in os.listdir():
    if archivo.endswith(".pdf"):
        os.makedirs("Mis_Documentos", exist_ok=True)
        shutil.move(archivo, "Mis_Documentos")
        # comment: 
    # end if
# end for