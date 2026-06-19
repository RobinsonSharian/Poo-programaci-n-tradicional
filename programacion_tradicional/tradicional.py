# =====================================================================
# PROGRAMA 1: PROGRAMACIÓN TRADICIONAL (ESTRUCTURADA)
# Asignatura: Programación Orientada a Objetos - Semana 3
# =====================================================================

def registrar_mascota():
    """Función para solicitar los datos de la mascota mediante teclado."""
    print("--- Registro de Nueva Mascota ---")
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (ej. Perro, Gato): ")
    
    # Validación básica de edad
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota: "))
            if edad >= 0:
                break
            print("La edad no puede ser negativa.")
        except ValueError:
            print("Por favor, ingrese un número entero válido para la edad.")
            
    # Retornamos los datos estructurados en un diccionario tradicional
    return {"nombre": nombre, "especie": especie, "edad": edad}


def mostrar_mascota(mascota):
    """Función para mostrar la información registrada de forma organizada."""
    print("\n=================================")
    print("     INFORMACIÓN DE LA MASCOTA   ")
    print("=================================")
    print(f"Nombre:  {mascota['nombre']}")
    print(f"Especie: {mascota['especie']}")
    print(f"Edad:    {mascota['edad']} años")
    print("=================================\n")


def main():
    """Función principal para controlar el flujo de la aplicación."""
    # Registro de la mascota
    datos_mascota = registrar_mascota()
    # Despliegue de la información
    mostrar_mascota(datos_mascota)


# Punto de entrada del programa tradicional
if __name__ == "__main__":
    main()