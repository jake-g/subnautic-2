# Subnautica 2 Telemetry Report

Live progression telemetry and configuration summary generated via SSH from gaming rig `jake@192.168.0.100`. All binary saves and plaintext configs are mirrored locally in `backups/`.

## Session Specifications
* **Game Title**: Subnautica 2 (Early Access Standalone | Unreal Engine 5)
* **Gaming Host**: `pc` (`192.168.0.100` | Windows 11 x64 | User: `jake`)
* **Platform Provider**: Steam (`OnlineSubsystemSteam` | Player ID `76561198797039235`)
* **Active Save File**: `savegame_1.sav` (1000.4 KB | Last Saved: `2026-06-16 23:29:18`)
* **Auto-Save State**: **Enabled** (`UWESaveSystemUserSetting.ini` | `bAutoSaveEnabled=True`)
* **Display Config**: `1280x720` dynamic render resolution scaling to `3840x2160` output (TSR Upscaling Quality Mode 3 | FPS Cap: 120)
* **Remote Git Repository**: `C:/Users/jake/AppData/Local/Subnautica2/Saved/.git/` (Pristine tree `4df49f6`)
* **Save Directory**: `C:/Users/jake/AppData/Local/Subnautica2/Saved/SaveGames/`
* **Log File**: `C:/Users/jake/AppData/Local/Subnautica2/Saved/Logs/Subnautica2.log`

## Equipment Status
Raw extracted equipment items and resource nodes actively discovered in workspace:

| Category | Discovered Symbols | Verification Status |
| :--- | :--- | :--- |
| **Tools** | Habitat Builder (`BP_Builder`), Scanner (`BP_Scanner`), Flashlight (`Tools_Flashlight`) | Equipped in active `AUWEBaseItem` slots. |
| **Survival Gear** | Small Oxygen Tank (`BP_OxygenTank_Small`), Basic Battery (`BP_BasicBattery`), First Aid MedKit (`BP_MedKit`) | +45.0 Max Oxygen Set Component verified. |
| **Raw Resources** | Titanium (`DA_Titanium`), Copper (`DA_Copper`), Quartz (`DA_Quartz`), Silver (`DA_Silver`), Lead (`DA_Lead`), Glass (`FullGlass`), Copper Wire (`CopperWire`) | Serialized in resource node prototypes. |

## Biome Coordinates
Telemetry engine confirms player traversal across the following core world partitions:

| Partition / Zone | Evaluated Telemetry Symbols | Approx Depth | Distance & Direction from Pod | Relative to Angel Comb Habitat |
| :--- | :--- | :--- | :--- | :--- |
| **Safe Shallows / Pod** | `L_Main`, `Lifepod_SignalOriginal` | ~0m | Origin (`X: 0m, Y: 0m`) | ~238m East |
| **Angel Comb Habitat** | `CoralGardens`, `BioBed`, `SolarPanel` | ~30m | ~238m West (`X: 0.1m, Y: -237.8m W`) | Core Base Reference Point |
| **Crashed Black Box** | `CoralGardensRadioMessageBlackBox` | ~45m | ~380m North | ~250m Northeast |
| **Kelp Forest Border** | `FeatherKelp`, `KelpRandomNode` | ~50m-90m | ~250m-400m West / Southwest | Directly South & Adjacent |
| **Welcome Center BioLab**| `DA__Signal_WelcomeCent_Hide` | ~60m | ~500m Northwest | ~300m North-Northwest |
| **Abandoned Basecamp** | `InvesgPOI_PZ_Basecamp`, `ColonistBunker052` | ~70m | ~420m West | ~180m West along canyon shelf |
| **Thermal Vents** | `SmallVent`, `VentFall` | ~80m-120m | ~450m Northeast / East | ~550m East-Northeast |

## Narrative Quests
* **Welcome Center Signal**: `DA__Signal_WelcomeCent_Hide`
* **Habitat Beacon**: `DA__Signal_Habitat_Hide`
* **Emergency Lifepod**: `Lifepod_SignalOriginal`
* **Black Box Investigation**: `CoralGardensRadioMessageBlackBox`

