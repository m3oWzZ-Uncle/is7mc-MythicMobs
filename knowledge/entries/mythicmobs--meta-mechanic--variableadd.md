# variableadd

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `addVar`, `addVariable`, `incrementVariable`, `varAdd`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/variableadd)

## Chức năng và cú pháp

**FACT · wiki.** Cập nhật biến theo thao tác cộng của kiểu đang dùng. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/variableadd)

Cú pháp đọc trong nguồn: `variableadd{var=...;value=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/variableadd#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| amount | a, value, val, v | — | 0 |

amount là giá trị cộng. Cần đối chiếu hành vi theo kiểu và các thuộc tính kế thừa từ SetVariable.

## Chọn target, condition và trigger

Chỉ cập nhật trên đúng caster giữ counter. Guard nhánh giữ/hồi tay trước khi cộng để tránh gọi lặp.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Giữ tay làm counter giảm. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L24)

```yaml
  - variableadd{var=caster.lccv_hand_count;value=-1} @caster
```

**FACT · YAML.** Hồi tay làm counter tăng nếu form còn. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L34)

```yaml
  - variableadd{var=caster.lccv_hand_count;value=1} @caster ?hasAura{auraName=luccotchivuong}
```

**INFERENCE.** Lục Cốt trừ 1 khi giữ tay và cộng 1 khi hồi.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử biến thiếu, sai kiểu, giá trị âm, hồi hai lần và counter lệch cờ.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
