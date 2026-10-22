---
id: G-13
titulo: Cómo documentar un ticket de soporte
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Cómo documentar un ticket

## Para qué
Un buen ticket evita que la siguiente persona repita lo que ya se probó. Se ahorra tiempo y el cliente no tiene que explicar todo de nuevo.

## Estructura recomendada
1. **Resumen en una línea:** qué falla y desde cuándo. Ejemplo: "Sin internet desde ayer, luz LOS encendida".
2. **Síntoma detallado:** lo que el cliente observa, con sus palabras.
3. **Alcance:** a qué dispositivos, ubicaciones o servicios afecta.
4. **Qué se probó:** lista de pasos y el resultado de cada uno.
5. **Datos técnicos:** estado de las luces, IP, velocidades medidas, mensajes de error.
6. **Hipótesis actual:** qué se sospecha y por qué.
7. **Siguiente paso:** quién debe hacer qué.

## Ejemplo
> **Resumen:** WiFi lento en el segundo piso desde hace una semana.
> **Alcance:** solo dispositivos inalámbricos; por cable la velocidad es normal.
> **Se probó:** medición por cable (normal), medición por WiFi cerca del router (normal), medición en el segundo piso (baja). Banda 5 GHz.
> **Hipótesis:** cobertura insuficiente en el segundo piso.
> **Siguiente paso:** proponer un repetidor o sistema mesh (ver G-14).

## Errores comunes
- Escribir "se revisó" sin decir qué se revisó ni el resultado.
- No poner la hora ni las mediciones.
- Mezclar varios problemas en un solo ticket.
- Incluir datos que no hacen falta, como claves de WiFi o datos personales. **Nunca pegues contraseñas en un ticket.**

## Cuándo cerrar
Cuando el cliente confirma que el problema está resuelto, y se anota qué lo solucionó.
