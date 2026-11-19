# SKILL

**Loại** `variable-scope` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes)

## Chức năng và cú pháp

**FACT · wiki.** Giữ giá trị trong skill tree hiện hành. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes)

Cú pháp đọc trong nguồn: `var=skill.name`.

## Thuộc tính và mặc định

Tên scope được công bố trong bảng Variables. Dữ liệu có vòng đời của cây và có thể được child truy cập.

## Chọn target, condition và trigger

Dùng cho offset, cờ của một cast hoặc giá trị truyền giữa child. Đọc branch nếu cần cách ly.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Offset dạng FLOAT. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L27)

```yaml
  - setvariable{var=skill.vkqt_side;type=FLOAT;value=<random.float.-9to9>}
```

**FACT · YAML.** Cờ lượt cast. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L9)

```yaml
  - setvariable{var=skill.casted;v=0} @caster
```

**INFERENCE.** Vạn Kiếm lưu offset; Lục Cốt lưu cờ đã chọn nhánh.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử hai cast, thời điểm đọc callback và việc ghi đè trong cùng cây.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
