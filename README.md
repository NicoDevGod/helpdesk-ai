# HelpDesk AI

Asistente de soporte para técnicos de un ISP: responde con pasos de diagnóstico y **cita la fuente**, y usa herramientas (tickets, estado de equipos) con confirmación. Proyecto de aprendizaje que integra los seis proyectos del [portafolio de IA](https://nicodevgod.github.io/ai-portfolio/) y suma evaluación, base de datos, autenticación y observabilidad.

Estado: **Fase 0, cimientos** (en curso).

| Carpeta | Contenido |
|---|---|
| `api/` | Servicio FastAPI (fase 1 en adelante) |
| `ingest/` | Carga y troceado de documentos |
| `eval/` | Set dorado y escenarios de evaluación |
| `web/` | Interfaz |
| `docs/` | Alcance y decisiones (`docs/adr/`) |

Empieza por [`docs/scope.md`](docs/scope.md).

## Desarrollo

```bash
py -m pip install -r requirements-dev.txt
ruff check . && ruff format --check . && pytest
```

CI ejecuta lo mismo en cada push (`.github/workflows/ci.yml`).
