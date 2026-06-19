# =====================================================================
# CLASE MASCOTA (ABSTRACCIÓN Y ENCAPSULAMIENTO)
# =====================================================================

class Mascota:
    """Clase que representa la plantilla abstracta de una Mascota."""
    
    def __init__(self, nombre, especie, edad):
        """Método constructor para inicializar los atributos de la clase."""
        self.nombre = nombre       # Atributo: nombre
        self.especie = especie     # Atributo: especie
        self.edad = edad           # Atributo: edad

    def mostrar_informacion(self):
        """Método para imprimir de forma organizada los atributos del objeto."""
        print(f"🐾 Nombre: {self.nombre:<12} | Especie: {self.especie:<10} | Edad: {self.edad} años")

    def hacer_sonido(self):
        """Método dinámico para simular el comportamiento o sonido de la mascota."""
        especie_clean = self.especie.lower().strip()
        if "perro" in especie_clean:
            return "¡Guau, guau!"
        elif "gato" in especie_clean:
            return "¡Miau, miau!"
        elif "loro" in especie_clean or "pajaro" in especie_clean:
            return "¡Cri-cri / Hola!"
        else:
            return "*(Sonido de mascota desconocido)*"