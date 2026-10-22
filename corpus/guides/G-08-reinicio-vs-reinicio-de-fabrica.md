---
id: G-08
titulo: Reinicio normal frente a reinicio de fábrica de un router u ONT
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Reinicio frente a reinicio de fábrica

## Son cosas distintas
- **Reinicio (reboot):** apaga y vuelve a encender el equipo. **No borra la configuración.** Es seguro y es lo primero que se prueba.
- **Reinicio de fábrica (factory reset):** **borra toda la configuración** y deja el equipo como salió de fábrica. Es la última opción.

## Cuándo reiniciar
Lentitud sin causa aparente, conexión que se cuelga, WiFi que desaparece, cambios de configuración que no se aplican.

Forma de hacerlo: desenchufar la fuente de poder, esperar unos 30 segundos y volver a enchufar. Luego espera unos minutos a que todas las luces se estabilicen antes de probar.

## Cuándo considerar el reinicio de fábrica
Solo si el reinicio normal no basta y se sospecha de una configuración dañada, o si se olvidó la clave de administración del equipo.

## Qué se pierde
- Nombre y clave del WiFi.
- Configuración de puertos, DMZ y reglas.
- Clave de acceso a la administración.
- **Datos del proveedor** que el equipo necesita para conectarse (por ejemplo credenciales o configuración que el proveedor aplicó). En muchos casos el proveedor puede volver a aplicarlos de forma remota, pero no siempre.

## Antes de hacerlo
1. Confirma el procedimiento del proveedor para ese modelo: en algunos equipos del proveedor un reinicio de fábrica desconecta al cliente hasta que se reconfigure.
2. Anota la configuración actual (nombre y clave del WiFi, reglas de puertos).
3. Avisa al cliente de que perderá su configuración y de que puede quedarse sin internet un tiempo.

## Cómo se hace
Generalmente se mantiene pulsado el botón pequeño de reset (a menudo hay que usar un clip) durante varios segundos con el equipo encendido. **El tiempo exacto y el comportamiento de las luces dependen del modelo:** consulta el manual del equipo.

## Qué anotar
Si se hizo reinicio normal o de fábrica, la hora y el resultado.
