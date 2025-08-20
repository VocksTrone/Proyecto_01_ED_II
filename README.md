# Proyecto 01 - Plataforma de Servicios Locales con Árbol B  

## 📚 Descripción del Proyecto  

Este software educativo ha sido desarrollado como parte del curso **Estructura de Datos II** de la carrera de Ingeniería en Informática y Sistemas.  
Su objetivo es **simular una plataforma de contratación de servicios locales**, en la cual se registran y organizan proveedores utilizando un **Árbol B** para realizar búsquedas eficientes y ordenadas.  

## 🧠 Funcionalidades Principales  

- Registrar proveedores de servicios con:  
  - ID único generado automáticamente  
  - Nombre  
  - Tipo de servicio  
  - Calificación inicial  
- Buscar proveedores por tipo de servicio.  
- Contratar proveedores y actualizar su calificación en tiempo real.  
- Mostrar todos los proveedores registrados.  
- Clasificación **Top 5 Global** y **Top 5 por Servicio**.  

## 🧱 Organización del Proyecto  

| Archivo       | Descripción |
|---------------|-------------|
| `main.py`     | Archivo principal, contiene el menú y la lógica del programa. |
| `btree.py`    | Implementación del Árbol B con inserciones y búsquedas. |
| `node.py`     | Clase `Node`, usada como base para la estructura del Árbol B. |
| `provider.py` | Clase `Provider` con los datos del proveedor y sistema de calificación en estrellas. |
| `mensajes.py` | Mensajes y colores para la interfaz en consola. |

## 🖥️ Menú Principal  

1. Registrar Proveedor  
2. Buscar Servicio  
3. Mostrar Proveedores  
4. Clasificación Top 5 Proveedores  
5. Salir  

## ⚙️ Tecnologías Utilizadas  

- **Lenguaje**: Python 3.13 
- **Paradigma**: Programación Orientada a Objetos  
- **Estructura de datos**: Árbol B  
- **Interfaz**: Consola con colores ANSI  

## 🧑‍🤝‍🧑 Equipo de Desarrollo
- Granados de León, Luis Oswaldo - 1506124
- Ramirez Alvarez, Javier Estuardo - 1647124
- Santay Matías, Mily Angélica Virginia - 1507624