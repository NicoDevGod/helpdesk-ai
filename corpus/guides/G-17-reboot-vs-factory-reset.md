---
id: G-17
titulo: Reboot versus factory reset on a router or ONT
idioma: en
tipo: guia
origen: written for this project, no company data
estado: borrador, pendiente de revisión
---

# Reboot versus factory reset

## They are different things
- **Reboot:** powers the device off and on. **It does not erase the configuration.** It is safe and is the first thing to try.
- **Factory reset:** **erases all configuration** and returns the device to its factory state. It is the last resort.

## When to reboot
Unexplained slowness, a connection that hangs, Wi-Fi that disappears, or configuration changes that do not apply.

How: unplug the power adapter, wait about 30 seconds, and plug it back in. Then wait a few minutes for all lights to settle before testing.

## When to consider a factory reset
Only if a normal reboot is not enough and a corrupted configuration is suspected, or if the administrator password was forgotten.

## What is lost
- Wi-Fi name and password.
- Port forwarding, DMZ and rules.
- The administrator password.
- **Provider data** the device needs to connect (for example credentials or settings applied by the provider). In many cases the provider can re-apply them remotely, but not always.

## Before doing it
1. Confirm the provider's procedure for that model: on some provider-supplied devices a factory reset disconnects the customer until it is reconfigured.
2. Write down the current settings (Wi-Fi name and password, port rules).
3. Tell the customer they will lose their settings and may be offline for a while.

## How it is done
Usually by holding the small reset button (often with a paperclip) for several seconds while the device is on. **The exact time and the light behavior depend on the model:** check the device manual.

## What to record
Whether a normal reboot or a factory reset was done, the time, and the result.
