<html>
<details> <!-- How to use -->
  <summary>How to use</summary>
  <ul>
    <li>Download this repo and add the files to "[...]\Steam\steamapps\common\Monster Hunter World"</li>
    <li>That's it! You can start the game and all mods will be loaded.</li>
  </ul>
</details>
<details> <!-- 3rd party mods included in our bundle -->
  <summary>3rd party mods included in our bundle</summary>
  <ul>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/1982">Stracker's Loader</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/3473">Performance Booster and Plugin Extender</a>
    </li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/3474">Tic Rate Fix</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/790">Camera Zoom</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/75">No Rain</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/5540">Skippable Cutscenes</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/1986">Guiding Lands Gathering Indicator</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/1972">Easier to spot Guiding Lands Gathering
        Spots</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/6556">All Monster Drops Increased</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/5601">Tenderizing Rebalance and Removal</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/3456">Permanent Shiny Drops</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/2459">True weapon damage values</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/345">Sharpening finish sound replacement__Nice
        Meme</a></li>
  </ul>
</details>
<details> <!-- Main tools used for our mods: -->
  <summary>Main tools used for our mods:</summary>
  <ul>
    <li><a href="https://github.com/Synthlight/MHW-Editor/releases">Synthlight's MHW Editor</a></li>
    <li><a href="https://github.com/Synthlight/MHW-Editor/wiki">Synthlight's MHW Editor Wiki</a></li>
    <li><a href="https://www.nexusmods.com/monsterhunterworld/mods/411">MHWNoChunk</a></li>
    <li><a href="https://marketplace.visualstudio.com/items?itemName=mechatroner.rainbow-csv">RBQL / Rainbow CSV for VS
        Code</a></li>
    <li>Our own scripts</li>
    <li>oo2core_8_win64.dll (got a backup on Google-Drive)</li>
  </ul>
</details>
<h3>Changelog:</h3>
<details> <!-- common\item\itemData.itm -->
  <summary>common\item\itemData.itm</summary>
  <ul>
    <li>Changed item carry limits, especially for healing items as part of the healing rework</li>
    <li>You're supposed to get the max amount of items</li>
    <li>The following items are now infinite use:
      <ul>
        <li>Blast and poison coatings, ammos (aside from para, sleep, cluster and slicing)</li>
        <li>Cool drink, hot drink, whetfish fin, whetfish fin+ and well-done steak</li>
      </ul>
    </li>
    <li>Banned the following items (healing rework):<br>
      Armortalon, armorcharm, (mega) armorskin, (mega) demondrug, ancient Potion</li>
  </ul>
</details>
<details> <!-- common\facility\shopList.slt -->
  <summary>common\facility\shopList.slt</summary>
  <ul>
    <li>You can now get all the usable items you'll need during hunts for 1z at the shop. Crafting and cultivating
      plants are no longer required</li>
    <li>Added (gourmet) vouchers, armor spheres, whetfish fins and Zorah Magdaros tickets to the shop</li>
  </ul>
</details>
<details> <!-- common\pl\pl_param.plp -->
  <summary>common\pl\pl_param.plp</summary>
  <ul>
    <li>Gunner defense rate 0.7 ⇒ 0.55 (healing rework)</li>
  </ul>
</details>
<details> <!-- common\equip\armor.am_dat -->
  <summary>common\equip\armor.am_dat</summary>
  <ul>
    <li>SELECT a.P1_Set_Group, a.p2_Variant, a.P3_Type, a.P4_Equip_slot, "Defense", a.Defense*3 WHERE a.Defense> 0</li>
  </ul>
</details>
<details> <!-- common\equip\skill_data.skl_dat -->
  <summary>common\equip\skill_data.skl_dat</summary>
  <ul>
    <li>Weakness exploit DLC nerf reverted, +15/30/50% affinity on weakspots, no softening requirement</li>
    <li>Focus:
      <ul>
        <li>Charge rate changed from 95/90/85% to 92/85/80%</li>
        <li>Gauge fill rate changed from 5/10/20% to 10/20/35%</li>
      </ul>
    </li>
    <li>Partbreaker changed from 10/20/30% to 20/35/50%</li>
    <li>Slugger changed from 20/30/40/50/60% to 20/40/50/75/100%</li>
    <li>Stamina thief from 20/30/40/50/60% to 40/60/80/110/150%</li>
    <li>Latent power affinity changed from 10/20/30/40/50/60/70% to 20/30/40/50/60/75/100%</li>
    <li>Agitator affinity changed from 5/5/7/7/10/15/20% to 5/6/7/8/10/15/20%</li>
    <li>Peak performance attack buff changed from 5/10/20 to 10/18/25</li>
    <li>Heroics:
      <ul>
        <li>Attack changed from 0/5/5/10/15/25/40% to 3/6/9/12/15/25/40%</li>
        <li>Defense changed from 50/50/100/100/100/150/150 to 50/60/70/80/100/125/150</li>
      </ul>
    </li>
    <li>Marathon runner stamina usage rate changed from 85/70/50% to 75/60/50%</li>
    <li>Stamina surge stamina recovery increase changed from 10/20/30% to 10/25/40%</li>
    <li>Quick sheath changed from 110/120/140 to 120/140/155</li>
    <li>Item prolonger changed from 10/25/50% to 33/66/100%</li>
    <li>Free meal changed from 25/50/75% to 20/35/50%</li>
    <li>Maximum might:
      <ul>
        <li>Affinity changed from 10/20/30/40/40% to 10/20/30/40/50%</li>
        <li>Max stamina time requirement removed (from 5/5/5/5/0s)</li>
        <li>Persisting buff duration changed from 2/3/3/4/0s to 0/0/0/1/2s</li>
      </ul>
    </li>
  </ul>
