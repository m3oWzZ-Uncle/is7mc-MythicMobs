# EntitiesInRadius

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** `@allInRadius`, `@EIR`, `@livingEntitiesInRadius`, `@livingInRadius`, `allInRadius`, `EIR`, `entitiesnearby`, `livingEntitiesInRadius`, `livingInRadius`, `nearbyentities`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRadius)

## Chức năng và cú pháp

**FACT · wiki.** Chọn entity quanh caster theo bán kính và bộ lọc. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRadius)

Cú pháp đọc trong nguồn: `@EntitiesInRadius{r=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRadius#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| shape | — | — | SPHERE |
| livingonly | living, l | — | true |

radius và các tùy chọn hình/loại entity phải đọc theo trang và build. sort/limit là thuộc tính targeter chung.

## Chọn target, condition và trigger

Dùng quanh caster. Dùng EntitiesNearOrigin nếu tâm là projectile callback.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** AoE xoay dùng EIR. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L117)

```yaml
  - mmodamage{amount="<mmostat.attack_damage> * (<modifier.damage> / 100) * 0.25";pkb=false;hnp=true;hp=true;types=SKILL,PHYSICAL} @EIR{r=5.5} ?hasAura{auraName=luccotchivuong}
```

**FACT · YAML.** So với cone của đòn thường. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L57)

```yaml
  - mmodamage{amount="<mmostat.attack_damage> * (<modifier.damage> / 100)";pkb=false;hnp=true;hp=true;types=SKILL,PHYSICAL} @EIC{a=225;r=6.5}
```

**INFERENCE.** Lục Cốt dùng EIR cho đòn xoay và EIC cho đòn có hướng.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử ally/pet, viền radius, số ứng viên và tổng số hit trên chuỗi lặp.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/damage-hit-detection.md)
