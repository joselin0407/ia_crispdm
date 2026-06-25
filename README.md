# 🤖 CRISP-IA: Agente Inteligente de Documentación de Repositorios (AIDA V3)

## 📋 1. Iniciativa

**CRISP-IA** es una iniciativa estratégica orientada a optimizar el ciclo de desarrollo analítico en la compañía, abordando de raíz uno de los retos históricos de la ciencia de datos: **la descentralización, la inconsistencia técnica y la fuga de conocimiento en la documentación de modelos de Machine Learning.**

A través de **AIDA (Agente Inteligente de Documentación Analítica)**, automatizamos la auditoría y el gobierno de código mediante un agente cognitivo serverless que lee repositorios de datos directamente de la nube, interpreta las matemáticas y configuraciones de los científicos de datos, y autogenera reportes oficiales de gobierno.

---

## 🎯 2. Objetivo

Automatizar y estandarizar de manera pasiva y segura la documentación de proyectos de Machine Learning mediante un agente inteligente (construido bajo el framework **Google Agent Development Kit - ADK**) que:

1. Se conecte de forma segura a buckets de **Google Cloud Storage (GCS)** sin descargar datos sensibles de manera local.
2. Analice de forma lógica los archivos de código fuente Python (`.py`) y Jupyter Notebooks (`.ipynb`).
3. Traduzca las métricas, transformaciones de datos e hiperparámetros de entrenamiento, y redacte automáticamente un reporte formal en formato Microsoft Word (`.docx`) estructurado bajo las 6 fases de la metodología **CRISP-DM (alineada al estándar oficial de IBM SPSS Modeler)**.

---

## 📂 3. Estructura del Repositorio de Datos (GCS Bucket)

Para asegurar una auditoría de gobierno de datos exitosa, cada proyecto de Machine Learning debe estar alojado dentro del proyecto corporativo de GCP **`RUTA-PROYECTO`** bajo el bucket central y estructurado sistemáticamente respetando la siguiente **Convención de Nomenclatura (Naming Convention)**:

**Ruta en Cloud Storage:** `gs://RUTA/gdp_001/`

```text
gs://gdp-RUTA-PROYECTO/gdp_001/
│
├── gdp_001_contexto.txt        # Contexto comercial y objetivos de negocio (Raíz)
│
├── 1. BU/                      # Comprensión del Negocio (Business Understanding)
│   └── gdp_001_BU.ipynb        # Notebook o archivo de la fase inicial
├── 2. DU/                      # Comprensión de los Datos (Data Understanding)
│   └── gdp_001_DU.ipynb        # Notebook con carga de datos y análisis exploratorio (EDA)
├── 3. DP/                      # Preparación de los Datos (Data Preparation)
│   └── gdp_001_DP.py           # Script o notebook de limpieza, imputación y feature engineering
├── 4. MOD/                     # Modelado (Modeling)
│   └── gdp_001_MOD.ipynb       # Notebook con algoritmos entrenados e hiperparámetros
├── 5. EVA/                     # Evaluación (Evaluation)
│   └── gdp_001_EVA.ipynb       # Notebook con matrices de confusión y métricas de desempeño
└── 6. DEPL/                    # Despliegue (Deployment)
    └── gdp_001_DEPL.py         # Script de exportación de artefactos (.pkl, .joblib, etc.)
```

> ⚠️ **Regla de Oro de Gobernanza:** Todos los archivos técnicos de cada fase deben iniciar estrictamente con el código identificador del proyecto (ej: `gdp_001`) definido en el archivo de contexto de la raíz.

---

## ⚙️ 4. Requisitos Previos y Configuración del Entorno Local

Para ejecutar el agente en tu máquina local conectándote de forma segura a Google Cloud, sigue estos pasos ordenados en tu terminal de PowerShell:

### Paso A: Clonar el proyecto y activar el Entorno Virtual de Python
Asegúrate de estar ubicado en la carpeta raíz del proyecto y ejecuta:

```powershell
# 1. Crear el entorno virtual aislado para evitar conflictos de versiones
python -m venv venv

# 2. Activar el entorno virtual en Windows PowerShell
.\venv\Scripts\Activate.ps1

# 3. Actualizar el gestor de paquetes pip e instalar librerías oficiales
python -m pip install --upgrade pip
pip install google-adk google-cloud-storage nbformat python-docx python-dotenv
```

### Paso B: Autenticación con el SDK de Google Cloud (ADC)
Para evitar el uso de API Keys personales y cargar de forma transparente la facturación computacional al proyecto de la empresa:

```powershell
# 1. Asegúrate de tener instalado el Google Cloud CLI (gcloud). Inicia sesión corporativa:
gcloud auth login

# 2. Enlaza tu consola local al proyecto corporativo de analítica:
gcloud config set project cursos-analytics

# 3. Genera tus credenciales por defecto de la aplicación (ADC) en tu sistema:
gcloud auth application-default login
```

### Paso C: Configurar el archivo de Variables de Entorno (`.env`)
Crea un archivo llamado `.env` en la raíz de tu proyecto e inyecta la configuración para habilitar Vertex AI en la nube (sin exponer claves privadas):

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT="NOMBREPROYECTO"
GOOGLE_CLOUD_LOCATION="us-central1"
```

---

## 🕹️ 5. Operación del Agente (Cómo Ejecutar la Auditoría)

Una vez configurado tu entorno de desarrollo, auditar un repositorio se hace en dos sencillos pasos:

**A. Arranca la interfaz interactiva de AIDA V3:**
```powershell
python run_aidav2.py
```

**B. Ordénale la auditoría pasándole la URI de Google Cloud Storage:**
En cuanto aparezca el prompt `[user]:`, introduce la ruta de tu bucket:
```text
[user]: AIDA, analiza la ruta gs://RUTA/gdp_001/ y genera el reporte Word
```

### 🔁 Flujo Automatizado que ejecutará el Agente:

* **A. Conexión en Caliente:** AIDA V3 leerá de forma asíncrona la URI `gs://`, se conectará al bucket usando tu inicio de sesión de gcloud y extraerá el contexto comercial `gdp_001_contexto.txt`.
* **B. Escaneo y Consolidación:** Escaneará carpeta por carpeta leyendo en la memoria RAM el código de los notebooks `.ipynb` y scripts `.py` que correspondan al proyecto `gdp_001`.
* **C. Análisis de IA (Vertex AI):** El modelo `gemini-3.1-flash-lite` procesará el consolidado de código e interpretará de forma lógica las transformaciones y entrenamiento aplicados.
* **D. Generación del Entregable:** El agente invocará la herramienta `save_markdown_as_docx`, limpiará los caracteres especiales visuales y guardará de forma automática en tu disco local un archivo de Word formal e impecable.
* **E. Resultado:** Un documento (ej: `documento_CRISP_DM.docx`) listo para entregar a la Dirección.

---

## 🚀 6. Despliegue en la Nube (Vertex AI Agent Platform)

Como el agente está desarrollado de forma nativa utilizando el Google ADK, la migración para desplegarlo permanentemente en la nube de Google Cloud se realiza de forma directa mediante la terminal de comandos (Cloud Shell) con la siguiente instrucción:

```powershell
adk deploy my_agent_v3
```
*Este comando desplegará el agente de forma oficial en la Plataforma de Agentes de GCP.*
`
