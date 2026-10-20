# HelpDesk AI: alcance (HD-0.1)

Versión 0.1. Este documento manda: si algo no está aquí, no se construye hasta cambiarlo aquí primero.

## Qué es

Un asistente de soporte para técnicos de un proveedor de internet (ISP). El técnico describe un problema del cliente (texto, y más adelante voz o foto) y el asistente responde con pasos de diagnóstico **citando el documento y la página de donde salen**. Cuando corresponde, también consulta o crea tickets mediante herramientas.

## Quién lo usa

Un técnico de soporte de nivel 1 o 2 que atiende reclamos de internet y TV, tiene prisa y necesita saber qué probar primero. No es un asistente para el cliente final.

## Idioma

Español como idioma principal; también entiende preguntas y manuales en inglés (el 20% del set dorado es en inglés).

## Datos

Solo documentos públicos (manuales de routers y ONT, estándares) y guías escritas desde cero para este proyecto. **Ninguna información de la empresa donde trabajo, ni de clientes reales.** Los tickets y equipos que se usen en las demos son inventados.

## 10 casos de uso

1. Sin internet: el router tiene luz roja en el puerto WAN o PON. ¿Qué reviso?
2. Internet lento solo por WiFi pero normal por cable.
3. Cortes intermitentes cada pocas horas.
4. Cómo reiniciar de fábrica un modelo concreto de router u ONT.
5. Qué significa cada luz de un ONT.
6. Cómo configurar apertura de puertos o DMZ en un modelo concreto.
7. Diferencias entre bandas de 2,4 y 5 GHz y cuándo recomendar cada una.
8. Crear un ticket con el resumen del problema y los pasos ya probados.
9. Consultar el estado de un ticket existente.
10. Dada una foto de las luces de un equipo, decir qué estado indica (fase 4).

## Lo que NO hará

- No ejecuta cambios en equipos reales ni se conecta a una red de producción.
- No responde sin una fuente: si no la encuentra, dice que no tiene esa información.
- No guarda ni pide datos personales de clientes.
- No sustituye el criterio del técnico: sugiere y cita; decide la persona.
- No cierra ni modifica tickets sin confirmación explícita (meta: 0 escrituras sin confirmar).
- No es un producto comercial ni tiene soporte.

## Cómo sabremos que funciona

Las metas medibles están en el plan (hit@4 ≥ 85 %, fidelidad ≥ 0,8, escenarios de agente ≥ 80 %, p95 < 8 s, costo < US$ 0,01 por consulta). Son propuestas hasta la primera medición de la fase 1 y se ajustan en un ADR, no en silencio.

## Fuera de la primera versión

Voz, foto y modelo propio (fases 4 y 5) quedan fuera de la ruta mínima (fases 0 a 3).
