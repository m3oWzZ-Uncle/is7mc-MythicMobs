# offgcd

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/offgcd)

## Chức năng và cú pháp

**FACT · wiki.** Xét global cooldown của caster. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/offgcd)

Cú pháp đọc trong nguồn: `offgcd`.

## Thuộc tính và mặc định

GCD do mechanic globalcooldown thiết lập theo tick; condition không có thuộc tính riêng được nêu.

## Chọn target, condition và trigger

Thêm vào Conditions của những nhánh cùng dùng cooldown chung.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Teleport kiểm tra GCD. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L81)

```yaml
  - offgcd
```

**FACT · YAML.** Ultimate đặt GCD. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L203)

```yaml
  - gcd{ticks=650}
```

**INFERENCE.** Các đòn Conductor có offgcd cạnh guard Drama, ultimate đặt GCD dài.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử timer chồng cùng tick và nhánh chưa khai báo offgcd.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
