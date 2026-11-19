# aura

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `buff`, `debuff`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura)

## Chức năng và cú pháp

**FACT · wiki.** Gắn hiệu ứng có thời hạn, stack, điều kiện hủy và callback. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura)

Cú pháp đọc trong nguồn: `aura{auraName=...;duration=...} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| auraName | aura, b, buff, buffname, debuff, debuffname, n, name | — | — |
| components | component, comp | — | — |
| auratype | auragroup, group, type, g | — | — |
| tags | tag | — | — |
| attachmenttype | attachment, attach | — | NONE |
| onStartSkill | onStart, os | — | — |
| onTickSkill | onTick, ot | — | — |
| onEndSkill | onEnd, oe | — | — |
| ShowBarTimer | bartimer, bt | — | false |
| Charges | c | — | 0 |
| Duration | ticks, t, d, time, t | — | 200 |
| Interval | i | — | 1 |
| maxStacks | ms | — | 1 |
| refreshDuration | rd | — | true |
| mergeSameCaster | msc, mc | — | false if any among mergeAll, overwriteAll or overwriteSameCaster is true |
| mergeAll | ma | — | false |
| overwriteSameCaster | osc, oc | — | false |
| overwriteAll | overwrite, ow | — | false |
| CancelOnGiveDamage | cogd | — | false |
| CancelOnTakeDamage | cotd | — | false |
| CancelOnDeath | cod | — | true |
| CancelOnCasterDeath | cocd | — | false |
| CancelOnTeleport | cot | — | false |
| CancelOnChangeWorld | cocw | — | false |
| CancelOnSkillUse | cosu | — | false |
| CancelOnQuit | coq | — | true |
| DoEndSkillOnTerminate | desot, alwaysrunendskill, ares | — | true |

[Modelengine attachment](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura#modelengine-attachment)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| attachmentmodel | attachmodel, model | — | — |
| attachmentstate | attachstate, state | — | — |
| attachmentcolor | attachcolor | — | — |
| attachmentscale | attachscale | — | 1 |
| attachmentViewRadius | attackviewradius | — | -1 |
| attachmentEnchanted | attachEnchanted, enchanted | — | false |
| attachmentGlowing | attachGlowing, glowing | — | false |
| attachmentglowcolor | attachglowcolor | — | — |
| attachmentCulling | attachCulling, culling | — | true |
| attachmentoffset | attachoffset | — | 0,0,0,0,0 |

[Showbartimer attribute](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura#showbartimer-attribute)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| bartimerdisplay | bartimertext | — | auraname |
| bartimercolor | — | — | RED |
| bartimerstyle | — | — | SOLID |

Ưu tiên đọc duration/interval, refreshDuration và các cờ merge/overwrite. Kiểm tra hủy theo target hay caster và callback khi kết thúc. Nhóm attachment và boss bar áp dụng khi dùng chức năng tương ứng.

## Chọn target, condition và trigger

Dùng @self cho trạng thái cast, target kế thừa cho cờ áp lên người bị hit. Chọn tên nhất quán với guard/cleanup.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Đặt CASTING ở entry. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L3)

```yaml
  - aura{auraName=CASTING;duration=280} @self
```

**FACT · YAML.** Đặt aura ngắn trong callback hit. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L137)

```yaml
  - aura{auraName=immunedelay;duration=5}
```

**INFERENCE.** Vạn Kiếm đánh dấu CASTING, Xích Huyết lưu charge trên target của callback.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử refresh, stack, logout, remove chủ động và nhiều caster dùng chung tên aura. Component thay đổi qua các bản.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
