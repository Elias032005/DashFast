# DashFast Business Intelligence

Módulo personalizado para Odoo orientado a la gestión y análisis de datos empresariales dentro del proyecto **DashFast**.

## Descripción

Este módulo ha sido desarrollado como parte de un proyecto académico centrado en:

- modelado de datos en Odoo
- creación de modelos personalizados con Python
- definición de vistas XML
- organización de menús y acciones
- preparación de datos para análisis posterior en herramientas de Business Intelligence

La idea principal del módulo es registrar información interna de la empresa de forma estructurada para después poder explotarla y analizarla.

## ¿Para qué sirve un módulo personalizado en Odoo?

Un módulo personalizado permite ampliar Odoo con funcionalidades propias sin modificar directamente los módulos estándar del sistema.

En este caso, el módulo se utiliza para:

- crear modelos de datos adaptados al proyecto
- registrar departamentos, métricas y KPIs
- relacionar información entre modelos
- visualizar los datos desde la interfaz de Odoo
- preparar una base estructurada para futuros análisis

## Funcionalidades principales

Actualmente el módulo incluye:

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