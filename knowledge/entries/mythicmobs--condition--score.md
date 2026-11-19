# score

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/score)

## Chức năng và cú pháp

**FACT · wiki.** Kiểm tra giá trị scoreboard của đối tượng được xét. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/score)

Cú pháp đọc trong nguồn: `score{objective=...;value=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/score#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| objective | obj, o | — | — |
| entry | ent, e | — | — |
| value | val, v | — | — |

objective chọn objective, entry là đầu vào riêng nếu dùng, value chọn giá trị hoặc khoảng. Ô mặc định trống trong nguồn.

## Chọn target, condition và trigger

Đặt Conditions khi score thuộc boss. Dùng từng dải và thử chính xác giá trị sát biên.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Dải Mid. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L64)

```yaml
  - score{objective=drama;value=31to90}
```

**FACT · YAML.** Ngưỡng ultimate. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L199)

```yaml
  - score{objective=drama;value=>119}  #Modify when should the ult be casted here
```

**INFERENCE.** Conductor dùng khoảng Mid và ngưỡng ultimate khác nhau.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử score chưa khởi tạo, 91, 119, reset và hai instance.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
