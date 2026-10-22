# ADR-001: stack, base de datos, LLM y hosting

- Estado: aceptada
- Fecha: 2026-10-22
- Ticket: HD-0.5

## Contexto

HelpDesk AI necesita una API que busque en documentos y cite la fuente, guarde datos que sobrevivan a un reinicio (tickets, historial, resultados de evaluación) y llame a un LLM. Restricciones:

- Presupuesto cero: todo en planes gratuitos.
- Una sola persona, unas 6 h semanales: pocas piezas y conocidas.
- Los proyectos anteriores corren en Render gratis (512 MB de RAM, el servicio se duerme y el primer acceso tarda entre 70 y 100 s). La lección de esos proyectos fue medir la memoria en el entorno real, no en local.
- El chatbot RAG actual usa Chroma en memoria: se reconstruye en cada arranque y no guarda nada. Sirve para una demo, no para tickets ni historial.

## Decisión

| Pieza | Elección |
|---|---|
| API | FastAPI (Python 3.12) |
| Base de datos y búsqueda vectorial | Postgres con la extensión pgvector, alojado en Neon |
| LLM | Groq (`openai/gpt-oss-20b` al inicio), detrás de una interfaz propia para poder cambiarlo |
| Hosting de la API | Render, plan gratuito |
| Hosting de la interfaz | GitHub Pages, como el portafolio |

## Por qué

- **FastAPI:** ya conozco Python, da validación y documentación automática de los endpoints, y es sencillo de probar con pytest.
- **Postgres con pgvector, y no Chroma:** una sola base guarda vectores, tickets e historial, así que no hay dos sistemas que sincronizar. Persiste entre reinicios, de modo que el arranque deja de reindexar todo. También permite búsqueda híbrida (texto más vectores) en la fase 1.
- **Neon, y no la base de Render:** Neon ofrece Postgres gratuito con pgvector. Mantener la base fuera de Render evita depender de las condiciones del plan gratuito de la base de Render (a verificar), y la API puede cambiar de proveedor sin migrar datos.
- **Render para la API:** ya sé desplegar ahí, funciona con el `render.yaml` de mis otros proyectos y conozco sus límites.
- **Groq:** gratuito, rápido y ya integrado en el chatbot. La interfaz propia deja abierta la fase 5, donde se compara contra un modelo ajustado.

## Alternativas descartadas

- **Chroma en memoria o en disco:** no persiste en el plan gratuito de Render y no sirve para datos transaccionales.
- **Supabase:** también sirve (Postgres con pgvector). Me quedo con Neon por ser solo base de datos; Supabase añade autenticación y almacenamiento que aún no necesito. Es el plan B si Neon falla.
- **Fly.io o Railway:** no los conozco y no he revisado sus planes gratuitos; no compensa aprender una plataforma más para este proyecto.
- **Un servidor propio:** costo y mantenimiento fuera del alcance.

## Consecuencias

- **Memoria en Render:** el límite de 512 MB sigue vigente. La API no debe cargar un modelo de embeddings grande; esto se decide en la fase 1 (ver "Pendientes") y se mide en Render, no en local.
- **Arranque en frío doble:** la API se duerme en Render y la base de Neon también puede escalar a cero. El primer acceso tras un rato inactivo puede sumar ambas esperas. Habrá que pre-calentar desde la interfaz, como ya hace el portafolio con las demos.
- **Dependencia de planes gratuitos:** los límites de Render, Neon y Groq pueden cambiar. Los números concretos (almacenamiento, horas, cuotas) se verifican en sus páginas oficiales al empezar la fase 1 y se anotan aquí, no se asumen.
- **Secretos:** las claves (Groq, cadena de conexión de Neon) van en variables de entorno de Render y nunca en el repositorio.

## Pendientes (no decididos aquí)

- **Modelo de embeddings.** MiniLM (el que uso hoy) rinde peor en español. En la fase 1 se compara con un modelo multilingüe usando el set dorado y se registra en ADR-002.
- **Cómo se ejecuta la evaluación en CI** sin gastar la cuota de Groq (fase 3).
- **Autenticación** de la API (fase 6).

## Cuándo revisar

- Si el arranque en frío doble hace inusable la demo.
- Si la memoria en Render supera unos 450 MB medidos.
- Si Groq retira el modelo o cambia las condiciones del plan gratuito.
