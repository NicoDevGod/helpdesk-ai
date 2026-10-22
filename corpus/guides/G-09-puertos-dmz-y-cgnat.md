---
id: G-09
titulo: Apertura de puertos, DMZ y CGNAT, guía general
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Apertura de puertos, DMZ y CGNAT

## Para qué se piden
Cámaras de seguridad, servidores caseros, consolas o juegos que necesitan recibir conexiones desde internet.

## Apertura de puertos (port forwarding)
Se indica al router que, cuando llegue tráfico a un puerto concreto desde internet, lo envíe a un equipo de la red local.

Pasos generales (los nombres de menú varían por modelo):
1. Dar al equipo de destino una **IP fija o reservada** en el router, para que no cambie.
2. Entrar en la configuración del router, sección de puertos, NAT o servidores virtuales.
3. Crear la regla: puerto externo, puerto interno, protocolo (TCP, UDP o ambos) y la IP del equipo.
4. Guardar y probar **desde fuera de la red del cliente** (por ejemplo con datos móviles), no desde dentro.

## DMZ
La DMZ envía **todo** el tráfico entrante no solicitado a un equipo. Es práctica para probar, pero **deja ese equipo expuesto a internet**. Úsala solo de forma temporal y no con equipos importantes.

## Cuando nada funciona: CGNAT
Algunos proveedores comparten una misma IP pública entre varios clientes (CGNAT). En ese caso **no se puede abrir puertos hacia internet** desde el router del cliente, porque la IP pública no es solo suya.

Pista para sospecharlo: la IP que muestra el router como "WAN" está en el rango `100.64.0.0` a `100.127.255.255`, o es distinta de la IP pública que muestra un sitio de consulta de IP.

Si el cliente está en CGNAT, las opciones son pedir al proveedor una IP pública (si lo ofrece) o usar servicios de túnel que no requieran puertos abiertos.

## Qué anotar
IP del equipo de destino, puertos y protocolo configurados, y si la IP WAN parece privada o de CGNAT.
