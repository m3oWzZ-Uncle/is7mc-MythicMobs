# stance

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/stance)

## Chức năng và cú pháp

**FACT · wiki.** So trạng thái stance của entity đang xét. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/stance)

Cú pháp đọc trong nguồn: `stance{s=Mid}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/stance#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| stance | s | — | DEFAULT |
| strict | str | — | true |

stance chọn giá trị so; mặc định theo bảng wiki nếu có.

## Chọn target, condition và trigger

Xét caster khi chuyển phase, dùng action phù hợp để tránh gửi signal lặp.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Guard stance của phase Mid. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L65)

```yaml
  - stance{s=Mid} cancel
```

**INFERENCE.** Nhánh Mid của Conductor so stance trước khi phát signal và ghi trạng thái.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử thiếu stance, case tên, reset và chuyển phase nhanh.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
