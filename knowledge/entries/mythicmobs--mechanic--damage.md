# damage

**FACT · thay đổi 5.14.0.** Snapshot chưa ghi `then` (alias của `onDamage`), `<skill.var.damage-dealt>` và `triggerSkillDamage`. Changelog mô tả `then` chạy theo mục tiêu đã nhận damage và nêu ngoại lệ hit bị khiên chặn vẫn tính là landed. `triggerSkillDamage` phối hợp với `ts=true` nếu cần cả hai trigger. Kiểm thử immunity, khiên, giáp và callback trước khi dùng để tính hồi máu hoặc điểm combo. [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/damage.md), [Changelog](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#damage)

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `d`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/damage)

## Chức năng và cú pháp

**FACT · wiki.** Gây damage lên entity đã chọn. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/damage)

Cú pháp đọc trong nguồn: `damage{amount=...} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Non inheritable attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/damage#non-inheritable-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| amount | a | — | 1 |

[Inheritable attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/damage#inheritable-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| ignoreArmor | ia, i | — | false |
| preventknockback | pkb, pk | — | false |
| preventimmunity | pi | — | false |
| damagecause | dc, cause | — | entity_attack |
| ignoreenchantments | ignoreenchants, ie | — | false |
| noanger | na | — | false |
| ignoreinvulnerability | ignoreinvulnerable, ii | — | false |
| ignoreshield | is | — | false |
| damageshelmet | dh | — | false |
| ignoreeffects | ieff | — | false |
| ignoreresistance | ir | — | false |
| poweraffectsdamage | pad | — | true |
| tags | tag | — | — |
| rawtags | rtag | — | — |
| damagetype | element, e | — | — |
| triggerSkills | ts | — | false |
| bonusdamage | — | — | — |
| bonusdamagemodifiers | bonusdamagemods | — | — |

amount là đầu vào. Các cờ bỏ qua giáp, enchantment, effect, resistance, shield và invulnerability xử lý các lớp khác nhau. preventimmunity liên quan cửa miễn nhiễm, còn triggerSkills ảnh hưởng event liên kết.

## Chọn target, condition và trigger

Dùng target onHit kế thừa khi đánh người vừa bị chạm. Dùng targeter vùng và condition riêng khi đòn là AoE.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Fishball khai báo lượng damage 2 và tùy chọn knockback. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L121)

```yaml
  - damage{a=2;pkb=true}  #Modify damage here
```

**INFERENCE.** Fishball khai báo damage trực tiếp. Lục Cốt gọi mmodamage cho công thức theo stat MMO.

## Giới hạn và kiểm chứng

**INFERENCE.** Đo HP mất, chống hit lặp, miễn nhiễm, damage vanilla và listener plugin. Đối chiếu option với changelog trước khi dùng.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/damage-hit-detection.md)
