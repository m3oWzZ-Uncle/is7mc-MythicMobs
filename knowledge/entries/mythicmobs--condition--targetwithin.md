# targetwithin

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/targetwithin)

## Chức năng và cú pháp

**FACT · wiki.** Kiểm tra khoảng cách tới target của caster. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/targetwithin)

Cú pháp đọc trong nguồn: `targetwithin{d=24}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/targetwithin#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| distance | d | — | 0 |

Đọc khoảng cách trong bảng. Xác định target hiện tại trước khi diễn giải guard.

## Chọn target, condition và trigger

Đặt ở Conditions khi boss chỉ được dùng chiêu lúc có target đủ gần.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Guard tích lũy drama. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L36)

```yaml
  - targetwithin{d=24}
```

**FACT · YAML.** Guard ultimate. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L200)

```yaml
  - targetwithin{d=24}
```

**INFERENCE.** Conductor dùng 24 block cho tích lũy drama và cho ultimate.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử không có target, mép ranh giới, đổi aggro và target khác world.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/conditional-skills.md)
