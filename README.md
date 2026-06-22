# Subnautica 2 Telemetry Toolkit

A dedicated engineering toolkit and automated coaching bridge for **Subnautica 2** (Early Access Standalone / Unreal Engine 5). This repository connects to a remote Windows 11 gaming rig over SSH (`192.168.0.100`), inspects live binary Unreal Engine 5 SaveGame files (`.sav`), synchronizes save vaults locally, and generates dynamic clinical coaching walkthroughs and progression guides.

## Features

- **Remote Telemetry Bridge**: Connects to the gaming rig (`jake@192.168.0.100`), runs Python regular expression parsers against binary save files, and extracts player inventory, equipped tools, and visited biomes.
- **File Synchronization Engine**: Bi-directional base64 transfer tool (`sync_remote_vault.py`) that pulls binary saves (`.sav`) and engine config profiles (`GameUserSettings.ini`) flat into local backups (`backups/`).
- **SaveGame Decoder**: Clinical plaintext converter (`decode_sav.py`) that filters out boilerplate UE5 serialization noise and dumps progression registers to structured markdown guides.
- **Remote Rollback Engine**: Tracks remote progression states directly inside `C:/Users/jake/AppData/Local/Subnautica2/Saved/.git` on the gaming host, preventing save corruption and enabling rollback.
- **Master Coaching Guide**: Synthesizes live binary save inspection with historical chat archives to generate [subnautica.md](file:///Users/jakegarrison/Downloads/projects/subnautica-2/subnautica.md) with reverse-chronological roadmaps and multiplayer SOPs.

## Structure

| File | Description |
| :--- | :--- |
| [subnautica_scraper.py](file:///Users/jakegarrison/Downloads/projects/subnautica-2/subnautica_scraper.py) | Main telemetry scraper and master coaching guide generator. |
| [decode_sav.py](file:///Users/jakegarrison/Downloads/projects/subnautica-2/decode_sav.py) | Unreal Engine 5 SaveGame binary decoder. |
| [sync_remote_vault.py](file:///Users/jakegarrison/Downloads/projects/subnautica-2/sync_remote_vault.py) | Bi-directional base64 file synchronization bridge over SSH. |
| [Makefile](file:///Users/jakegarrison/Downloads/projects/subnautica-2/Makefile) | Developer CLI automation targets. |
| [subnautica.md](file:///Users/jakegarrison/Downloads/projects/subnautica-2/subnautica.md) | Generated master coaching walkthrough and progression report. |
| [CHANGELOG.md](file:///Users/jakegarrison/Downloads/projects/subnautica-2/CHANGELOG.md) | Chronological ledger recording developer milestones. |
| `backups/` | Local flat archive containing synced `.sav` files, INI configs, and logs. |

## Usage

Use the included [Makefile](file:///Users/jakegarrison/Downloads/projects/subnautica-2/Makefile) to manage remote inspection and vault sync:

```bash
# Scrape live save game over SSH and regenerate report
make report

# Pull remote save games and config INIs locally
make pull

# Decode local backup saves and format guides
make format

# Check remote Git save repo status on gaming PC
make git-status
```

## Status

- **Location**: ~239m West of lifepod in **Infected Crevasse** (mined Silver ore veins).
- **Focus**: Base construction at **Coral Gardens** (~350m North) for inventory storage.
- **Equipment**: Habitat Builder (`BP_Builder`), Scanner (`BP_Scanner`), Flashlight (`Tools_Flashlight`), Small Oxygen Tank.

---
*For detailed history, see [CHANGELOG.md](file:///Users/jakegarrison/Downloads/projects/subnautica-2/CHANGELOG.md) and [subnautica.md](file:///Users/jakegarrison/Downloads/projects/subnautica-2/subnautica.md).*
