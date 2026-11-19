# onDamaged

**Loại** `trigger` · **Plugin** `mythicmobs` · **Alias** `onHurt`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDamaged)

## Chức năng và cú pháp

**FACT · wiki.** Gọi skill khi mob nhận damage. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDamaged)

Cú pháp đọc trong nguồn: `~onDamaged`.

## Thuộc tính và mặc định

Trang mục mô tả placeholder damage theo skill tree, cần kiểm tra nguồn event và lúc đọc.

## Chọn target, condition và trigger

Dùng @self cho phản ứng của mob, chọn @trigger khi cần xác định entity gây hit.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Phát âm thanh khi nhận hit. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L32)

```yaml
  - sound{s=entity.polar_bear.hurt;p=0.5;v=1;cd=0.5} @SelfLocation ~onDamaged  #Artificial hurt sound effect
```

**INFERENCE.** Conductor phát âm thanh tại chính mob. Arctic dùng aura phản ứng ở skill người chơi.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử hit bị chặn, môi trường không có attacker và timing HP.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/damage-hit-detection.md)
