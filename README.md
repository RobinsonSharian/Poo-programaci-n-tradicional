# Sistema de Gestión de Mascotas - Comparación de Enfoques

**Estudiante:** [ROBINSON ENRIQUE SHARIAN PINCHU]  
**Asignatura:** Programación Orientada a Objetos  
**Semana:** 3  

---

## 📝 Descripción de los Programas

1. **Programación Tradicional (`programacion_traditional/`):** Se desarrolló una solución estructurada que hace uso exclusivo de variables locales, estructuras de datos nativas (diccionarios) y funciones procedimentales secuenciales para capturar por teclado y mostrar los datos de una mascota sin persistencia ni abstracción formal de entidades.

2. **Programación Orientada a Objetos (`programacion_poo/`):** Se diseñó una arquitectura modular dividida en una plantilla lógica (`Mascota`) que encapsula las propiedades (`nombre`, `especie`, `edad`) y comportamientos (`mostrar_informacion()`, `hacer_sonido()`). El archivo de ejecución `main.py` actúa como el cliente que instancia múltiples objetos independientes de dicha clase.

---

## 🔍 Reflexión del Aprendizaje: Diferencias entre Programación Tradicional y POO

* **Organización y Estructura del Código:** En la programación tradicional, el código se enfoca en los pasos lógicos y las funciones operan directamente pasando los datos de un lado a otro. En cambio, la POO agrupa orgánicamente los datos (atributos) y el comportamiento (métodos) en un solo bloque conceptual llamado clase, facilitando el orden visual.
* **Gestión de la Información y Escalabilidad:** Con el enfoque tradicional, si quisiéramos manejar 100 mascotas de forma independiente, tendríamos que lidiar de manera compleja con matrices o listas de diccionarios, aumentando el riesgo de mutar datos por error. En la POO, cada mascota es una instancia de objeto totalmente aislada, autónoma y segura que retiene su propio estado.
* **Abstracción y Reutilización:** La POO permite modelar el software simulando elementos reales del mundo. Al separar la lógica en `mascota.py` y el flujo en `main.py`, se consigue un código altamente reutilizable y fácil de mantener si en el futuro se requiriera agregar características complejas (como herencia para tipos específicos de animales).