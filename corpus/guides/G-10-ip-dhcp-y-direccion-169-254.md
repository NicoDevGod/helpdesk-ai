---
id: G-10
titulo: DHCP, IP duplicada y la dirección 169.254
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# DHCP, IP duplicada y 169.254

## Qué hace DHCP
El router entrega automáticamente a cada dispositivo una dirección IP, una puerta de enlace y un DNS. Sin eso, el dispositivo no sabe cómo salir.

## Dirección 169.254.x.x
Si `ipconfig` muestra una IP que empieza con `169.254`, el equipo **no recibió dirección del DHCP** y se asignó una por sí mismo. No tendrá internet.

Qué revisar:
1. Que el cable o el WiFi estén realmente conectados al router correcto.
2. Que el DHCP esté activado en el router.
3. Que el router no haya agotado su rango de direcciones (muchos dispositivos).
4. Que no haya un segundo router o equipo en la red entregando direcciones (ver abajo).

Intento rápido en Windows:
- `ipconfig /release`
- `ipconfig /renew`

## Dos DHCP en la misma red
Si el cliente conectó otro router o repetidor mal configurado, puede haber dos equipos entregando direcciones y los dispositivos quedan con datos contradictorios. Síntoma: unos equipos funcionan y otros no, o la puerta de enlace cambia de un momento a otro. Solución: dejar el DHCP activo en un solo equipo (el principal) y poner el otro en modo punto de acceso.

## IP duplicada
Dos dispositivos con la misma IP provocan cortes intermitentes en ambos. Suele ocurrir cuando se configura una IP fija a mano dentro del rango que reparte el DHCP. Solución: usar una reserva de DHCP en el router o una IP fija **fuera** del rango de reparto.

## Qué anotar
IP, máscara y puerta de enlace que mostraba el equipo, y si `release` y `renew` lo arreglaron.
