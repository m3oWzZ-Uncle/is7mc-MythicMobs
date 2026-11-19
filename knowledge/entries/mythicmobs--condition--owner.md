# owner

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** `isOwner`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/owner)

## Chức năng và cú pháp

**FACT · wiki.** Kiểm tra entity đang xét có là chủ của caster theo loại entity hay không. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/owner)

Cú pháp đọc trong nguồn: `owner true`.

## Thuộc tính và mặc định

Trang mục ghi không có thuộc tính riêng. Wiki mô tả cách xét khác nhau cho tameable, mob thường và dropped item.

## Chọn target, condition và trigger

Sau SudoSkill, xét TriggerConditions nếu chủ ban đầu trở thành trigger. Dùng TargetConditions khi xét người nhận pickup.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Owner condition trong pickup. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L157)

```yaml
  - owner{} true
```

**FACT · YAML.** Owner condition ở trigger recall. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L220)

```yaml
  - owner true
```

**INFERENCE.** Xích Huyết dùng owner ở cả pickup và recall.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử hai chủ, owner offline, entity không có owner và ownership khác parent.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
