---
id: G-01
titulo: Sin internet, cómo diagnosticar por capas
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Sin internet: diagnosticar por capas

## Cuándo usar esta guía
El cliente dice "no tengo internet" y no se sabe todavía si falla el acceso, el router, el WiFi o solo un sitio.

## Idea central
Avanza de abajo hacia arriba y detente en la primera capa que falle. Cada capa depende de la anterior.

1. **Energía y luces.** ¿El equipo está encendido? Mira las luces del ONT o módem (ver G-02). Si no hay luz de señal del proveedor, el problema está antes del router: ve a G-03.
2. **Enlace local.** Si el equipo conecta por cable, ¿el puerto LAN tiene luz? Prueba otro cable y otro puerto.
3. **Dirección IP.** En el equipo del cliente, `ipconfig` (Windows). Si la IP empieza con `169.254`, no recibió dirección del router (ver G-10). Si tiene IP del rango del router, sigue.
4. **Puerta de enlace.** `ping` a la puerta de enlace que muestra `ipconfig`. Si no responde, falla la red local.
5. **Salida a internet por IP.** `ping 8.8.8.8`. Si responde, la conexión a internet funciona.
6. **Nombres (DNS).** `ping google.com`. Si el paso 5 funciona y este no, es un problema de DNS (ver G-07).
7. **Aplicación.** Si todo lo anterior funciona, el problema está en el navegador, un bloqueo o el sitio concreto.

## Qué anotar
La capa donde falló y qué probaste. Es lo primero que necesita quien reciba el ticket (ver G-13).

## Cuándo escalar
Si las luces del equipo indican que no hay señal del proveedor, o si el equipo del cliente funciona hasta el paso 5 pero otros sitios no, y ya probaste otro dispositivo.
