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
  - Banned the following items (defense rework):
  - Powertalon, Powercharm, Armortalon, Armorcharm, Demon Powder, Mega Armorskin, Armorskin, Mega Demondrug, Demondrug, Ancient Potion


  </details>

  <details>
  <summary>common\facility\shopList.slt</summary>
  
  - add lots of stuff to the shop
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
  
  </details>
  
  <details>
  <summary>common\pl\music_skill_efc.mske (script for these changes not yet written)</summary>

  - encore no longer extends the duration or boosts the effect of buffs
  - duration of all songs changed to 3min/6min/12min (no maestro/maestro 1/maestro 2)
  - made the following changes to the effects of buffs:
    - Tool Use Drain Reduced (S): from 0.75/0.75 ==> 0.8
    - Tool Use Drain Reduced (L): from 0.75/0.75 ==> 0.7
    - Elemental Attack Boost: from 1.08/1.1 ==> 1.12
    - Abnormal Status Atk. Increased: from 1.1/1.15 ==> 1.3
    - Defense or Attack Up (S): from 1.1/1.15 ==> 1.12
    - Defense or Attack Up (L): from 1.15/1.2 ==> 1.2
    - Recovery Speed (S): from 2/2 ==> 2
    - Recovery Speed (L): from 3/3 ==> 3
    - Blight Res Up: from 5/10 ==> 10
    - Elemental Res Boost (S): from 5/7 ==> 7
    - Elemental Res Boost (L): from 7/10 ==> 10
    - Affinity Up and Health Rec. (S): from 15/20 ==> 20
    - Health Boost (S): from 30/30 ==> 30
    - Health Boost (L): from 50/50 ==> 50
    - Max Stamina Up + Recovery: from 50/50 ==> 50
  
  </details>
  <details>
  <summary>hm\wp\wp05\music_skill.msk</summary>
  
  </details>
