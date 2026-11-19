# setvariable

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `setvar`, `variableset`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setvariable)

## Chức năng và cú pháp

**FACT · wiki.** Ghi giá trị có kiểu vào scope đã chọn. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setvariable)

Cú pháp đọc trong nguồn: `setvariable{var=scope.name;value=...;type=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Inheritable attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setvariable#inheritable-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| variable | name, n, var, key, k | — | — |
| scope | s | — | SKILL |
| save | — | — | false |
| duration | d, e, expire | — | Infinite |

[Non inheritable attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setvariable#non-inheritable-attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| value | val, v, amount, a | — | — |
| type | t | — | INTEGER |

variable/scope chỉ nơi lưu. value/type phải tương thích. save/duration cần kiểm tra khả năng áp dụng theo scope. Bảng tách nhóm inheritable.

## Chọn target, condition và trigger

Dùng SKILL cho dữ liệu cast, CASTER cho trạng thái cần chia sẻ giữa các lần gọi cùng caster. Đặt khởi tạo trước guard đọc biến.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Offset FLOAT trong skill tree. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L27)

```yaml
  - setvariable{var=skill.vkqt_side;type=FLOAT;value=<random.float.-9to9>}
```

**FACT · YAML.** Counter của caster khi khởi tạo form. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_backgroung.yml#L10)

```yaml
          - setvariable{var=caster.lccv_hand_count;value=2}
```

**INFERENCE.** Vạn Kiếm lưu offset float, Lục Cốt lưu số tay rảnh.

## Giới hạn và kiểm chứng

**INFERENCE.** Kiểm tra ghi đè trước khi callback đọc, khởi tạo lại và biến bị xóa khi aura hết.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
