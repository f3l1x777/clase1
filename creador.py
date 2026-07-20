import os
from datetime import datetime

# 1. Obtener la fecha de hoy con un formato bonito (Año-Mes-Día)
fecha_hoy = datetime.now().strftime("%Y-%m-%d")

# 2. Definir el nombre de la carpeta principal del día
carpeta_del_día = "Trabajo_" + fecha_hoy

print("Iniciando el script de automatización...")

# 3. Comprobar si la carpeta ya existe. Si no, la crea.
if not os.path.exists(carpeta_del_día):
    os.mkdir(carpeta_del_día)
    print("¡Carpeta principal '" + carpeta_del_día + "' creada con éxito!")
    
    # 4. Crear subcarpetas organizadas dentro de la carpeta del día
    subcarpetas = ["documentos", "imagenes", "codigos"]
    for sub in subcarpetas:
        ruta_subcarpeta = os.path.join(carpeta_del_día, sub)
        os.mkdir(ruta_subcarpeta)
        print("  -> Subcarpeta '" + sub + "' creada.")
        
    print("\n¡Estructura de hoy organizada perfectamente!")
else:
    print("Aviso: La carpeta de hoy ya existía. No se hizo ningún cambio.")

