# onAttack

**Loại** `trigger` · **Plugin** `mythicmobs` · **Alias** `onHit`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onAttack)

## Chức năng và cú pháp

**FACT · wiki.** Gọi skill khi mob đánh entity. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onAttack)

Cú pháp đọc trong nguồn: `~onAttack`.

## Thuộc tính và mặc định

Các điều kiện/damage liên quan thuộc skill gọi. Không thấy giá trị mặc định ở cấp trigger.

## Chọn target, condition và trigger

Chọn đối tượng gây/nhận hiệu ứng theo event và dùng sync khi cần hủy event.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Entry hủy melee. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L19)

```yaml
  - skill{s=Conductor_CancelMelee;sync=true} ~onAttack
```

**INFERENCE.** Conductor dùng điểm vào để chặn melee và chạy pattern timer riêng.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử event hủy, damage plugin và việc damage quay lại onAttack.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/huy-event-dong-bo.md)
