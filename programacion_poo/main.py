# =====================================================================
# PROGRAMA 2: PROGRAMACIÓN ORIENTADA A OBJETOS
# Archivo principal de ejecución (Orquestador)
# =====================================================================
from mascota import Mascota

def main():
    print("==================================================")
    print("    SISTEMA DE GESTIÓN DE MASCOTAS (ENFOQUE POO)  ")
    print("==================================================\n")
    
    # El requerimiento pide crear al menos DOS objetos de la clase Mascota
    # Instanciación del Objeto 1
    mascota1 = Mascota("Max", "Perro", 3)
    
    # Instanciación del Objeto 2
    mascota2 = Mascota("Luna", "Gato", 2)
    
    # Instanciación de un Objeto 3 opcional para robustecer el ejemplo
    mascota3 = Mascota("Paco", "Loro", 1)

    # Ejecución de los métodos definidos para mostrar la información
    print("--- Listado de Objetos Instanciados ---")
    mascota1.mostrar_informacion()
    mascota2.mostrar_informacion()
    mascota3.mostrar_informacion()
    
    print("\n--- Demostración de Métodos de Comportamiento (hacer_sonido) ---")
    print(f"{mascota1.nombre} dice: {mascota1.hacer_sonido()}")
    print(f"{mascota2.nombre} dice: {mascota2.hacer_sonido()}")
    print(f"{mascota3.nombre} dice: {mascota3.hacer_sonido()}")
    print("\n==================================================")

if __name__ == "__main__":
    main()