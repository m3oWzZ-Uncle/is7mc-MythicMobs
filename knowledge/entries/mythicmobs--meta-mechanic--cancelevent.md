# cancelevent

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/cancelevent)

## Chức năng và cú pháp

**FACT · wiki.** Hủy event làm phát sinh skill. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/cancelevent)

Cú pháp đọc trong nguồn: `CancelEvent`.

## Thuộc tính và mặc định

Trang mục ghi không có thuộc tính riêng. sync=true là yêu cầu thực thi; chạy trước delay.

## Chọn target, condition và trigger

Chọn trigger có event hủy được. Kiểm tra đoạn đầu sync và tách phần hậu xử lý theo luật gameplay.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Dòng gọi sync từ onAttack. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L19)

```yaml
  - skill{s=Conductor_CancelMelee;sync=true} ~onAttack
```

**FACT · YAML.** Metaskill hủy event. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L3)

```yaml
  - CancelEvent
```

**INFERENCE.** Conductor hủy melee bằng một skill ngắn, có các timer riêng cho combat.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử listener khác, triggerSkills, điều kiện event bị hủy và HP trước/sau.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/huy-event-dong-bo.md)
