---
id: G-06
titulo: Cortes intermitentes de internet cada pocas horas
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Cortes intermitentes

## Lo primero: caracterizar el corte
Un corte que ocurre "a veces" es difícil de arreglar hasta que se describe bien. Pregunta:
- ¿Cada cuánto ocurre y cuánto dura? ¿Siempre a la misma hora?
- ¿Se cae todo (cable y WiFi) o solo el WiFi?
- ¿Afecta a todos los dispositivos o a uno solo?
- ¿Las luces del equipo cambian cuando se corta? (ver G-02)

## Cómo interpretar la respuesta
- **Se cae solo el WiFi y el cable sigue:** problema de radio, interferencia o dispositivo (ver G-04 y G-05).
- **Se caen WiFi y cable, y las luces de señal del proveedor cambian:** problema de acceso o de fibra (ver G-03).
- **Se cae todo pero las luces están normales:** puede ser sobrecalentamiento, el router saturado de dispositivos, o un problema más arriba que se debe escalar.
- **Siempre a la misma hora:** busca algo programado o un patrón de uso (reinicios automáticos, otro equipo que satura la red).

## Revisiones del equipo
- **Temperatura:** el equipo no debe estar tapado ni sobre otro aparato que caliente.
- **Fuente de poder:** una fuente defectuosa causa reinicios aleatorios. Si el equipo se reinicia solo, desconfía de ella y del enchufe.
- **Cables sueltos o dañados.**
- **Reinicios del equipo:** si el tiempo de funcionamiento (uptime) en la configuración es muy bajo, el equipo se está reiniciando solo.

## Cómo reunir evidencia
Pide al cliente que anote la hora de cada corte durante un par de días, y deja un `ping -t 8.8.8.8` corriendo en un computador conectado por cable para ver cuándo se pierden paquetes.

## Cuándo escalar
Cuando los cortes se repiten, afectan a todo, y ya descartaste fuente de poder, cables y temperatura. Adjunta las horas de los cortes.
