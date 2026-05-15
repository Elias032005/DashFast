# DashFast Business Intelligence

**DashFast Business Intelligence** es un módulo personalizado desarrollado sobre **Odoo** cuyo objetivo es facilitar la gestión, automatización y preparación de datos empresariales para su posterior análisis mediante herramientas de **Business Intelligence**, especialmente **Power BI**.

Este proyecto forma parte de un desarrollo académico orientado a demostrar cómo una empresa puede pasar de tener datos repartidos o poco explotados a disponer de una base organizada, consultable y preparada para generar informes visuales.

---

## Índice

- [Descripción del proyecto](#descripción-del-proyecto)
- [Problema que resuelve](#problema-que-resuelve)
- [Objetivo del proyecto](#objetivo-del-proyecto)
- [Funcionamiento general](#funcionamiento-general)
- [Funcionalidades principales](#funcionalidades-principales)
- [Tecnologías utilizadas](#tecnologías-utilizadas)
- [Modelos de datos incluidos](#modelos-de-datos-incluidos)
- [Formulario web personalizado](#formulario-web-personalizado)
- [Automatización de consultas SQL](#automatización-de-consultas-sql)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Explicación de carpetas y archivos](#explicación-de-carpetas-y-archivos)
- [Instalación con Docker Compose](#instalación-con-docker-compose)
- [Uso básico del módulo](#uso-básico-del-módulo)
- [Comandos útiles](#comandos-útiles)
- [Buenas prácticas del repositorio](#buenas-prácticas-del-repositorio)
- [Posibles mejoras futuras](#posibles-mejoras-futuras)
- [Estado del proyecto](#estado-del-proyecto)

---

## Descripción del proyecto

DashFast Business Intelligence es un módulo personalizado para Odoo diseñado para registrar, organizar y preparar información empresarial con el objetivo de facilitar su análisis posterior.

El proyecto combina diferentes partes:

- desarrollo de modelos personalizados en Odoo
- creación de vistas XML
- configuración de menús y acciones
- personalización del formulario web de Odoo
- uso de JavaScript para mejorar la interacción del formulario
- generación automática de consultas SQL mediante Python
- almacenamiento de consultas generadas
- preparación del entorno mediante Docker Compose
- enfoque final orientado a Business Intelligence y Power BI

La idea principal del proyecto es simular una solución real en la que una empresa pueda solicitar información concreta desde una interfaz sencilla y obtener como resultado una consulta SQL preparada para extraer datos desde la base de datos.

---

## Problema que resuelve

Muchas empresas generan datos diariamente:

- ventas
- compras
- clientes
- productos
- proveedores
- importes
- fechas
- departamentos
- métricas internas
- indicadores de rendimiento

Sin embargo, tener datos no significa necesariamente tener información útil.

En muchos casos, los datos están almacenados en sistemas internos, bases de datos o aplicaciones empresariales, pero no existe una forma sencilla para que una persona no técnica pueda consultarlos, prepararlos o analizarlos.

Algunos problemas habituales son:

- los datos no están organizados para análisis
- las consultas SQL se tienen que escribir manualmente
- los informes dependen de procesos repetitivos
- la información tarda en prepararse
- los usuarios no técnicos dependen de perfiles técnicos
- no existe una conexión clara entre la gestión interna y el análisis BI
- la toma de decisiones se realiza con información poco visual o poco actualizada

DashFast Business Intelligence intenta resolver este problema creando un flujo sencillo:

```text
Datos empresariales en Odoo
        ↓
Formulario web personalizado
        ↓
Selección de filtros por parte del usuario
        ↓
Generación automática de una consulta SQL
        ↓
Archivo SQL guardado en el sistema
        ↓
Preparación para análisis en Power BI
```

---

## Objetivo del proyecto

El objetivo principal de DashFast Business Intelligence es crear una base funcional que conecte la gestión empresarial con el análisis de datos.

A nivel académico, el proyecto demuestra conocimientos en:

- desarrollo de módulos personalizados en Odoo
- programación en Python
- diseño de modelos de datos
- relaciones entre modelos
- vistas XML
- control de permisos
- modificación de formularios web
- automatización de procesos
- generación de consultas SQL
- uso de Docker
- conexión con PostgreSQL
- preparación de datos para Power BI

A nivel funcional, el objetivo es facilitar que una empresa pueda transformar sus datos internos en información útil para la toma de decisiones.

---

## Funcionamiento general

El funcionamiento general del proyecto se puede resumir en el siguiente flujo:

```text
1. El usuario accede al formulario web de Odoo
        ↓
2. Introduce los datos necesarios para la consulta
        ↓
3. El formulario envía la información al módulo personalizado
        ↓
4. Python procesa los datos recibidos
        ↓
5. Se genera una consulta SQL personalizada
        ↓
6. La consulta se guarda como archivo .sql
        ↓
7. El archivo puede revisarse o utilizarse posteriormente
        ↓
8. Los datos resultantes pueden analizarse en Power BI
```

Este flujo permite automatizar parte del trabajo que normalmente se haría de forma manual.

---

## Funcionalidades principales

Actualmente, el proyecto incluye las siguientes funcionalidades:

### Gestión de datos internos en Odoo

- creación de modelos personalizados
- registro de departamentos
- registro de KPIs de empleados
- registro de métricas empresariales
- relaciones entre modelos
- vistas de tipo lista, formulario y búsqueda
- menús personalizados dentro de Odoo

### Personalización del formulario web

- modificación del formulario web estándar de Odoo
- inclusión de nuevos campos adaptados al proyecto
- envío de datos hacia lógica personalizada
- integración con JavaScript para mejorar la experiencia de usuario

### Automatización con Python

- lectura de los datos enviados desde el formulario
- validación básica de información recibida
- generación automática de consultas SQL
- creación de archivos `.sql`
- almacenamiento de consultas en una carpeta específica

### Preparación para Business Intelligence

- estructura de datos orientada a análisis
- consultas SQL reutilizables
- preparación de información para Power BI
- separación entre captura de datos, generación SQL y análisis visual

---

## Tecnologías utilizadas

El proyecto utiliza las siguientes tecnologías:

| Tecnología | Uso dentro del proyecto |
|----------|--------------------------|
| Odoo | ERP base sobre el que se desarrolla el módulo |
| Python | Desarrollo de modelos, lógica interna y generación SQL |
| XML | Definición de vistas, menús y modificación del formulario web |
| JavaScript | Comportamiento dinámico del formulario web |
| PostgreSQL | Base de datos utilizada por Odoo |
| Docker | Contenerización del entorno |
| Docker Compose | Orquestación de servicios |
| SQL | Consultas generadas para extracción de datos |
| Power BI | Herramienta objetivo para análisis y visualización |
| GitHub | Control de versiones y documentación del proyecto |

---

## Modelos de datos incluidos

El módulo incluye varios modelos personalizados que permiten registrar información empresarial dentro de Odoo.

---

### `df.department`

Representa los departamentos de una empresa.

Este modelo permite almacenar información básica relacionada con áreas internas de la organización.

Campos principales:

| Campo | Descripción |
|-----|-------------|
| `code` | Identificador interno del departamento |
| `name` | Nombre del departamento |
| `date` | Fecha asociada al registro |
| `value` | Valor numérico relacionado con el departamento |

Relaciones:

| Relación | Descripción |
|--------|-------------|
| `employee_kpis_ids` | Relación `One2many` con el modelo `df.employee_kpi` |

Ejemplo de uso:

```text
Departamento: Ventas
Código: VENT
Fecha: 06/05/2026
Valor: 150
```

---

### `df.employee_kpi`

Representa indicadores o KPIs asociados a empleados.

Este modelo permite registrar valores medibles relacionados con empleados o departamentos.

Campos principales:

| Campo | Descripción |
|-----|-------------|
| `code` | Código identificador del KPI |
| `name` | Nombre del indicador |
| `date` | Fecha del indicador |
| `value` | Valor numérico del indicador |

Relaciones:

| Relación | Descripción |
|--------|-------------|
| `department_id` | Relación `Many2one` con `df.department` |

Ejemplo de uso:

```text
KPI: Ventas realizadas
Departamento: Ventas
Valor: 35
Fecha: 06/05/2026
```

---

### `df.company_metric`

Representa métricas generales de empresa.

Este modelo está pensado para almacenar información más global, relacionada con la empresa en su conjunto.

Campos principales:

| Campo | Descripción |
|-----|-------------|
| `code` | Código de la métrica |
| `name` | Nombre de la métrica |
| `date` | Fecha de la métrica |
| `value` | Valor numérico de la métrica |

Relaciones:

| Relación | Descripción |
|--------|-------------|
| `company_id` | Relación `Many2one` con `res.company` |

Ejemplo de uso:

```text
Métrica: Facturación mensual
Empresa: DashFast
Valor: 25000
Fecha: 06/05/2026
```

---

## Formulario web personalizado

Además de los modelos internos, el proyecto incluye una modificación del formulario web de Odoo.

El objetivo de esta modificación es permitir que el usuario pueda solicitar información desde una interfaz sencilla, sin necesidad de escribir consultas SQL manualmente.

El formulario personalizado permite recoger datos como:

- correo o empresa asociada
- tabla o área de información solicitada
- rango de fechas
- tipo de consulta
- datos necesarios para generar el SQL

La personalización se realiza principalmente mediante dos archivos:

```text
views/website_contact.xml
static/src/js/website_contact.js
```

---

### `website_contact.xml`

Este archivo modifica la vista del formulario web de Odoo.

Su función principal es adaptar el formulario estándar a las necesidades del proyecto DashFast.

Desde este archivo se pueden añadir, modificar o eliminar campos del formulario.

Ejemplos de elementos que puede controlar:

- campos visibles en el formulario
- nombres de campos enviados al backend
- acción del formulario
- método de envío
- integración con rutas personalizadas
- estructura visual del formulario

---

### `website_contact.js`

Este archivo añade lógica JavaScript al formulario.

Su objetivo es mejorar la interacción del usuario con el formulario y controlar comportamientos dinámicos.

Por ejemplo:

- mostrar u ocultar campos según la selección del usuario
- cambiar opciones disponibles en función de otra opción elegida
- validar ciertos datos antes del envío
- mejorar la experiencia del usuario
- evitar que el formulario sea completamente estático

Esta parte es importante porque permite que el formulario sea más flexible y se adapte mejor al tipo de información que se quiere consultar.

---

## Automatización de consultas SQL

Una de las funcionalidades más importantes del proyecto es la generación automática de consultas SQL.

El usuario no escribe directamente la consulta. En su lugar, rellena un formulario con la información que necesita.

Después, el sistema procesa esos datos y genera una consulta SQL adaptada.

---

### Objetivo de la automatización

El objetivo es reducir el trabajo manual y evitar que el usuario tenga que escribir consultas SQL cada vez que quiera obtener información.

En un caso real, esto permitiría que una persona con menos conocimientos técnicos pudiera solicitar datos concretos mediante un formulario.

Por ejemplo:

```text
Quiero consultar las ventas de una empresa entre dos fechas concretas.
```

El sistema podría generar automáticamente una consulta SQL preparada para extraer esos datos desde PostgreSQL.

---

### Carpeta `search`

Las consultas generadas se guardan en la carpeta:

```text
dashfast_business_intelligence/search/
```

Ejemplos de archivos generados:

```text
DashFast_Ventas_06052026_11_22_06.sql
Suministros_Levante_SL_Ventas_05052026_12_28_36.sql
Suministros_Levante_SL_Ventas_06052026_08_30_14.sql
```

Cada archivo representa una consulta generada automáticamente.

El nombre del archivo incluye información útil como:

- nombre de la empresa
- tipo de consulta
- fecha de generación
- hora de generación

Esto permite identificar fácilmente cuándo se creó cada consulta y a qué información pertenece.

---

### Script de generación

La lógica relacionada con la generación de consultas se encuentra dentro de la carpeta:

```text
dashfast_business_intelligence/controles/
```

Archivo principal:

```text
script.py
```

Este script se encarga de procesar los datos recibidos y generar la consulta SQL correspondiente.

---

## Estructura del proyecto

La estructura actual del proyecto es la siguiente:

```bash
.
├── DashFast.pdf
├── docker-compose.yml
├── estructura.txt
├── README.md
└── dashfast_business_intelligence/
    ├── __init__.py
    ├── __manifest__.py
    │
    ├── controles/
    │   ├── __init__.py
    │   └── script.py
    │
    ├── models/
    │   ├── __init__.py
    │   ├── company_metric.py
    │   ├── departament.py
    │   └── employee_kpi.py
    │
    ├── search/
    │   ├── DashFast_Ventas_06052026_11_22_06.sql
    │   ├── Suministros_Levante_SL_Ventas_05052026_12_28_36.sql
    │   └── Suministros_Levante_SL_Ventas_06052026_08_30_14.sql
    │
    ├── security/
    │   └── ir.model.access.csv
    │
    ├── static/
    │   └── src/
    │       └── js/
    │           └── website_contact.js
    │
    └── views/
        ├── company_metric.xml
        ├── department.xml
        ├── employee_kpi.xml
        └── website_contact.xml
```

---

## Explicación de carpetas y archivos

### `DashFast.pdf`

Documento o presentación asociada al proyecto.

Puede utilizarse como apoyo para explicar:

- objetivo del proyecto
- problema detectado
- solución propuesta
- arquitectura general
- demostración
- resultados
- posibles mejoras futuras

---

### `docker-compose.yml`

Archivo encargado de definir los servicios necesarios para ejecutar el proyecto mediante Docker Compose.

Normalmente, este archivo contiene la configuración de servicios como:

- Odoo
- PostgreSQL
- pgAdmin, si se utiliza
- volúmenes
- redes
- puertos

Gracias a este archivo, el proyecto puede levantarse sin instalar manualmente todos los servicios en el equipo.

---

### `README.md`

Archivo de documentación principal del repositorio.

Su objetivo es explicar qué es el proyecto, cómo funciona, cómo instalarlo y qué contiene.

Es el primer archivo que normalmente ve una persona al entrar en el repositorio de GitHub.

---

### `estructura.txt`

Archivo auxiliar con la estructura del proyecto.

No es imprescindible para el funcionamiento del módulo. Puede utilizarse como referencia durante el desarrollo, aunque en un entorno final podría excluirse del repositorio.

---

### `dashfast_business_intelligence/`

Carpeta principal del módulo personalizado de Odoo.

Todo el código del módulo se encuentra dentro de esta carpeta.

---

### `__manifest__.py`

Archivo de configuración principal del módulo de Odoo.

Este archivo indica a Odoo información como:

- nombre del módulo
- versión
- autor
- categoría
- dependencias
- archivos XML que se deben cargar
- archivos de seguridad
- assets estáticos, como JavaScript
- descripción del módulo

Sin este archivo, Odoo no puede reconocer correctamente el módulo.

---

### `__init__.py`

Archivo utilizado para inicializar el módulo Python.

Permite indicar qué paquetes o carpetas internas deben cargarse.

Por ejemplo:

- modelos
- controladores
- scripts auxiliares

---

### `models/`

Carpeta donde se definen los modelos personalizados del módulo.

Cada archivo Python representa una parte de la estructura de datos.

Archivos incluidos:

```text
company_metric.py
departament.py
employee_kpi.py
```

Estos archivos permiten crear nuevas entidades dentro de Odoo.

---

### `views/`

Carpeta donde se definen las vistas XML del módulo.

Las vistas controlan cómo se muestran los datos dentro de la interfaz de Odoo.

Archivos incluidos:

```text
company_metric.xml
department.xml
employee_kpi.xml
website_contact.xml
```

Las vistas pueden incluir:

- vistas de lista
- vistas de formulario
- vistas de búsqueda
- acciones
- menús
- modificación de formularios web

---

### `security/`

Carpeta donde se definen los permisos de acceso.

Archivo principal:

```text
ir.model.access.csv
```

Este archivo indica qué permisos tienen los usuarios sobre los modelos personalizados.

Por ejemplo:

- leer registros
- crear registros
- modificar registros
- eliminar registros

En Odoo, los permisos son necesarios para poder acceder a los modelos desde la interfaz.

---

### `static/`

Carpeta utilizada para archivos estáticos del módulo.

En este proyecto contiene código JavaScript.

Ruta principal:

```text
static/src/js/website_contact.js
```

Este archivo se carga en el frontend de Odoo y permite controlar el comportamiento del formulario web.

---

### `controles/`

Carpeta creada para almacenar lógica auxiliar relacionada con el proyecto.

Actualmente contiene:

```text
script.py
```

Este archivo está relacionado con la generación automática de consultas SQL.

En futuras versiones, esta carpeta podría evolucionar hacia una estructura más estándar de Odoo, por ejemplo usando una carpeta `controllers/` si se trabaja directamente con rutas HTTP personalizadas.

---

### `search/`

Carpeta donde se guardan las consultas SQL generadas automáticamente.

Cada archivo `.sql` representa una consulta creada a partir de los datos introducidos por el usuario en el formulario.

Esta carpeta es útil para:

- revisar consultas generadas
- guardar un histórico
- documentar pruebas
- reutilizar consultas
- conectar posteriormente con herramientas de análisis

---

## Instalación con Docker Compose

Esta sección explica cómo instalar y ejecutar el proyecto usando Docker Compose.

---

### Requisitos previos

Antes de ejecutar el proyecto, es necesario tener instalado:

- Docker Desktop
- Git
- navegador web
- editor de código, por ejemplo Visual Studio Code

Opcionalmente:

- Power BI Desktop
- pgAdmin
- extensión de Docker para Visual Studio Code

---

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
```

Entrar en la carpeta del proyecto:

```bash
cd TU_REPOSITORIO
```

---

### 2. Comprobar que existe el archivo `docker-compose.yml`

Antes de levantar el entorno, comprobar que el archivo existe:

```bash
dir
```

En Linux o macOS:

```bash
ls
```

Debe aparecer un archivo llamado:

```text
docker-compose.yml
```

---

### 3. Levantar los contenedores

Ejecutar:

```bash
docker compose up -d
```

Este comando descarga las imágenes necesarias y levanta los servicios definidos en el archivo `docker-compose.yml`.

Si se utiliza una versión antigua de Docker Compose, también puede usarse:

```bash
docker-compose up -d
```

---

### 4. Comprobar que los contenedores están activos

```bash
docker ps
```

Deberían aparecer los contenedores relacionados con el proyecto, por ejemplo:

- Odoo
- PostgreSQL
- pgAdmin, si está configurado

---

### 5. Ver los logs del proyecto

Para ver los logs generales:

```bash
docker compose logs -f
```

Para ver únicamente los logs del servicio de Odoo, si el servicio se llama `web`:

```bash
docker compose logs -f web
```

---

### 6. Acceder a Odoo

Abrir el navegador y entrar en:

```text
http://localhost:8080
```

El puerto puede variar según la configuración definida en el archivo `docker-compose.yml`.

---

### 7. Crear o seleccionar la base de datos

Al entrar en Odoo, puede ser necesario crear una base de datos o seleccionar una existente.

El módulo DashFast debe instalarse dentro de la base de datos de Odoo que se vaya a utilizar para el proyecto.

---

### 8. Activar el modo desarrollador

Dentro de Odoo:

```text
Ajustes → Activar modo desarrollador
```

El modo desarrollador permite actualizar la lista de aplicaciones y trabajar con módulos personalizados.

---

### 9. Actualizar la lista de aplicaciones

Dentro de Odoo:

```text
Aplicaciones → Actualizar lista de aplicaciones
```

Después, buscar el módulo:

```text
DashFast Business Intelligence
```

---

### 10. Instalar el módulo

Una vez encontrado el módulo, pulsar en:

```text
Instalar
```

Odoo cargará:

- modelos Python
- vistas XML
- menús
- acciones
- permisos
- assets JavaScript

---

## Uso básico del módulo

Una vez instalado el módulo, se puede utilizar desde dos partes principales.

---

### 1. Uso interno desde Odoo

Desde el backend de Odoo se pueden gestionar los modelos personalizados:

- Departamentos
- KPIs de empleados
- Métricas de empresa

Estos modelos permiten registrar información interna de la empresa y visualizarla desde la interfaz de Odoo.

---

### 2. Uso desde el formulario web

Desde el sitio web de Odoo, el usuario puede acceder al formulario personalizado.

El formulario permite introducir información que posteriormente será procesada para generar una consulta SQL.

Flujo:

```text
Usuario rellena el formulario
        ↓
El formulario envía los datos
        ↓
Python recibe la información
        ↓
Se genera una consulta SQL
        ↓
La consulta se guarda en la carpeta search
```

---

### 3. Revisión de consultas generadas

Las consultas SQL generadas se guardan dentro de:

```text
dashfast_business_intelligence/search/
```

Cada archivo puede abrirse con un editor de texto o utilizarse posteriormente para extraer información desde la base de datos.

---

## Comandos útiles

### Levantar el entorno

```bash
docker compose up -d
```

---

### Apagar el entorno

```bash
docker compose down
```

---

### Reiniciar todos los servicios

```bash
docker compose restart
```

---

### Reiniciar solo Odoo

Si el servicio de Odoo se llama `web`:

```bash
docker compose restart web
```

---

### Ver contenedores activos

```bash
docker ps
```

---

### Ver logs generales

```bash
docker compose logs -f
```

---

### Ver logs de Odoo

```bash
docker compose logs -f web
```

---

### Entrar dentro del contenedor de Odoo

Si el contenedor se llama `DashFast_Odoo`:

```bash
docker exec -it DashFast_Odoo bash
```

---

### Entrar dentro del contenedor de PostgreSQL

Si el contenedor se llama `DashFast_Postgres`:

```bash
docker exec -it DashFast_Postgres bash
```

---

### Comprobar conexión a PostgreSQL desde Docker

Ejemplo:

```bash
docker exec -it DashFast_Postgres psql -U USUARIO -d NOMBRE_BASE_DATOS
```

---

## Buenas prácticas del repositorio

Durante el desarrollo pueden generarse archivos que no deberían subirse al repositorio.

Por ejemplo:

```text
__pycache__/
*.pyc
```

Estos archivos son generados automáticamente por Python.

También puede decidirse si subir o no las consultas SQL generadas dentro de la carpeta `search`.

En un proyecto real, se recomienda usar un archivo `.gitignore`.

Ejemplo de `.gitignore` recomendado:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Archivos temporales
*.log
*.tmp

# Estructura auxiliar
estructura.txt

# Entornos virtuales
venv/
.env

# Archivos del sistema
.DS_Store
Thumbs.db
```

Si no se quieren subir las consultas generadas automáticamente:

```gitignore
dashfast_business_intelligence/search/*.sql
```

Si se quiere mantener la carpeta `search` vacía en GitHub, se puede añadir un archivo `.gitkeep` dentro de ella:

```text
dashfast_business_intelligence/search/.gitkeep
```

---

## Notas sobre seguridad

Este proyecto tiene un enfoque académico, pero en un entorno real habría que tener en cuenta varios aspectos de seguridad:

- no subir contraseñas reales al repositorio
- no guardar credenciales directamente en el código
- usar variables de entorno
- validar correctamente todos los datos recibidos desde formularios
- evitar inyección SQL
- controlar permisos de usuario en Odoo
- proteger rutas públicas
- limitar el acceso a archivos generados
- revisar qué información se guarda en los archivos `.sql`

En un entorno profesional, las credenciales deberían gestionarse mediante variables de entorno o archivos no versionados.

---

## Posibles mejoras futuras

Algunas mejoras que podrían añadirse al proyecto son:

### Mejoras funcionales

- añadir más tipos de consultas
- permitir seleccionar más tablas desde el formulario
- generar consultas SQL más avanzadas
- permitir descargar la consulta desde la interfaz
- mostrar un mensaje de confirmación más personalizado
- guardar el histórico de consultas dentro de un modelo de Odoo
- crear una pantalla en Odoo para consultar los archivos generados

### Mejoras técnicas

- separar mejor la lógica en controladores estándar de Odoo
- mejorar validaciones del formulario
- añadir control de errores más detallado
- evitar consultas SQL inseguras
- mejorar la estructura del código
- añadir tests
- añadir documentación técnica adicional

### Mejoras de Business Intelligence

- conectar directamente con Power BI
- crear dashboards de ejemplo
- automatizar la ejecución de consultas
- crear una tabla calendario
- preparar modelos estrella
- añadir métricas DAX
- crear informes filtrables por empresa, fecha o producto

### Mejoras de despliegue

- usar variables de entorno
- mejorar el archivo `docker-compose.yml`
- añadir instrucciones para producción
- separar entorno de desarrollo y entorno final
- añadir backup automático de base de datos

---

## Estado del proyecto

El proyecto se encuentra en fase académica y de desarrollo.

Actualmente permite:

- instalar un módulo personalizado en Odoo
- trabajar con modelos propios
- visualizar datos desde la interfaz de Odoo
- modificar el formulario web
- ejecutar lógica JavaScript en el frontend
- generar consultas SQL automáticamente
- guardar consultas como archivos `.sql`
- preparar una base para análisis posterior con Power BI

---

## Objetivo académico

Este proyecto ha sido desarrollado como parte de mi formación en Desarrollo de Aplicaciones Multiplataforma.

El objetivo no es únicamente crear un módulo funcional, sino demostrar un flujo completo de trabajo que une varias áreas:

```text
Desarrollo backend
        ↓
Modelado de datos
        ↓
Personalización de Odoo
        ↓
Automatización con Python
        ↓
SQL
        ↓
Docker
        ↓
Business Intelligence
        ↓
Power BI
```

Este enfoque permite mostrar una solución más completa que una aplicación aislada, conectando el desarrollo de software con el análisis de datos.

---

## Resumen final

DashFast Business Intelligence es un proyecto que combina Odoo, Python, SQL, Docker y Power BI para crear una solución orientada al análisis empresarial.

El módulo permite registrar información, personalizar formularios, generar consultas SQL y preparar los datos para su explotación en herramientas de Business Intelligence.

Su objetivo principal es demostrar cómo se puede automatizar parte del proceso de obtención de datos y facilitar la creación de informes para la toma de decisiones.
