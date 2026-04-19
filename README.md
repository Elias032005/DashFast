# DashFast Business Intelligence

Módulo personalizado para Odoo orientado a la gestión y análisis de datos empresariales dentro de mi proyecto **DashFast**.

## Descripción

He desarrollado este módulo como parte de un proyecto académico centrado en:

- modelado de datos en Odoo
- creación de modelos personalizados con Python
- definición de vistas XML
- organización de menús y acciones
- preparación de datos para análisis posterior en herramientas de Business Intelligence

La idea principal de este módulo es registrar información interna de la empresa de forma estructurada para después poder explotarla y analizarla.

## ¿Para qué sirve un módulo personalizado en Odoo?

Un módulo personalizado permite ampliar Odoo con funcionalidades propias sin modificar directamente los módulos estándar del sistema.

En este caso, utilizo el módulo para:

- crear modelos de datos adaptados a mi proyecto
- registrar departamentos, métricas y KPIs
- relacionar información entre modelos
- visualizar los datos desde la interfaz de Odoo
- preparar una base estructurada para futuros análisis

## Funcionalidades principales

Actualmente, el módulo incluye:

- modelo de **Departamentos**
- modelo de **KPIs de empleados**
- modelo de **Métricas de empresa**
- relaciones entre modelos
- vistas `tree`, `form` y `search`
- acciones y menús personalizados dentro de Odoo

## Modelos incluidos

### `df.department`
Representa los departamentos de la empresa.

Campos principales:
- `code` → identificador
- `name` → nombre
- `date` → fecha
- `value` → valor numérico

Relaciones:
- `employee_kpis_ids` → relación `One2many` con `df.employee_kpi`

---

### `df.employee_kpi`
Representa indicadores o KPIs asociados a empleados.

Campos principales:
- `code`
- `name`
- `date`
- `value`

Relaciones:
- `department_id` → relación `Many2one` con `df.department`

---

### `df.company_metric`
Representa métricas generales de empresa.

Campos principales:
- `code`
- `name`
- `date`
- `value`

Relaciones:
- `company_id` → relación `Many2one` con `res.company`

## Decisión de estructura

Aunque Odoo permite concentrar parte del desarrollo en menos archivos, en este proyecto he optado por separar los modelos Python y las vistas XML por bloques funcionales.

He tomado esta decisión de forma consciente con un objetivo principalmente didáctico y organizativo. Al tratarse de mi primer desarrollo de módulos personalizados en Odoo, he preferido trabajar con una estructura más clara y mantenible, que me permita identificar con facilidad qué lógica pertenece a cada modelo y qué vistas corresponden a cada uno de ellos.

Por ello, he seguido una organización basada en:

- un archivo `.py` por modelo
- un archivo `.xml` por modelo o conjunto de vistas asociado

Este enfoque me facilita:

- comprender mejor el módulo
- localizar errores más rápido
- mantener el código de forma más ordenada
- ampliar el proyecto en el futuro con una base más clara

Soy consciente de que en módulos pequeños podría agruparse más contenido en menos archivos, pero en este caso he preferido una estructura más ordenada para reforzar mi aprendizaje y trabajar con una base más limpia y escalable.

## Estructura del proyecto

```bash
dashfast_business_intelligence/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── department.py
│   ├── employee_kpi.py
│   └── company_metric.py
├── security/
│   └── ir.model.access.csv
└── views/
    ├── department.xml
    ├── employee_kpi.xml
    └── company_metric.xml