## Constructed Facilities
* **Base Modules**: `/Game/Art/Bases/BasePieces/Hatch/SM__ASkeletal`, `/Game/Blueprints/BaseBuilding/BP_Hatch_C`, `6Investig_BioBed__CoralGardensRadioMessageBlackBoxbChoi`, `7BioBed_TriggbayInsidChiManifest_DB`, `8Hatch`, `BP_SupplyLocker`, `BP_WorldSupplyLocker`, `BTubaJubileeP_DestroyedBiobed`
* **Discovered POIs**: `/InvesgPOI_PZ_Basecamp`, `6Investig_BioBed__CoralGardensRadioMessageBlackBoxbChoi`, `6ingBioLab_WelcomeCenter`, `CampOne`, `Lifepod_SignalOriginal`, `P/Narrative//DA__Signal_WelcomeCent_Hide`
* **World Engine Milestones**: `CrateHasBeenOpe`, `CrateHasBeenOpeItem`, `StartupItemsHaveBeenAdd`, `aFAbandonedBase`, `bStartupItemsHaveBeenAdd`, `bStartupItemsHaveBeenAdded`
* **Decoded Progression Guide**: [savegame_1_decoded.md](./backups/savegame_1_decoded.md)

## Graphics Configuration
Summary extracted from [GameUserSettings.ini](./backups/GameUserSettings.ini):
* **Resolution**: ResolutionSizeX=1280, ResolutionSizeY=720
* **Frame Rate Cap**: FrameRateLimit=120.000000
* **Upscaling Quality**: ScalabilityQuality_TSR=3

## Recent Engine Events
Snapshot of diagnostic gameplay session events logged by engine:

```text
[2026.06.23-06.04.17:227][969]LogSonarAPI: Warning: Attempting to create an http request without being logged in /a
[2026.06.23-06.04.18:098][969]LogBlueprintUserMessages: [WBP_CompilingShadersScreen_C_2147480723] *** DECONSTRUCT
access-control-expose-headers: x-sentry-error,x-sentry-rate-limits,retry-after
[2026.06.23-06.04.19:986][969]LogMoviePlayer: Shutting down movie player
[2026.06.23-06.04.20:590][969]LogHttp: Warning: 	verb=[POST] url=[https://api.live.subnautica.net/api/v1/player/log
```

## Reference Links
* **Progression Guide**: [GUIDE.md](./GUIDE.md)
* **Progression Roadmap**: [TODO.md](./TODO.md)
* **Primary Project Guide**: [README.md](./README.md)
* **Multiplayer Cloud SOP**: [MULTIPLAYER.md](./MULTIPLAYER.md)
* **Previous Chat Archive**: [subnuatica_2_previous_chat.md](./backups/subnuatica_2_previous_chat.md)
* **Local Engine Log Dump**: [Subnautica2.log](./backups/Subnautica2.log)
* **Local Backups Vault**: [backups/](./backups)
* **Developer Toolkit**: [Makefile](./Makefile)
* **Unified Toolkit**: [subnautica_scraper.py](./subnautica_scraper.py)
* **Project Changelog**: [CHANGELOG.md](./CHANGELOG.md)
* **Steam News Hub**: [store.steampowered.com/news/app/1962700](https://store.steampowered.com/news/app/1962700)
* **Dev Kanban Board**: [subnautica2.nolt.io/kanban](https://subnautica2.nolt.io/kanban)
* **Official Site News**: [unknownworlds.com/en/news](https://unknownworlds.com/en/news)
* **Subnautica 2 Official Wiki**: [subnautica.fandom.com/wiki/Subnautica_2](https://subnautica.fandom.com/wiki/Subnautica_2)
* **Subnautica 2 Interactive Map**: [subnauticamap.io](https://subnauticamap.io)
* **Official Website**: [subnautica.com](https://subnautica.com)
