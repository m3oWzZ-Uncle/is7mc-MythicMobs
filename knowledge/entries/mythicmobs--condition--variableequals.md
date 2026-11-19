# variableequals

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** `vareq`, `varequals`, `variableeq`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableequals)

## Chức năng và cú pháp

**FACT · wiki.** So biến trong scope với giá trị mong đợi. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableequals)

Cú pháp đọc trong nguồn: `varEquals{var=scope.name;value=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableequals#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | — | — |
| value | val, v | — | — |
| scope | s | — | — |

variable, scope và value là ba đầu vào. Kiểm tra kiểu của biến đã khởi tạo trước khi so.

## Chọn target, condition và trigger

Đặt Conditions cho biến caster của form. Khi kiểm tra target, xác nhận đối tượng và scope trỏ đúng entity.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Kiểm tra tay trái. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L21)

```yaml
  - varEquals{var=caster.lccv_hand_1_availability;value=1}
```

**FACT · YAML.** Kiểm tra cả hai tay qua counter. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L70)

```yaml
  - varEquals{var=caster.lccv_hand_count;value=2}
```

**INFERENCE.** Lục Cốt xét tay trái rảnh và xét counter đủ hai tay.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử biến chưa tồn tại, giá trị bị đổi trước callback và kiểu số/text.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
