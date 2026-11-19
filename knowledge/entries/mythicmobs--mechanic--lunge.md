# lunge

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/lunge)

## Chức năng và cú pháp

**FACT · wiki.** Áp vận tốc để tạo chuyển động lao. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/lunge)

Cú pháp đọc trong nguồn: `lunge{velocity=...;velocityY=...} @forward`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/lunge#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| velocity | v, magnitude | — | 1 |
| velocityY | vy, yv, yvelocity | — | 1 |
| oldmath | old, o | — | false |

velocity và velocityY cấu hình vận tốc; oldmath chọn cách tính cũ theo trang mục.

## Chọn target, condition và trigger

Chọn hướng/vị trí đầu vào phù hợp. Nếu dash có damage, thiết kế một đường hitbox rõ và kiểm tra cùng hướng.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Dash tiến về vị trí trước mặt. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L103)

```yaml
  - lunge{velocity=3.2;velocityY=0} @forward{f=16;y=-1;lockpitch=true}
```

**INFERENCE.** Xích Huyết dùng lunge cho caster rồi tạo projectile dò hit riêng.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử sát tường, góc dốc, xoay mặt, vận tốc tồn tại và lệch hitbox với đường dịch chuyển.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/movement-combat-ai.md)
