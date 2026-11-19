# EntitiesNearOrigin

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** `@ENO`, `ENO`, `NearOrigin`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesNearOrigin)

## Chức năng và cú pháp

**FACT · wiki.** Lấy entity quanh origin của metaskill. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesNearOrigin)

Cú pháp đọc trong nguồn: `@EntitiesNearOrigin{r=...}`.

## Thuộc tính và mặc định

Trang mục ghi kế thừa EntitiesInRadius và không có thuộc tính riêng. sort/limit thuộc targeter chung, target filters có ngữ cảnh edition.

## Chọn target, condition và trigger

Dùng trong callback projectile khi tâm cần là vị trí va chạm. Kết hợp bộ lọc quyền damage và entity sống.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** AoE tại điểm chạm. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L43)

```yaml
  - skill{s=VKQT_SWORD_DAMAGE} @EntitiesNearOrigin{r=2.5;limit=8;sort=NEAREST;conditions=[- isLiving true - entitytype{t=ARMOR_STAND} false - mmoCanTarget{interaction=OFFENSE_ACTION} true]}
```

**FACT · YAML.** AoE tại điểm kết thúc SkyFall. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L196)

```yaml
  - skill{s=xichhuyetthienthuong_SkyFall_IMPACT_DAMAGE} @EntitiesNearOrigin{r=2.25;limit=8;sort=NEAREST;conditions=[- isLiving true - mmoCanTarget{interaction=OFFENSE_ACTION} true]}
```

**INFERENCE.** Vạn Kiếm chọn bán kính 2.5; SkyFall chọn 2.25 ở end.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử lệch tâm, entity đứng sát viền, ally và target limit trong đám đông.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/projectile-va-cham.md)
