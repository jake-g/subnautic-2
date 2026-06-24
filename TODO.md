# Subnautica 2 Progression Roadmap & Exploration Tracker

A structured coaching roadmap and systematic exploration checklist for **Subnautica 2** (Early Access Standalone / Unreal Engine 5).

> [!NOTE]
> **Primary Progression Manual**: For clinical biome geometry matrices, high-level progression phases, beginner survival wisdom, transition criteria, and official dev news links, consult [GUIDE.md](./GUIDE.md).
> **Live Diagnostic Telemetry**: For dynamic progression state, active tool loadouts, inventory registers, and world streaming partition flags decoded from `savegame_1.sav`, consult [REPORT.md](./REPORT.md).

---

## 🧭 Exploration Verification SOP ("Closing Out" Areas)

When scouting nearby landmarks, beacons, and biomes, use this Standard Operating Procedure (SOP) before marking an area as **Closed / Fully Explored**:
1. **Sweep & Scan**: Equip Scanner (`BP_Scanner`) and check all wreckage crates, data terminals, PDA lore logs, and tech fragments.
2. **Verify Blueprints**: Check your PDA Blueprints tab (`::Unlocked`) to confirm no partial fragments (e.g., 1/2 or 2/3) remain for vehicles or base modules in that zone.
3. **Telemetry Validation**: Run `make report` to extract world partition strings and confirm StoryGoal trigger completion in `savegame_1_decoded.md`.

### Perimeter Destination Verification Checklists (Granular Closeout Targets)

#### 1. Emergency Lifepod & Starter Shelf (Safe Shallows)
- **Approx Location**: `~0m depth` | Origin (`X: 0m, Y: 0m`). (Approx `~238m East` of Angel Comb Base).
- **Status**: **CLOSED**
- **Verified Blueprints & Equipment**:
  - [x] Scanner (`BP_Scanner`) & Habitat Builder (`BP_Builder`)
  - [x] Flashlight (`Tools_Flashlight`) & Small Oxygen Tank (`BP_OxygenTank_Small`)
  - [x] Survival Knife (`BP_Knife`) & Standard Metal Salvage (`BP_MetalSalvage`)
- **Verified Flora Scans**: Acid Anemone (`BP_AcidAnemone`) & Coral Sea Whip (`BP_CoralSeaWhip`).

#### 2. Angel Comb Starter Base (Infected Crevasse Shelf)
- **Approx Location**: `~30m depth` | `~238m West` of Lifepod (`X: 0.1m, Y: -237.8m W`). (Core Habitat Origin).
- **Status**: **CLOSED (Core Habitat)**
- **Verified Base Modules & Construction**:
  - [x] Starter Multipurpose Room built near Angel Comb thermal current.
  - [x] Side Hatch (`BP_Hatch`) attached and ~5 Solar Panels deployed on roof for continuous power/oxygen.
  - [x] Interior Bed (`BioBed`) installed and Wall Lockers (`BP_WorldSupplyLocker`) constructed and stocked with Silver, Titanium, Copper, Quartz, and Lead.

#### 3. Crashed Black Box (Alterra Emergency Signal)
- **Approx Location**: `~45m depth` | `~380m North` of Lifepod (`~250m Northeast` of Angel Comb Base).
- **Status**: **IN PROGRESS**
- **Granular Verification Targets**:
  - [ ] **Blueprints / Tech**: Scan Light Stick / Floodlight fragments and Bar Table / Bench decorative furniture blueprints scattered around the crashed recorder. *(Verify 100% scanned!)*
  - [~] **PDA Lore / Audio Logs**: Emergency Radio Transmission Audio Log retrieved. *(Verify 100% via Databank tab)*.
  - [ ] **Scraps**: Salvage all nearby Titanium cargo crates and copper wire nodes.

#### 4. Welcome Center & BioLab Facility (Alterra Research Outpost)
- **Approx Location**: `~60m depth` | `~500m Northwest` of Lifepod (`~300m North-Northwest` of Angel Comb Base).
- **Status**: **NEEDS VERIFICATION (100%)**
- **Granular Verification Targets**:
  - [ ] **Blueprints / Tech**: Scan BioLab Lab Counter, Specimen Analyzer, Glass Desk, Office Chair, and Chemical Storage Locker blueprints inside the laboratory chambers. *(Verify 100%!)*
  - [ ] **Equipment Data**: Research High Capacity Oxygen Tank blueprint data terminal.
  - [ ] **PDA Lore / Audio Logs**: Collect Welcome Center Log #1 (Research Objectives), BioLab Containment Breach Datapad, and Chief Scientist Audio Log. *(Manual check required)*.
  - [ ] **Scan Targets**: Specimen containment cylinders, automated centrifuge, Alterra security bulkhead doors.

#### 5. Abandoned Basecamp & Habitat Beacon (Infected Crevasse Wreckage)
- **Approx Location**: `~70m depth` | `~420m West` of Lifepod (`~180m West` of Angel Comb Base along canyon shelf).
- **Status**: **NEEDS VERIFICATION (100%)**
- **Granular Verification Targets**:
  - [ ] **Blueprints / Tech**: Scan Multipurpose Room fragments (if partial), Composite Corridor sections, Exterior Growbed / Planter Box, Floodlight (`BP_Floodlight`), and Battery Charger fragments (requires 2 scans). *(Verify 100%!)*
  - [~] **PDA Lore / Logs**: Colonist Bunker Pad #052 extracted. *(Verify 100% via Databank tab)*.
  - [ ] **Scan Targets**: Damaged Alterra base modules, whiteboards, broken solar arrays.

