# variableunset

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `unsetvar`, `unsetvariable`, `varunset`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/variableunset)

## Chức năng và cú pháp

**FACT · wiki.** Bỏ một biến khỏi scope. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/variableunset)

Cú pháp đọc trong nguồn: `variableUnset{var=scope.name}`.

## Thuộc tính và mặc định

Trang mục dẫn tới nhóm thuộc tính inheritable của SetVariable. Đọc variable và scope ở mục SetVariable trước khi đổi cấu hình.

## Chọn target, condition và trigger

Gọi ở cleanup của scope chứa biến, và kiểm tra guard đọc biến sau khi form kết thúc.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Cleanup counter khi orbital kết thúc. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_backgroung.yml#L16)

```yaml
          - variableUnset{var=caster.lccv_hand_count}
```

**INFERENCE.** Lục Cốt xóa counter và cả hai cờ trong onEnd.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử hết hạn, remove chủ động, callback cũ chạy vào form mới và biến đã bị xóa.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
