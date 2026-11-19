# summon

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `piratesummon`, `spawnmob`, `spawnmobs`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/summon)

## Chức năng và cú pháp

**FACT · wiki.** Tạo mob theo điểm hoặc entity được chọn. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/summon)

Cú pháp đọc trong nguồn: `summon{type=ID;amount=...} @origin`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/summon#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| type | t, mob, m | — | SKELETON |
| onSummon | onsummonskill, then | — | — |
| amount | a | — | 1 |
| level | l | — | 0 |
| yaw | — | — | — |
| pitch | — | — | — |
| usetargetyaw | uty | — | false |
| usetargetpitch | utp | — | false |
| radius | r, noise, n | — | 0 |
| yRadius | yr, ynoise, yn | — | radius |
| yRadiusUpOnly | yradiusonlyup, yruo, yu | — | false |
| velocity | v, force, f | — | 0 |
| yvelocity | yv, yforce, yf | — | velocity |
| onSurface | os, s | — | false |
| copyThreatTable | ctt | — | false |
| inheritThreatTable | itt | — | false |
| inheritFaction | if | — | true |
| inheritdespawn | inheritdespawnoption, ido | — | false |
| summonerIsOwner | sio | — | true |
| summonerIsParent | sip | — | true |

type và amount chọn mob/số lượng. radius/yRadius/onSurface điều khiển nơi spawn, sio/sip tách owner và parent. Kiểm tra các cờ threat/faction/despawn trước khi áp cho add.

## Chọn target, condition và trigger

Dùng @origin cho điểm va chạm hoặc @self cho quanh boss. Chọn quan hệ owner/parent theo việc cần xác minh hoặc cleanup.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Thương rơi có owner và parent. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L143)

```yaml
  - summon{type=VFX_XHPTT_DROPPED_SPEAR;amount=1;radius=0;yRadius=0;onSurface=true;sio=true;sip=true} @origin
```

**FACT · YAML.** Conductor summon theo lượt. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L218)

```yaml
  - summon{type=HOL2[SYS]_Conductor-RipplesLite;amount=3;r=10;yr=4;os=true;repeat=5;repeatInterval=40} @Self
```

**INFERENCE.** Thương rơi xuất hiện tại điểm end; Conductor xếp nhiều lượt spawn add.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử vị trí không hợp lệ, trần số mob, ownership, chết/despawn và chi phí AI.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
