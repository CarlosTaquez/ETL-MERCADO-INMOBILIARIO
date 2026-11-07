# Proyecto de Análisis del Mercado Inmobiliario

## 1. Descripción del proyecto

Este proyecto tiene como objetivo analizar información del mercado inmobiliario mediante el procesamiento, almacenamiento y visualización de datos relacionados con la venta de viviendas.

El trabajo se desarrolla en equipo y está dividido en diferentes responsabilidades: procesamiento de datos mediante ETL, almacenamiento en PostgreSQL, análisis y visualización con Power BI y desarrollo de una aplicación.

## 2. Integrantes y responsabilidades

El proyecto está organizado en cuatro responsabilidades:

- **Integrante 1 – ETL y base de datos:** extracción, transformación y carga de los datos utilizando Python, PySpark y PostgreSQL. Diseño y preparación de la base de datos para el almacenamiento de la información.
- **Integrante 2 – Power BI y análisis de datos:** construcción del modelo de datos, medidas DAX, indicadores y visualizaciones para analizar el mercado inmobiliario.
- **Integrante 3 – Desarrollo de la aplicación:** implementación de la aplicación que permitirá consultar y utilizar la información procesada.
- **Integrante 4 – Integración y apoyo al proyecto:** participación en la integración de los componentes y las actividades complementarias del proyecto.

*Nota: las responsabilidades de los integrantes pueden ajustarse según la distribución acordada por el equipo.*

## 3. Responsabilidad del Integrante 1: ETL y base de datos

Se desarrolló un proceso ETL (Extract, Transform, Load) para preparar y almacenar los datos del mercado inmobiliario.

### Tecnologías utilizadas

- Python.
- PySpark.
- PostgreSQL 18.
- psycopg2.
- python-dotenv.
- Visual Studio Code.

### Fuente de datos

Se utilizó el conjunto de datos **King County House Sales**, obtenido de Kaggle.

El archivo original contiene información de viviendas, precios, superficies, ubicación geográfica, habitaciones, baños y otras características.

### 3.1 Extracción (Extract)

Se implementó el archivo `extract.py`, encargado de leer el archivo CSV original utilizando PySpark.

Se realizó la lectura de los datos y la identificación de su estructura, cantidad de registros y columnas.

### 3.2 Transformación (Transform)

En el archivo `transform.py` se desarrollaron las operaciones de preparación y transformación de los datos.

Entre las principales actividades realizadas se encuentran:

- Auditoría de los datos.
- Revisión de valores nulos.
- Identificación de registros con identificadores repetidos.
- Revisión de valores inválidos en campos numéricos.
- Conversión de la columna `date` al tipo de dato fecha.
- Conversión de la superficie de pies cuadrados a metros cuadrados.
- Cálculo del precio por metro cuadrado.

Los identificadores repetidos se conservaron, ya que se decidió no eliminar registros del conjunto original.

### 3.3 Carga (Load)

En el archivo `load.py` se implementó la conexión con PostgreSQL mediante `psycopg2`.

Los datos transformados se insertaron en la tabla `public.viviendas`, utilizando las columnas correspondientes.

Las credenciales de conexión se gestionan mediante variables de entorno en un archivo `.env`, evitando publicar contraseñas en el repositorio.

## 4. Resultados del proceso ETL

Al finalizar el proceso se obtuvieron los siguientes resultados:

| Indicador | Resultado |
|---|---:|
| Registros procesados | 21.613 |
| Columnas originales | 21 |
| Columnas transformadas | 23 |
| Valores nulos detectados | 0 |
| Identificadores repetidos conservados | 176 |
| Base de datos | mercado_inmobiliario |
| Tabla | public.viviendas |

Se añadieron dos columnas calculadas:

- `superficie_m2`: superficie habitable expresada en metros cuadrados.
- `precio_por_m2`: precio de la vivienda por metro cuadrado.

