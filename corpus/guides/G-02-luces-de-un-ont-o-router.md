---
id: G-02
titulo: Qué significan las luces de un ONT o router (guía general)
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Luces de un ONT o router: guía general

## Aviso importante
Los nombres, colores y comportamientos de las luces **cambian según el fabricante y el modelo**. Esta guía describe lo que suele ser común. Ante la duda, manda el manual del modelo concreto.

## Luces habituales

| Luz | Qué indica normalmente | Si falla |
|---|---|---|
| Power / Encendido | Hay energía | Revisar fuente de poder y enchufe |
| PON | El ONT está sincronizado con la red de fibra | Si parpadea sin parar, aún no se sincroniza; ver G-03 |
| LOS (Loss of Signal) | Se enciende o se pone roja cuando **no llega luz** por la fibra | Ver G-03 |
| WAN / Internet | El equipo obtuvo conexión a internet | Si está apagada con PON estable, puede ser un problema de configuración o de autenticación |
| LAN 1-4 | Hay un equipo conectado por cable en ese puerto | Cambiar cable o puerto |
| WiFi (2.4G / 5G) | La radio WiFi está activa | Revisar si está desactivada en la configuración |

## Patrón útil para razonar
- PON estable y WAN apagada: la fibra está bien, el problema está más arriba (configuración o servicio).
- LOS encendida: el problema está en la fibra o el conector, no en el router.
- Todo encendido y sin internet: ve a G-01, desde el paso 3.

## Qué anotar
Qué luces estaban encendidas, apagadas o parpadeando, y de qué color. Una foto de las luces ayuda más que la descripción.
