# Corpus

Documentos que alimentan el asistente (HD-0.3).

| Carpeta | Contenido | Origen |
|---|---|---|
| `guides/` | Guías generales de diagnóstico, en español e inglés | Redactadas para este proyecto, sin datos de ninguna empresa |
| `manuals/` | Manuales públicos de fabricantes | Pendiente. Cada uno debe registrar la URL de origen y su licencia |

## Formato de cada documento

Cada guía lleva un encabezado YAML con `id`, `titulo`, `idioma` (`es` o `en`), `tipo`, `origen` y `estado`, y secciones con títulos claros. Un test (`api/tests/test_corpus.py`) comprueba que se cumpla.

## Reglas

- Sin datos de la empresa donde trabaja el autor ni de clientes reales.
- Sin contraseñas ni claves, ni siquiera de ejemplo con aspecto real.
- Lo que depende del modelo concreto de un equipo se marca como tal y no se afirma en general.
- Las guías en estado "borrador" se revisan por una persona antes de considerarse listas.

## Guías actuales

| ID | Tema | Idioma |
|---|---|---|
| G-01 | Sin internet, diagnóstico por capas | es |
| G-02 | Luces de un ONT o router | es |
| G-03 | Sin señal óptica (LOS) | es |
| G-04 | Lento por WiFi, normal por cable | es |
| G-05 | Bandas 2,4 y 5 GHz | es |
| G-06 | Cortes intermitentes | es |
| G-07 | Hay conexión pero no cargan sitios (DNS) | es |
| G-08 | Reinicio frente a reinicio de fábrica | es |
| G-09 | Puertos, DMZ y CGNAT | es |
| G-10 | DHCP, IP duplicada y 169.254 | es |
| G-11 | Medir bien la velocidad | es |
| G-12 | Comandos de diagnóstico en Windows | es |
| G-13 | Cómo documentar un ticket | es |
| G-14 | Cobertura WiFi, repetidor y mesh | es |
| G-15 | No internet, layer by layer | en |
| G-16 | Wi-Fi 2.4 vs 5 GHz | en |
| G-17 | Reboot vs factory reset | en |
