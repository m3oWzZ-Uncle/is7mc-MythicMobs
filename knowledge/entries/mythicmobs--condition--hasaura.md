# hasaura

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** `hasbuff`, `hasdebuff`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/hasaura)

## Chức năng và cú pháp

**FACT · wiki.** Kiểm tra entity đang giữ aura đã nêu. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/hasaura)

Cú pháp đọc trong nguồn: `hasAura{auraName=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/hasaura#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| aura | auraname, b, buff, buffname, debuff, debuffname, n, name | — | — |

aura là tên cần tìm. Tên phải khớp nơi tạo và dọn aura.

## Chọn target, condition và trigger

Đặt trong Conditions nếu guard theo caster, hoặc TargetConditions nếu guard theo từng người nhận.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Chặn khi có aura xoay. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L5)

```yaml
  - hasAura{auraName=lccv_xoaytay} false
```

**FACT · YAML.** Điều kiện đổi nhánh. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L7)

```yaml
  - hasAura{auraName=lccv_haitay} castinstead lccv_danhthuong_haitay
```

**INFERENCE.** Lục Cốt dùng false để chặn khi đang xoay và castinstead khi aura hai tay tồn tại.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử tên trùng, aura hết giữa delay và nhiều caster cùng ảnh hưởng một target.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/conditional-skills.md)
