# ModelEngine 4

**Loại** `integration` · **Plugin** `modelengine` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/modelengine/MythicMobs)

## Chức năng và cú pháp

**FACT · wiki.** Tích hợp ModelEngine cung cấp mechanic, condition và targeter cho skill MythicMobs. [Trang mục](https://wiki.mythiccraft.io/modelengine/MythicMobs)

Cú pháp đọc trong nguồn: `model{mid=...} @self`.

## Thuộc tính và mặc định

Trang tích hợp giải thích namespace meg: khi có xung đột. Thuộc tính theo từng mechanic.

## Chọn target, condition và trigger

Gắn model lên đúng entity, đọc ID, animation, hitbox và vòng đời child.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Model kiếm tại spawn. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_mobs.yml#L12)

```yaml
  - model{usestatemachine=true;mid=vankiemquytong_sword;lockpitch=true} @self ~onSpawn
```

**FACT · YAML.** State trên child. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L27)

```yaml
      - state{s=taytraiattack} @self
```

**INFERENCE.** Vạn Kiếm gắn model mob bullet; Lục Cốt chạy state trên model con.

## Giới hạn và kiểm chứng

**INFERENCE.** Kiểm tra bản addon, asset đăng ký, resource pack và chính sách model hitbox.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/dong-bo-animation-damage.md)