</details>
<details> <!-- Hunting Horn (wp05) -->
  <summary><b>Hunting Horn (wp05)</b></summary>
  <u>common\pl\music_skill_efc.mske (script for these changes not yet written)</u>
  <ul>
    <li>Encore no longer extends the duration or boosts the effect of buffs</li>
    <li>Duration of all songs changed to 3min/6min/12min (no maestro/maestro 1/maestro 2)</li>
    <li>Made the following changes to the effects of buffs:
      <ul>
        <li>Tool Use Drain Reduced (S) from 0.75/0.75 ⇒ 0.8</li>
        <li>Tool Use Drain Reduced (L) from 0.75/0.75 ⇒ 0.7</li>
        <li>Elemental Attack Boost from 1.08/1.1 ⇒ 1.12</li>
        <li>Abnormal Status Atk. Increased from 1.1/1.15 ⇒ 1.3</li>
        <li>Defense or Attack Up (S) from 1.1/1.15 ⇒ 1.12</li>
        <li>Defense or Attack Up (L) from 1.15/1.2 ⇒ 1.2</li>
        <li>Recovery Speed (L) from 3/3 ⇒ 3</li>
        <li>Blight Res Up from 5/10 ⇒ 10</li>
        <li>Affinity Up and Health Rec. (S) from 15/20 ⇒ 20</li>
        <li>Max Stamina Up + Recovery from 50/50 ⇒ 50</li>
        <li>Elemental Res Boost (L) from 7/10 ⇒ 10</li>
        <li>Health Boost (L) from 50/50 ⇒ 50</li>
      </ul>
    <li>Replaced the following (S) songs with their (L) versions
      <ul>
        <li>Earplugs (S) ⇒ Earplugs (L)</li>
        <li>Health Boost (S) from 30/30 ⇒ Health Boost (L)</li>
        <li>Recovery Speed (S) from 2/2 ⇒ Recovery Speed (L)</li>
        <li>Wind Pressure Negated ⇒ All Wind Pressure Negated</li>
        <li>Elemental Res Boost (S) from 5/7 ⇒ Elemental Res Boost (L)</li>
      </ul>
    </li>
</details>
<details> <!-- Lance (wp06) -->
  <summary><b>Lance (wp06)</b></summary>
  <u>hm\wp\wp06\collision\wp06.col & hm\wp\wp06\collision\wp06_01.col</u>
</details>
<details> <!-- Bow (wp11) -->
  <summary><b>Bow (wp11)</b></summary>
  <u>hm\wp\wp11\wp11_param.w11p</u>
  <ul>
    <li>Status Coating Buildup Multiplier unchanged at 1/1.2/1.4/1.6 (Charge 1/2/3/4)</li>
    <li>Power Coating Damage unchanged at 1.35</li>
    <li>Close Range Coating Damage unchanged at 1.18</li>
    <li>Close Range Coating Critical Start Multiplier unchanged at 0.1</li>
    <li>Close Range Coating Critical End Multiplier unchanged at 0.6</li>
    <li>Amount of Arrows Shot unchanged</li>
  </ul>
</details>
<details> <!-- toDo list -->
  <summary>toDo list</summary>
  <ul>
    <li>Add certain decos as quest rewards</li>
    <li>Change drop tables</li>
    <li>hh dmg*1.35 and songs scripts</li>
    <li>Armor defense & negative res scripts</li>
    <li>Lance dmg*1.2 script (poke and up-poke same dmg)</li>
    <li>Buff bow dragon piercer, Buff Raw Bow</li>
    <li>Change gun ammo (pierce, spread, normal, sticky, slicing)</li>
    <li>Switch axe: nerf Power Phials, buff overall dmg</li>
    <li>Fix Kulve Taroth</li>
    <li>Buff clutch claw motion values by 50% each</li>
    <li>Change lifesteal</li>
    <li>Change "Long Range" and "Close Range"</li>
    <li>Buff defense augment</li>
    <li>Buff defense on weapons</li>
  </ul>
</details>