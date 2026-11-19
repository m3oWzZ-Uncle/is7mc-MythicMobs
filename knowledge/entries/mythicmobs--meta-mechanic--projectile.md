# projectile

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `p`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile)

## Chức năng và cú pháp

**FACT · wiki.** Phóng projectile có callback theo vòng đời và cấu hình va chạm riêng. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile)

Cú pháp đọc trong nguồn: `projectile{...} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Inheritable attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#inheritable-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| onStartSkill | onStart, oS | — | — |
| onTickSkill | onTick, oT, m, meta, s, skill | — | — |
| onHitSkill | onHit, oH | — | — |
| onEndSkill | onEnd, oE | — | — |
| onBounceSkill | onBounce | — | — |
| onHitBlockSkill | onHitBlock, ohb | — | — |
| onInteractSkill | onInteract | — | — |
| BulletType | bullet, b | — | — |
| Interval | int, i | — | 1 |
| HorizontalRadius | hRadius, hR, r | — | 1.25 |
| VerticalRadius | vRadius, vR | — | 1.25 |
| Duration | maxDuration, md, d | — | 400 |
| MaxRange | mr | — | 40 |
| Velocity | v | — | 5 |
| DeathDelay | death, dd | — | 2 |
| StartYOffset | syo | — | 1 |
| StartFOffset | forwardoffset, sfo | — | 1 |
| TargetYOffset | tyo, targety | — | 0 |
| SideOffset | soffset, so | — | 0 |
| StartSideOffset | ssoffset, sso | — | sideoffset |
| EndSideOffset | endoffset, esoffset, eso | — | sideoffset |
| startingdirection | startingdir, startdir, sdir | — | @Targeted |
| HorizontalOffset | hO | — | 0 |
| VerticalOffset | vO | — | 0 |
| Accuracy | ac, a | — | 1 |
| HorizontalNoise | hn | — | (1-ac)*45 |
| VerticalNoise | vn | — | (1-ac)*4.5 |
| StopAtEntity | sE | — | true |
| StopAtBlock | sB | — | true |
| PowerAffectsRange | par | — | true |
| PowerAffectsVelocity | pav | — | true |
| Interactable | — | — | false |
| HitSelf | — | — | false |
| HitPlayers | hp | — | true |
| HitNonPlayers | hnp | — | false |
| HitTarget | ht | — | true |
| HitTargetOnly | hto | — | false |
| ImmuneDelay | immune, id | — | 2000 |
| hitConditions | conditions, cond, c | — | — |
| stopconditions | stpcond | — | null |
| hitBlockConditions | hbcond | — | — |
| doEndSkillOnHit | esoh | — | true |
| fromorigin | fo | — | false |
| requireLineOfSight | rlos, los, requirelos | — | PLAYERS_ONLY |
| drawHitbox | — | — | false |
| tickinterpolation | interpolation, ti | — | 0 |
| shareSubHitboxCooldown | shcd | — | true |
| hitTargeter | htr | — | — |

[Projectile specific attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#projectile-specific-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| Type | — | — | NORMAL |
| gravity | g | — | 0 |
| Bounces | bounce | — | false |
| BounceVelocity | bv | — | 0.9 |
| HugSurface | hs | — | false |
| HugLiquid | hugwater, huglava | — | false |
| HeightFromSurface | hfs | — | 0.5 |
| MaxClimbHeight | mch | — | 3 |
| MaxDropHeight | mdh | — | 10 |
| highAccuracyMode | ham | — | PLAYERS_ONLY |

[Universal bullet attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#universal-bullet-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletforwardoffset | bulletfo, bulletoffset, bfo | — | 1.8 |
| bulletYOffset | byo | — | 0 |

[Arrow bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#arrow-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| arrowtype | bulletarrowtype | — | NORMAL |

[Block bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#block-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | — | STONE |
| bulletspin | bspin | — | 0 |
| audience | — | — | world |

[Smallblock bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#smallblock-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | — | STONE |
| audience | — | — | world |

[Item bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#item-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | — | STONE |
| bulletModel | model | — | 0 |
| bulletColor | — | — | — |
| bulletmatchdirection | bmd, bulletsmall | — | false |
| bulletEnchanted | enchanted | — | false |
| audience | — | — | world |

[Mob bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#mob-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| mob | mobType, mm | — | SkeletalKnight |
| bulletspin | bspin | — | 0 |
| bulletmatchdirection | bmd | — | false |
| bulletKillable | bk | — | false |
| bulletYOffset | byo | — | 1.35 |
| bulletForwardOffset | bfo | — | 1.35 |

[Tracking bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#tracking-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | — | STONE |
| bulletModel | model | — | 0 |
| bulletColor | — | — | — |
| bulletEnchanted | enchanted | — | false |
| pitch | — | — | 0 |
| yaw | — | — | 0 |
| roll | — | — | 0 |
| rotation | rot | — | 0,0,0 |
| pitchspeed | ps | — | 0 |
| yawspeed | ys | — | 0 |
| rollspeed | rs | — | 0 |
| rotationspeed | rotspeed, rots | — | 0,0,0 |
| audience | — | — | world |

[Realtracking bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#realtracking-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletmaterial | material, mat | — | STONE |
| bulletModel | model | — | 0 |
| bulletColor | — | — | — |
| bulletEnchanted | enchanted | — | false |

[Display bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#display-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletmaterial | material, mat, bulletitem | — | STONE |
| bulletModel | model | — | — |
| bulletcustommodeldata | custommodeldata, cmd | — | 0 |
| bulletColor | — | — | — |
| bulletEnchanted | enchanted | — | false |
| bulletscale | scale | — | 0.5,0.5,0.5 |
| bulletyoffset | byoffset, byo | — | 0.2 |
| bulletBillboarding | bulletBillboard | — | FIXED |
| bulletbrightness | bulletbrightnessblock | — | -1 |
| bulletbrightnesssky | — | — | bulletbrightness |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | — | 50 |
| pitch | — | — | 0 |
| yaw | — | — | 0 |
| roll | — | — | 0 |
| rotation | rot | — | 0,0,0 |
| pitchspeed | ps | — | 0 |
| yawspeed | ys | — | 0 |
| rollspeed | rs | — | 0 |
| rotationspeed | rotspeed, rots | — | 0,0,0 |
| tx | — | — | 0 |
| ty | — | — | 0 |
| tz | — | — | 0 |
| translation | pos, offset | — | 0,0,0 |
| hideFirstTick | hft | — | false |
| bulletCullingHeight | cullHeight | — | 0.0 |
| bulletCullingWidth | cullWidth | — | 0.0 |
| audience | — | — | world |
| bulletgen | generation, bulletgeneration | — | — |

[Me bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#me-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletModel | model | — | — |
| bulletstate | state | — | — |
| bulletcolor | — | — | — |
| bulletscale | — | — | 1 |
| bulletEnchanted | enchanted | — | false |
| bulletGlowing | glowing | — | false |
| bulletglowcolor | — | — | — |
| bulletCulling | culling | — | true |
| bulletViewRadius | — | — | -1 |
| bulletBrightness | — | — | — |
| bulletalod | alod | — | true |

[Text bullet](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/projectile#text-bullet)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bulletText | text | — | * |
| bulletBillboard | billboard | — | CENTER |
| bulletscale | scale | — | 0.5,0.5,0.5 |
| forcedBulletRotation | forcedRotation | — | — |
| bulletRotatesBasedOnDirection | — | — | false |
| bulletyoffset | byoffset, byo | — | 0 |
| bulletforwardoffset | bulletfo, bulletoffset, bfo | — | 1.8 |
| backgroundcolor | color | — | 64,0,0,0 |
| bulletCullingDistance | bulletViewDistance, bulletViewRange | — | 50 |
| bulletCullingHeight | cullHeight | — | 0.0 |
| bulletCullingWidth | cullWidth | — | 0.0 |
| bulletBrightness | bulletBrightnessBlock | — | -1 |
| bulletBrightnessSky | — | — | -1 |
| audience | — | — | world |

Chia thuộc tính theo va chạm (hR/vR, sE/sB, hitConditions), chuyển động (i/v/mr, offset, ham, nội suy) và bullet. Bảng bullet chỉ áp dụng cho loại đã chọn. hitConditions cần Premium theo wiki.

**FACT · offset theo trang chi tiết.** `sso`/`syo` dịch điểm sinh theo ngang/dọc. `eso`/`tyo` dịch điểm ngắm theo ngang/dọc. `hO` xoay vận tốc ban đầu theo phương ngang, `vO` chỉnh độ dốc. Với `@Forward`, `lockpitch=true` tính điểm ngắm như khi caster nhìn ngang. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward)

Snapshot khớp các offset và callback va chạm đã đối chiếu ngày 14/11/2026. Changelog 5.13.0 ghi `hbcond` cho điều kiện trên block, còn `hitConditions` là bộ lọc entity. Nếu cần nổ khi chạm đúng vật liệu, dùng cơ chế block tương thích với build. Khi chỉ cần vùng đứng yên, xem Totem. [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/projectile.md), [Changelog](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#5130), [Totem](../wiki-research/totem.md)

**INFERENCE · kiểm tra đường bay.** Khi cần đường song song, có thể thử dùng chung offset đầu/cuối. Khi cần rải đường bay, lấy offset đầu/cuối độc lập. `mr` là tầm bay tối đa. Điểm ngắm dùng để xác định hướng, còn việc dừng cần đối chiếu với cài đặt va chạm, tầm và thời lượng. [Đối chiếu Vạn Kiếm Quy Tông](../../docs/wiki/doi-chieu-2026-11-14.md#vạn-kiếm-quy-tông)

## Chọn target, condition và trigger

Chọn location để điều khiển đường bay, dùng target kế thừa trong onHit nếu chỉ đánh entity bị chạm và dùng @origin khi xử lý AoE/visual tại projectile.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Kiếm có mob bullet, nội suy và callback va chạm. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L29)

```yaml
  - projectile{bulletType=MOB;mob=VFX_VKQT_SWORD;bmd=true;oT=VKQT_SWORD_TICK;oH=VKQT_SWORD_IMPACT;ohb=VKQT_SWORD_IMPACT;v=32;i=1;mr=32;hR=0.55;vR=0.7;hp=true;hnp=true;sE=true;sB=true;hs=false;sfo=1.5;sso=<skill.var.vkqt_side>;eso=<skill.var.vkqt_side>;syo=<skill.var.vkqt_up>;tyo=<skill.var.vkqt_up>;fo=false;rlos=false;tickinterpolation=2;drawhitbox=false;ham=true;hitConditions=[- isLiving true - mmoCanTarget{interaction=OFFENSE_ACTION} true]} @forward{f=32;y=0;lockpitch=true}
```

**FACT · YAML.** SkyFall có bộ callback riêng. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L178)

```yaml
  - projectile{bulletType=MOB;mob=VFX_XHPTT_SKY_SPEAR;bmd=true;oT=xichhuyetthienthuong_SkyFall_TICK;oH=xichhuyetthienthuong_SkyFall_HIT;oE=xichhuyetthienthuong_SkyFall_END;v=24;i=1;mr=12;hR=0.8;vR=1;hp=true;hnp=true;sE=false;sB=true;syo=10;sfo=6;tyo=0;byo=0;ham=true;tickinterpolation=2;immuneDelay=20;hitConditions=[- isLiving true - mmoCanTarget{interaction=OFFENSE_ACTION} true]}
```

**INFERENCE.** Vạn Kiếm dùng chung callback hit entity/block. SkyFall có callback đường bay và AoE cuối riêng.

## Giới hạn và kiểm chứng

**INFERENCE.** Kiểm tra tường, hit đúp, mục tiêu chạy ngang, nhiều caster và chi phí nội suy.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/projectile-va-cham.md)
