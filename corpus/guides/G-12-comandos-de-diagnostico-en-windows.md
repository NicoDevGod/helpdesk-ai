---
id: G-12
titulo: Comandos de diagnóstico de red en Windows
idioma: es
tipo: guia
origen: redactado para este proyecto, sin datos de empresa
estado: borrador, pendiente de revisión
---

# Comandos de diagnóstico de red en Windows

Se ejecutan en el Símbolo del sistema o en PowerShell.

| Comando | Para qué sirve |
|---|---|
| `ipconfig` | Muestra la IP, la máscara y la puerta de enlace del equipo |
| `ipconfig /all` | Añade el DNS, la dirección MAC y si usa DHCP |
| `ipconfig /release` y `ipconfig /renew` | Suelta y vuelve a pedir una IP al DHCP |
| `ipconfig /flushdns` | Borra la caché de nombres |
| `ping 8.8.8.8` | Comprueba si hay salida a internet por IP |
| `ping google.com` | Comprueba la resolución de nombres y la conexión |
| `ping -t 8.8.8.8` | Ping continuo; se detiene con Ctrl+C. Sirve para ver cortes |
| `tracert google.com` | Muestra por qué saltos pasa el tráfico y dónde se pierde |
| `nslookup google.com` | Consulta al DNS qué dirección corresponde a un nombre |
| `netstat -an` | Lista conexiones y puertos abiertos |

## Cómo leer un ping
- **Respuesta con tiempo** (por ejemplo, 12 ms): hay conexión. Cuanto menor el tiempo, mejor.
- **Tiempo de espera agotado:** el destino no respondió. Puede haber un corte, o el destino puede bloquear los ping.
- **Pérdida de paquetes:** si de cada 100 paquetes se pierden varios, la conexión es inestable.

## Cómo leer un tracert
Cada línea es un salto. Un `*` aislado en un salto intermedio no siempre es un problema (algunos equipos no responden), pero si **todos** los saltos a partir de uno fallan, el problema está en ese punto o justo después.

## Orden sugerido
`ipconfig` y luego ping a la puerta de enlace, ping a `8.8.8.8` y ping a un nombre. Es la misma secuencia de la guía G-01.
