# onSignal

**Loại** `trigger` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onSignal)

## Chức năng và cú pháp

**FACT · wiki.** Gọi skill khi mob nhận signal phù hợp. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onSignal)

Cú pháp đọc trong nguồn: `~onSignal:Mid`.

## Thuộc tính và mặc định

Tên signal là phần sau dấu hai chấm.

## Chọn target, condition và trigger

Dùng quan hệ parent/child và tên riêng cho mỗi luồng. Nhánh nhận đặt guard phù hợp với trạng thái mob nhận.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Vioar xử lý Mid. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L59)

```yaml
  - setstance{s=Mid} @Self ~onSignal:Mid
```

**FACT · YAML.** Boss phát Mid. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L67)

```yaml
  - signal{s=Mid} @Children
```

**INFERENCE.** Boss phát Mid; Vioar nhận và đổi stance.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử add xuất hiện sau tín hiệu, nhiều boss và signal lặp.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
