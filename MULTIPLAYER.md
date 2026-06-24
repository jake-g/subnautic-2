# Subnautica 2 Multiplayer

Comprehensive operational guidelines, cloud synchronization semantics, and save hygiene protocols for **Subnautica 2** (Early Access Standalone / Unreal Engine 5).

---

## ☁️ Cloud Sharing Semantics

The built-in cloud-share engine in *Subnautica 2* is an asynchronous **manual snapshot (copy/paste) utility**, not a live cloud synchronized lobby. Builds and world changes **will not automatically sync** across Steam accounts or separate gaming rigs in real time.

### Cloud Sharing Lifecycle
1. **Host Export ("Upload to Cloud")**: Person A selects **"Upload to Cloud"** from the main menu. The server snapshots the active world tree and generates a unique one-time-use **8-digit share code**.
2. **Guest Import ("Import Save")**: Person B inputs this 8-digit code via **"Import Save"**. Person B receives an exact, isolated local clone of Person A's world at that exact timestamp.
3. **Isolated Progression**: Any subsequent habitat modules, vehicle assemblies, or resource gathering Person B performs solo exist **strictly on Person B's local machine**. Person A's save tree remains completely unaltered.

---

## 🔄 The "Pass the Torch" Synchronization Protocol

To merge guest progress or solo base expansions back to the primary world host:
1. Person B saves their solo progress, returns to the main menu, and selects **"Upload to Cloud"** to generate a fresh 8-digit share code.
2. Person B transmits this new code to Person A.
3. Person A selects **"Import Save"** and inputs the fresh code, overwriting their older local save tree with Person B's progressed snapshot.

> [!WARNING]
> **Zero Branch Merging**: If Person A and Person B both play solo on diverged world copies simultaneously, their changes cannot be merged. Only one designated player should progress the primary save solo at any given time.

> [!CAUTION]
> **Early Access Inventory Reset Bug**: Importing cloud saves in Early Access frequently resets personal inventories or respawns player characters at the starter Emergency Lifepod. **Always deposit all gear, raw materials, and equipped hand tools into a base Wall Locker before uploading or importing cloud codes.**

---

## 🛠️ Automated Community Background Daemons

For PC players seeking automated background cloud synchronization without manual 8-digit codes, third-party community background daemons such as [SaveSync](https://savesync.games) are commonly utilized across Steam Community and Reddit discussions to continuously mirror local Unreal Engine 5 save directories (`Saved/SaveGames`).
