========================================================
|                ESTRUCTURA DE COMMITS                 |
========================================================

                    < TIPOS DE TASK >

    Add       = Nueva funcionalidad
    Fix       = Corrección de errores
    Update    = Modificación/mejora
    Remove    = Eliminación de código
    Refactor  = Reestructuración interna/mejorar código sin cambiar funcionalidad
    Docs      = Documentación
    Config    = Configuración del proyecto
    Test      = Testing y pruebas

========================================================
|                     BACKEND                          |
========================================================

Task-001  -> Task-399
|
|-- Ejemplos:
|
|   Task-001: Add: implementar sistema login
|   Task-002: Fix: corregir validación JWT
|   Task-003: Refactor: optimizar controlador usuarios
|   Task-004: Remove: eliminar middleware antiguo
|
`-- Área:
    API | DB | Auth | Controllers | Models


========================================================
|                     FRONTEND                         |
========================================================

Task-401  -> Task-799
|
|-- Ejemplos:
|
|   Task-401: Add: crear componente navbar
|   Task-402: Fix: corregir responsive dashboard
|   Task-403: Style: mejorar diseño login
|   Task-404: Refactor: reorganizar componentes React
|
`-- Área:
    UI | UX | React | Vite | CSS | Tailwind


========================================================
|            GENERAL / DEVOPS / EXTRAS                |
========================================================

Task-1001 -> ∞
|
|-- Ejemplos:
|
|   Task-1001: Docs: agregar README instalación
|   Task-1002: Config: configurar ESLint
|   Task-1003: Add: añadir archivo tareas.txt
|   Task-1004: Test: crear pruebas backend
|
`-- Área:
    GitHub | Deploy | Docker | Docs | Configuración


========================================================
|                 FORMATO OFICIAL                      |
========================================================

Task-XXX: Tipo: descripción corta

|
|-- Ejemplos válidos:
|
|   Task-015: Fix: corregir expiración de sesión
|   Task-220: Add: crear sidebar admin
|   Task-1050: Docs: actualizar documentación API
|
`-- Reglas:
    - Descripciones cortas y claras
    - Un commit = una tarea
    - Mantener consistencia
    - No usar commits tipo:
      "arreglos"
      "cosas nuevas"
      "asd"
      "final_final_ahora_si"
    -No comiteen como botardos.
