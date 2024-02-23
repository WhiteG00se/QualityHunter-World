<details>
<summary>How to use</summary>
  
- Download this repo and add the files to "[...]\Steam\steamapps\common\Monster Hunter World"
- That's it, you can start the game and all mods will be loaded  
</details>

<details>
<summary>3rd party mods included in our bundle</summary>
  
- Stracker's Loader - https://www.nexusmods.com/monsterhunterworld/mods/1982
- Performance Booster and Plugin Extender - https://www.nexusmods.com/monsterhunterworld/mods/3473
- Tic Rate Fix - https://www.nexusmods.com/monsterhunterworld/mods/3474
- Camera Zoom - https://www.nexusmods.com/monsterhunterworld/mods/790
- No Rain - https://www.nexusmods.com/monsterhunterworld/mods/75
- Skippable Cutscenes - https://www.nexusmods.com/monsterhunterworld/mods/5540
- Guiding Lands Gathering Indicator - https://www.nexusmods.com/monsterhunterworld/mods/1986
- Easier to spot Guiding Lands Gathering Spots - https://www.nexusmods.com/monsterhunterworld/mods/1972
- All Monster Drops Increased - https://www.nexusmods.com/monsterhunterworld/mods/6556
- Tenderizing Rebalance and Removal - https://www.nexusmods.com/monsterhunterworld/mods/5601
- Permanent Shiny Drops - https://www.nexusmods.com/monsterhunterworld/mods/3456
- Sharpening finish sound replacement__Nice Meme - https://www.nexusmods.com/monsterhunterworld/mods/345
</details>

<details>
<summary>The rest of the files we created using:</summary>

- The rest of the files we created using
- https://github.com/Synthlight/MHW-Editor
- https://github.com/Synthlight/MHW-Editor/wiki
- https://www.nexusmods.com/monsterhunterworld/mods/411
- oo2core_8_win64.dll (got a backup on Google-Drive)
</details>

<h2>Changelog:</h2>

  <details>
  <summary>common\item\itemData.itm</summary>
    
  - changed item carry limits, especially for healing items as part of the defense rework
  - the following items are now infinite use: 
      - Blast and poison coatings, ammos (aside from para, sleep, cluster and slicing)
      - Cool Drink, Hot Drink, Whetfish Fin, Whetfish Fin+ and Well-done Steak
  - Banned the following items (defense rework): <br>
   Armortalon, Armorcharm, (Mega) Armorskin, (Mega) Demondrug, Ancient Potion


  </details>

  <details>
  <summary>common\facility\shopList.slt</summary>
  
  - add all relevent usable items to the shop and some other items as well
  </details>

  <details>
  <summary>common\pl\pl_param.plp</summary>

  - Gunner Defense Rate 0.7 => 0.55  
  </details>

  <details>
  <summary>common\equip\armor.am_dat</summary>
    
  - SELECT a.P1_Set_Group, a.p2_Variant, a.P3_Type, a.P4_Equip_slot,"Defense",a.Defense*3 WHERE a.Defense> 0
  </details>

  <details>
  <summary>common\equip\skill_data.skl_dat</summary>
  
  - Weakness Exploit DLC nerf reverted, +15/30/50% affinity on weakspots, no softening requirement
  - Focus:
    - charge rate changed from 95/90/85% to 92/85/80%
    - gauge fill rate changed from 5/10/20% to 10/20/35%
  - Partbreaker changed from 10/20/30% to 20/35/50%
  - Slugger changed from 20/30/40/50/60% to 20/40/50/75/100%
  - Stamina Thief from 20/30/40/50/60% to 40/60/80/110/150%
  - Latent Power affinity changed from 10/20/30/40/50/60/70% to 20/30/40/50/60/75/100%
  - Agitator affinity changed from 5/5/7/7/10/15/20% to 5/6/7/8/10/15/20%
  - Peak Performance attack buff changed from 5/10/20 to 10/18/25
  - Heroics:
   - attack changed from 0/5/5/10/15/25/40% to 3/6/9/12/15/25/40%
   - defense changed from 50/50/100/100/100/150/150 to 50/60/70/80/100/125/150
  - Marathon Runner stamina usage rate changed from 85/70/50% to 75/60/50%
  - Stamina Surge stamina recovery increase changed from 10/20/30% to 10/25/40%
  - Quick Sheath changed from 110/120/140 to 120/140/155
  - Item Prolonger changed from 10/25/50% to 33/66/100%
  - Free Meal changed from 25/50/75% to 20/35/50%
  - Maximum Might:
    - affinity changed from 10/20/30/40/40% to 10/20/30/40/50% 
    - max stamina time requirement removed (from 5/5/5/5/0s)
    - persisting buff duration changed from 2/3/3/4/0s to 0/0/0/1/2s



  </details>
  
  <details>
  <summary>common\pl\music_skill_efc.mske (script for these changes not yet written)</summary>

  - encore no longer extends the duration or boosts the effect of buffs
  - duration of all songs changed to 3min/6min/12min (no maestro/maestro 1/maestro 2)
  - made the following changes to the effects of buffs:
    - Tool Use Drain Reduced (S) from 0.75/0.75 ==> 0.8
    - Tool Use Drain Reduced (L) from 0.75/0.75 ==> 0.7
    - Elemental Attack Boost from 1.08/1.1 ==> 1.12
    - Abnormal Status Atk. Increased from 1.1/1.15 ==> 1.3
    - Defense or Attack Up (S) from 1.1/1.15 ==> 1.12
    - Defense or Attack Up (L) from 1.15/1.2 ==> 1.2
    - Recovery Speed (L) from 3/3 ==> 3
    - Blight Res Up from 5/10 ==> 10
    - Affinity Up and Health Rec. (S) from 15/20 ==> 20
    - Max Stamina Up + Recovery from 50/50 ==> 50
    - Elemental Res Boost (L) from 7/10 ==> 10
    - Health Boost (L) from 50/50 ==> 50
  - replaced the following (S) songs with their (L) versions
    - Earplugs (S) ==> Earplugs (L)
    - Health Boost (S) from 30/30 ==> Health Boost (L)
    - Recovery Speed (S) from 2/2 ==> Recovery Speed (L)
    - Wind Pressure Negated ==> All Wind Pressure Negated
    - Elemental Res Boost (S) from 5/7 ==> Elemental Res Boost (L)
    </details>

  </details>
  <details>
  <summary>toDo list</summary>

  - add certain decos as quest rewards
  - change drop tables
  - hh (dmg and songs) scripts
  - armor script + armor res changes
  - Lance poke and up-poke should deal same dmg
  - buff bow dragon piercer
  </details>