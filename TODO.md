# Subnautica 2 Progression Roadmap & Exploration Tracker

A structured coaching roadmap and systematic exploration checklist for **Subnautica 2** (Early Access Standalone / Unreal Engine 5).

> [!NOTE]
> **Primary Progression Manual**: For clinical biome geometry matrices, high-level progression phases, beginner survival wisdom, transition criteria, and official dev news links, consult [GUIDE.md](./GUIDE.md).
> **Live Diagnostic Telemetry**: For dynamic progression state, active tool loadouts, inventory registers, and world streaming partition flags decoded from `savegame_1.sav`, consult [REPORT.md](./REPORT.md).

---

## 📋 Immediate Action Roadmap (Next Session Focus)

> [!IMPORTANT]
> **Active Origin**: Starting safely inside **Angel Comb Base** (`~30m depth`) with `2x Salt` in inventory.

### 🚀 Priority 1: Kelp Forest Border Harvest & Scan (`~250m South` | `~50m depth`)
* [ ] **Harvest Creepvine**: Grab at least **2x Creepvine Seed Clusters** (glowing yellow pods needed for Silicone Rubber / Lubricant) and slash stalks for **Creepvine Leaves** (`FiberMesh`). *Essential for crafting Seaglide!*
* [ ] **Scan Seaglide (`BP_Seaglide`)**: Sweep shallow seafloor directly under the glowing seed pods. Scan white Alterra equipment boxes for missing Seaglide handlebars/propellers (`3` needed).
* [ ] **HIGH PRIORITY — Gather Gold & Lead (`Galena Outcrops`)**: 
  - *How to find & identify*: Look for **dark grey, metallic cube-shaped crystalline rocks** sticking out of ravine walls (unlike brownish Limestone or reddish Sandstone). When cracked, Galena drops either **Lead** or Titanium. Also crack Sandstone/Shale for **Gold** (`BP_Gold`).
  - *Why this is crucial*: **Lead** builds your **Sonic Resonator** & base foundations; **Gold** crafts **Computer Chips** (needed for base automation & Scanner Room upgrades) and Advanced Wiring Kits. *(Silver Ore: Grab when seen to restock reserves).*
* [ ] **HIGH PRIORITY — Slice Shelf Bracket Corals (`Table Coral`)**: You haven't been doing this! Use your Survival Knife to slice red/purple/green shelf coral brackets growing horizontally along canyon walls for **Table Coral Samples** (`BP_TableCoral`). *Required to craft Computer Chips and Scanner Room Range Upgrades!*
* [ ] **Bonus Salt Collection**: Pick up any extra crystalline **Salt deposits** spotted on the seafloor (supplies battery crafting & water purification). *(Note: 2x Salt already saved in base inventory)*.
* [ ] **HUD Triage**: Confirm `Wu "Wu" Lianghai`, `Old Habitat`, and `Blackbox - Ruby` are marked **Green** / OFF. Set `Blackbox - Wander` to Green once swept.

### 🏠 Priority 2: Base Assembly & Power Network (Angel Comb Base)
* [ ] **Deploy Hydroelectric Turbine**: Place your newly unlocked **Hydroelectric Turbine** (`HydroelectricTurbine`) in the bubbling hydrothermal vent current near your base to generate continuous renewable energy.
* [ ] **Connect Power Transmitter**: Deploy a **Power Transmitter** (`BP_PowerTransmitter`) to relay remote thermal current back to your base corridors.
* [ ] **Construct Bioreactor**: Build an interior **Bioreactor** (`BP_Bioreactor`) inside your multipurpose room to supplement solar/hydro power.
* [ ] **Craft Seaglide & Repair Tool**: Using gathered Creepvine materials, craft your **Seaglide** (`BP_Seaglide`) and **Repair Tool** (`BP_RepairTool`) at your interior Fabricator.
* [ ] **Scanner Room Upgrades** *(Along the way bonus)*: Craft **Scanner Room Range Upgrades** (`BP_ScannerRoomUpgrade_Range`) at your Fabricator using Copper + Table Coral to expand radar coverage across the entire 400m perimeter.

