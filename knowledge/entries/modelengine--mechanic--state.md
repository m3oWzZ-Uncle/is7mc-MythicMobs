# State

**Loại** `mechanic` · **Plugin** `modelengine` · **Alias** `animation`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State)

## Chức năng và cú pháp

**FACT · wiki.** Phát hoặc dừng state animation của ModelEngine. [Trang mục](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State)

Cú pháp đọc trong nguồn: `state{s=...} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| modelid | m, mid, model | String | — |
| srcmodelid | src, sid, srcmodel | String | — |
| state | s | String | — |
| remove | r | Boolean | false |

[When remove false](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State#when-remove-false)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| speed | sp | Double | 1 |
| lerpin | li | Integer | 0 |
| lerpout | lo | Integer | 0 |
| force | f | Boolean | true |
| priority | p, pr | Integer | 1 |
| loop | l | Loop Mode | — |
| override | ov | Override Mode | — |
| skiplastframe | skip | Boolean | — |
| merge | mg | Boolean | false |
| zero | ez | Boolean | — |

[When remove true](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State#when-remove-true)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| ignorelerp | i | Boolean | false |
| priority | p, pr | Integer | 1 |

modelid/srcmodelid và state chọn model/animation; remove chia hai bảng. speed/lerpin/lerpout thay đổi thời gian hiển thị, priority có ngữ cảnh hệ animation.

## Chọn target, condition và trigger

Chọn entity đã gắn model. Nếu model ở child, đổi caster cho nhánh animation và giữ đường hit riêng theo người chơi.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Model con phát taytraiattack. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L27)

```yaml
      - state{s=taytraiattack} @self
```

**FACT · YAML.** Nhánh hai tay phát haitayattack. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L80)

```yaml
      - state{s=haitayattack} @self
```

**INFERENCE.** Lục Cốt phát state tay trái hoặc hai tay, tùy nhánh.

## Giới hạn và kiểm chứng

**INFERENCE.** Đo mốc visual thực tế, addon build, tên state, model load, tốc độ và FPS.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/dong-bo-animation-damage.md)