La tabla PostgreSQL también contiene `registro_id`, una columna autogenerada que funciona como clave primaria y permite conservar los identificadores originales repetidos.

## 5. Estructura del proyecto

```text
mercado-inmobiliario-etl/
│
├── config/
│
├── data/
│   └── raw/
│       └── kc_house_data.csv
│
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

**Descripción de los archivos principales:**

- `main.py`: ejecuta las etapas del proceso ETL.
- `extract.py`: realiza la extracción de los datos.
- `transform.py`: realiza la auditoría y transformación.
- `load.py`: carga los datos en PostgreSQL.
- `requirements.txt`: contiene las dependencias del proyecto.
- `.env.example`: plantilla para configurar las credenciales de conexión.
- `.gitignore`: evita publicar archivos privados o innecesarios.

## 6. Configuración del entorno

Para ejecutar el proyecto localmente se deben tener instalados Python, PostgreSQL 18 y las dependencias necesarias.

### 6.1 Clonar el repositorio

```bash
git clone https://github.com/CarlosTaquez/ETL-MERCADO-INMOBILIARIO.git
```

Entrar en la carpeta:

```bash
cd ETL-MERCADO-INMOBILIARIO
```

### 6.2 Crear un entorno virtual

```bash
python -m venv venv
```

Activarlo en Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 6.3 Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6.4 Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto, tomando como referencia `.env.example`.

Configurar los datos de conexión:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mercado_inmobiliario
DB_USER=postgres
DB_PASSWORD=tu_contraseña
```

Cada integrante debe utilizar sus propias credenciales de PostgreSQL.

### 6.5 Preparar la base de datos

Crear una base de datos llamada:

```text
mercado_inmobiliario
```

La tabla utilizada por el proceso de carga es:

```text
public.viviendas
```

Para trabajar con los datos ya procesados, se puede importar el archivo CSV entregado por el Integrante 1 mediante pgAdmin 4.

**Importante:** el archivo CSV contiene los datos procesados y debe importarse respetando sus encabezados y tipos de datos. La tabla de destino debe tener una estructura compatible con las columnas exportadas.

## 7. Ejecución del proceso ETL

Una vez configurado el entorno, la base de datos y el archivo `.env`, el proceso se ejecuta desde la raíz del proyecto:

```bash
python main.py
```

El programa realiza las siguientes operaciones:

1. Extracción del archivo CSV.
2. Auditoría de los datos.
3. Transformación de las columnas.
4. Carga de los registros en PostgreSQL.

**Advertencia:** el proceso de carga actual utiliza inserciones. No se debe ejecutar nuevamente sobre una tabla que ya contiene los registros sin preparar previamente la tabla, porque se pueden insertar datos duplicados.

## 8. Entrega de información al equipo

Para continuar con las siguientes etapas del proyecto se entregan dos recursos:

**Repositorio de GitHub:**

https://github.com/CarlosTaquez/ETL-MERCADO-INMOBILIARIO

Contiene el código fuente, la estructura del proyecto, las dependencias y la documentación del proceso ETL.

**Archivo CSV procesado:**

Se comparte por separado el archivo exportado desde PostgreSQL, correspondiente a la tabla `public.viviendas`.

Este archivo contiene la información transformada y puede utilizarse para:

- Construir el modelo de datos en Power BI.
- Crear indicadores y visualizaciones.
- Realizar análisis del mercado inmobiliario.
- Alimentar la aplicación que desarrollará el equipo.

## 9. Continuidad del proyecto

Una vez finalizada la etapa de extracción, transformación y almacenamiento, el equipo puede continuar con el análisis de datos en Power BI y el desarrollo de la aplicación.

El objetivo es que todos los componentes trabajen sobre la misma información procesada, manteniendo consistencia entre la base de datos, los análisis y la aplicación.

---

**Proyecto universitario – Ingeniería de Software**

**Repositorio:** CarlosTaquez / ETL-MERCADO-INMOBILIARIO