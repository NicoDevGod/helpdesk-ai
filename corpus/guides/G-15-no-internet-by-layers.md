---
id: G-15
titulo: No internet, how to troubleshoot layer by layer
idioma: en
tipo: guia
origen: written for this project, no company data
estado: borrador, pendiente de revisión
---

# No internet: troubleshooting layer by layer

## When to use this guide
A customer reports "no internet" and it is not yet clear whether the problem is the access line, the router, Wi-Fi, or one specific site.

## Core idea
Work from the bottom up and stop at the first layer that fails. Each layer depends on the one below it.

1. **Power and lights.** Is the device on? Check the ONT or modem lights. If there is no signal light from the provider, the problem is upstream of the router.
2. **Local link.** For wired devices, does the LAN port show a light? Try another cable and another port.
3. **IP address.** Run `ipconfig` on the customer's computer. An address starting with `169.254` means the device got no address from the router's DHCP server.
4. **Default gateway.** Ping the gateway shown by `ipconfig`. If it does not answer, the local network is failing.
5. **Internet by IP.** Run `ping 8.8.8.8`. If it replies, the connection to the internet works.
6. **Names (DNS).** Run `ping google.com`. If step 5 works and this one fails, it is a DNS problem.
7. **Application.** If everything above works, the issue is in the browser, a block, or the specific site.

## What to record
The layer where it failed and what you tried. The next person needs this first.

## When to escalate
If the lights show no provider signal, or if the customer's device works up to step 5 but other sites do not and another device was already tested.