### 🏊‍♂️ Priority 3: Wreckage Sweep Circuit (Camp One & BioLab Hangar)
* [ ] **Stop 1: Camp One Wreckage** *(Swim ~180m West | ~70m depth)*:
  - Search open white Alterra cargo crates sitting in the sand directly outside the bunker entrance to scan remaining **Repair Tool** (`BP_RepairTool`) fragments (`+1` left for 3/3).
  - Search roughly `~30m South/West` of the bunker doors among broken docking rings / thruster pods for **Tadpole Submersible** (`BP_Tadpole`) fragments (`+1` left for 3/3).
  - Check small tripod **Work Light** (`BP_WorkLight`) posts lying in the sand near the hatch (`+1` or `+2` left).
  - Inspect interior wall storage compartments inside damaged habitat tubes for **Wall Rack** (`BP_WallRack`) fragments (`+2` left).
  - *Along the way bonus*: Scan broken **Battery Charger** (`BP_BatteryCharger`) terminals on bunker walls (`2` scans needed to unlock battery recharging).
  - *HUD Triage*: Once swept, set `Camp One` Beacon to **Green** (or toggle OFF).
* [ ] **Stop 2: Welcome Center BioLab Hangar** *(Swim ~300m NNW | ~60m depth)*:
  - Check inside crashed BioLab moonpool hangar bay (water-level catwalks) or split yellow shipping containers along the shelf for any missed **Tadpole Submersible** fragments (`+1` left).
  - *Along the way bonus*: Keep an eye out for floating **Mobile Vehicle Bay** (`BP_MobileVehicleBay`) deployment consoles along the 100m drop-off shelf.
  - *HUD Triage*: Confirm `Welcome Center`, `Blackbox - Anita`, and `Blackbox - Chap` are set to **Green** / OFF.

---

## 🧭 Exploration Verification SOP ("Closing Out" & Disabling Signals)

Before marking an area as **Closed / Fully Explored** and toggling OFF its HUD Beacon in your PDA Signals tab, verify against these 3 concrete pieces of evidence:
1. **Telemetry StoryGoal Trigger (`_Hide`)**: Check [savegame_1_decoded.md](./backups/savegame_1_decoded.md#L227). When you interact with a major signal's core terminal, the engine records `DA__Signal_..._Hide`. If `_Hide` is present, the primary narrative objective is 100% complete.
2. **Zero Partial Blueprints (No Leftover Crates)**: Open your PDA **Blueprints** tab under `In Progress`. If you have unresolved fractions (like `2/3 Repair Tool`, `2/3 Tadpole`), wreckage sites you previously visited still contain un-scanned cargo crates!
3. **Sealed Bulkhead Audit (Laser Cutter Check)**: Many crashed Alterra structures contain sealed titanium bulkhead doors requiring a **Laser Cutter** (`BP_LaserCutter`). Do not disable its signal until you return with a cutting tool!

### Active Perimeter Destination Tracker

#### 1. Crashed Black Box (Alterra Emergency Signal)
- **Approx Location**: `~45m depth` | `~380m North` of Lifepod (`~250m Northeast` of Angel Comb Base).
- **Status**: **IN PROGRESS**
  - [ ] Scan Light Stick / Floodlight fragments and Bar Table / Bench decorative furniture blueprints.
  - [~] Emergency Radio Transmission Audio Log retrieved. *(Verify via Databank tab)*.
  - [ ] Salvage nearby Titanium cargo crates and copper wire nodes.

#### 2. Abandoned Basecamp & Habitat Beacon (Infected Crevasse Wreckage)
- **Approx Location**: `~70m depth` | `~420m West` of Lifepod (`~180m West` of Angel Comb Base along canyon shelf).
- **Status**: **NEEDS VERIFICATION (100%)**
  - [ ] Scan Multipurpose Room fragments (if partial), Composite Corridor sections, Exterior Growbed, Floodlight, and Battery Charger fragments.
  - [~] Colonist Bunker Pad #052 extracted. *(Verify via Databank tab)*.

#### 3. Thermal Vents & Hydrothermal Fissures (Volcanic Trenches)
- **Approx Location**: `~80m-120m depth` | `~450m NE/E` of Lifepod (`~550m ENE` of Angel Comb Base).
- **Status**: **SCOUTED / UNCLOSED**
  - [ ] Scan Thermal Plant fragments and Power Transmitter fragments near active volcanic vents.
  - [ ] Scan Vehicle Modification Station fragments.
  - [ ] Identify and harvest Magnetite and crystalline Lithium deposits surrounding hydrothermal fissures.

* **Visual Telemetry via Screenshots**: Capture in-game screenshots of your **PDA Blueprints tab** and **Base Storage Lockers**. Share or drop these screenshots directly in chat for 100% AI vision verification!
