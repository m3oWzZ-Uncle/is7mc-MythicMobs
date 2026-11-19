# onDeath

**Loại** `trigger` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDeath)

## Chức năng và cú pháp

**FACT · wiki.** Gọi skill khi Mythic mob chết. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDeath)

Cú pháp đọc trong nguồn: `~onDeath`.

## Thuộc tính và mặc định

Trang mục mô tả trigger. Dò trường chạy sau khi caster chết nếu phải gọi metaskill con.

## Chọn target, condition và trigger

Dùng @Children cho cleanup theo quan hệ. Test riêng despawn và reset.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Cleanup theo quan hệ khi boss chết. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L18)

```yaml
  - remove @Children ~onDeath
```

**FACT · YAML.** Hiệu ứng lúc chết. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L34)

```yaml
  - skill{s=HOL2_DeathEffect} ~onDeath  #Artificial death effect
```

**INFERENCE.** Conductor có nhánh remove con và nhánh hiệu ứng chết riêng.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử chết giữa ultimate, add spawn bằng lệnh và cleanup lặp.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
