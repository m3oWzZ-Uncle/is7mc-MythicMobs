# CASTER

**Loại** `variable-scope` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes)

## Chức năng và cú pháp

**FACT · wiki.** Lưu dữ liệu trên thực thể đang cast. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes)

Cú pháp đọc trong nguồn: `var=caster.name`.

## Thuộc tính và mặc định

Caster scope thuộc thực thể. Cấu hình kiểu, thời hạn hoặc lưu phải đọc trang mechanic ghi biến.

## Chọn target, condition và trigger

Dùng cho trạng thái form/counter giữa các cast. Kiểm tra caster sau SudoSkill.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Counter theo caster. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_backgroung.yml#L10)

```yaml
          - setvariable{var=caster.lccv_hand_count;value=2}
```

**FACT · YAML.** Xóa khi kết thúc. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_backgroung.yml#L16)

```yaml
          - variableUnset{var=caster.lccv_hand_count}
```

**INFERENCE.** Lục Cốt đặt counter khi form vào và unset khi form kết thúc.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử tái tạo form, hai caster và callback tới muộn.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
