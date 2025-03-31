Cambio al modelo all-mpnet-base-v2: Este modelo es más robusto para capturar relaciones semánticas complejas, a diferencia de all-MiniLM-L6-v2, que priorizaba doc:2 por razones menos precisas (probablemente palabras como "populares").
Consistencia: Los embeddings en Redis y el embedding de la consulta ahora se generan con el mismo modelo, asegurando una comparación justa.

El modelo **all-mpnet-base-v2** es un modelo de lenguaje desarrollado por **Microsoft**, basado en **MPNet** (Masked and Permuted Pretraining for Language Understanding). Este modelo está optimizado para tareas de **similaridad semántica** y **embeddings de oraciones**, lo que lo hace útil en aplicaciones como **búsqueda semántica, clasificación de textos, recuperación de información y clustering de documentos**.

### 📌 **Características clave:**
- **Arquitectura**: Basado en MPNet, que combina lo mejor de BERT y XLNet para mejorar la representación de oraciones.
- **Tamaño**: 110 millones de parámetros.
- **Entrenamiento**: Afinado utilizando **Sentence-BERT (SBERT)** en una gran cantidad de datos para mejorar la generación de embeddings.
- **Entrada y salida**:  
  - **Entrada**: Un texto o una oración.  
  - **Salida**: Un vector de embedding de tamaño **768**, que representa la semántica de la oración.
- **Aplicaciones**:
  - Comparación semántica de textos.
  - Recuperación de documentos basada en significado.
  - Clustering y clasificación de texto.
  - Generación de embeddings para motores de búsqueda.

En la versión anterior de bindings.cpp no se utilizó torch para analizar los embeddings de Redis,  en esta nueva versión de bindings.cpp se utiliza torch para cargar el modelo all-mpnet-base-v2.  Este cambio muestra un mejor desempeño para análisis de embeddings así como el performance también es superior al pasar el cálculo a C++ y no en Python.

En resumen ahora el sistema RAG:

  - Usa Redis para almacenar documentos y embeddings precalculados.
  - Genera embeddings de consultas en tiempo real con all-mpnet-base-v2 en C++.
  - Selecciona correctamente el documento más relevante basándose en similitud coseno.
