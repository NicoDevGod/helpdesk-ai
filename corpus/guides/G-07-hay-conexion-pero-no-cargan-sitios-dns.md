---
id: G-07
titulo: Hay conexión pero no cargan los sitios, problemas de DNS
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Hay conexión, pero no cargan los sitios (DNS)

## Síntoma típico
El WiFi o el cable están conectados, pero el navegador dice que no encuentra el sitio. Algunas aplicaciones que ya tenían conexión abierta pueden seguir funcionando.

## Prueba de aislamiento
1. `ping 8.8.8.8`. Si **responde**, hay salida a internet por dirección IP.
2. `ping google.com`. Si **no responde** o dice que no encuentra el host, el fallo está en el DNS, es decir, en la traducción de nombres a direcciones.

Si el paso 1 también falla, no es DNS: vuelve a G-01.

## Qué hacer
1. **Limpiar la caché del equipo:** `ipconfig /flushdns` en Windows.
2. **Ver qué DNS usa el equipo:** `ipconfig /all`. Normalmente apunta al router, que reenvía al DNS del proveedor.
3. **Probar con otro DNS público** en el equipo, por ejemplo 8.8.8.8 o 1.1.1.1, y comprobar si ahora carga. Si carga, el DNS del proveedor o el del router tiene un problema.
4. **Probar con otro dispositivo** en la misma red para saber si el problema es del equipo o de la red.
5. **Reiniciar el router** si el DNS que falla es el suyo.

## Herramienta útil
`nslookup google.com` muestra qué servidor responde y si consigue una dirección.

## Qué anotar
Si el ping por IP funciona, si el ping por nombre falla, qué DNS usaba el equipo y si cambiarlo lo arregló.

## Cuándo escalar
Si cambiar el DNS arregla el problema, pero el DNS del proveedor sigue fallando para todos los clientes, o si no hay ninguna mejora con DNS externos.