#### 6. Kelp Forest Border & Crevasse Ravines (Creepvine Forests)
- **Approx Location**: `~50m-90m depth` | `~250m-400m W/SW` of Lifepod (Directly `South & adjacent` to Angel Comb Base).
- **Status**: **SCOUTED / UNCRAFTED**
- **Granular Verification Targets**:
  - [ ] **Vehicle Blueprints**: Locate and scan all 3 **Seaglide** (`BP_Seaglide`) vehicle fragments along Kelp ravines.
  - [ ] **Submersible Tech**: Scan Mobile Vehicle Bay fragments (1/3, 2/3, 3/3) and Bioreactor fragments.
  - [ ] **Resource Harvesting**: Collect Creepvine Seed Clusters (bioluminescent yellow pods) for Silicone Rubber / Lubricant and slash stalks for Creepvine Leaves (`FiberMesh`).

#### 7. Thermal Vents & Hydrothermal Fissures (Volcanic Trenches)
- **Approx Location**: `~80m-120m depth` | `~450m NE/E` of Lifepod (`~550m ENE` of Angel Comb Base).
- **Status**: **SCOUTED / UNCLOSED**
- **Granular Verification Targets**:
  - [ ] **Power Blueprints**: Scan Thermal Plant fragments and Power Transmitter (`BP_PowerTransmitter`) fragments near active volcanic vents.
  - [ ] **Station Tech**: Scan Vehicle Modification Station fragments.
  - [ ] **Mineral Scouting**: Identify and harvest Magnetite and crystalline Lithium deposits surrounding hydrothermal fissures.

---

## 📋 Action Roadmap

> [!IMPORTANT]
> **Milestone Lifecycle**: When a coaching milestone under **Pending Focus** is completed and verified against live save telemetry, remove it from this file and record its completed details as a new entry in [CHANGELOG.md](./CHANGELOG.md). Keep `TODO.md` focused strictly on immediate actionable tasks and exploration closeouts.

Immediate things to craft, gather, and verify—sequenced logically for an efficient geographic sweep.

### Pending Focus (Geographic Sweep Sequence)

* [ ] **TODO-17 (Base Workshop & Repair Tool)** *(Location: Angel Comb Base)*: Construct an interior **Fabricator** (`BP_Fabricator`). Gather Cave Sulfur + Titanium + Wiring Kit to craft a **Repair Tool** (`BP_RepairTool`) to maintain habitat integrity.
* [ ] **TODO-16 (South Sweep: Kelp Resource Harvest & Seaglide)** *(Location: ~250m South)*: Swim south to the Kelp Forest border (`FeatherKelp`). Gather **Creepvine Seed Clusters** (`CreepvineSeedCluster`) for Lubricant/Silicone and slash stalks for **Creepvine Leaves** (`FiberMesh`). Scan remaining **Seaglide** fragments (3 total) and craft it upon returning to base.
* [ ] **TODO-15 (Base Agriculture & Pressure Gear)** *(Location: Angel Comb Base)*: Deploy an **Exterior Growbed** outside your base hatch to farm Creepvine locally. Upgrade your Small O₂ Tank to a **High Capacity O₂ Tank** (+90 max O₂) and craft a **Rebreather** (Wiring Kit + Fiber Mesh).
* [ ] **TODO-14 (North Sweep: Shallow Reef & Laser Cutter)** *(Location: ~350m North / Northeast)*: Using your Seaglide, harvest **Table Coral** (`TableCoral`) along shallow ledges and mine deeper Sandstone outcrops (>50m depth) for **Gold** (`DA_Gold`) and **Diamonds**. Craft a **Laser Cutter** (`BP_LaserCutter`) at your workshop.
* [ ] **TODO-13 (Base Utility & Storage Expansion)** *(Location: Angel Comb Base)*: Construct an interior **Battery Charger** (once scanned) to recycle batteries. Attach an adjacent Multipurpose Room dedicated to labeled Wall Lockers (`BP_WorldSupplyLocker`) and attach a **Scanner Room** (`BP_ScannerRoom`) with Range Upgrades.
* [ ] **TODO-12 (Clockwise Wreckage Closeout Sweep)** *(Location: Perimeter Wreckage Loop)*: Execute a continuous Seaglide sweep across **Crashed Black Box** (~380m N) → **Welcome Center BioLab** (~500m NW) → **Abandoned Basecamp** (~420m W). Slice open sealed bulkheads with your Laser Cutter, scan remaining Battery Charger fragments, and verify 100% blueprint capture.
* [ ] **TODO-11 (Visual Telemetry via Screenshots)** *(Location: Ongoing)*: Capture in-game screenshots of your **PDA Blueprints tab** (recording partial fragment scanning progress like 1/3 Seaglide or 1/2 Battery Charger) and **Base Storage Lockers** (showing per-container inventories). Share or drop these screenshots directly in chat for 100% AI vision verification!
