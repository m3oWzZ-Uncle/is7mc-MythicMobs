# BlockMask

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `e:blockMask`, `effect:blockMask`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/BlockMask)

## Chức năng và cú pháp

**FACT · wiki.** Hiển thị mask khối theo vật liệu, vùng và thời lượng. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/BlockMask)

Cú pháp đọc trong nguồn: `effect:blockmask{m=ice;r=20;d=600} @self`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/BlockMask#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| material | mat, m, block, b | — | GRAVEL |
| radius | r | — | 0 |
| radiusy | ry | — | radius |
| noise | n | — | 0 |
| duration | d | — | 0 |
| shape | s | — | SPHERE |
| noair | na | — | true |
| onlyair | oa | — | false |
| audience | — | — | nearby |
| occ | o, oc | — | true |

Đọc radius/radiusY, duration, shape, audience và các cờ chọn block. Duration 0 có ý nghĩa đặc biệt theo wiki.

## Chọn target, condition và trigger

Chọn tâm quanh caster hoặc origin. Chọn audience và thời lượng phù hợp hiệu ứng.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Lớp băng lớn của aura Arctic. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/skills/ArcticKnight.yml#L58)

```yaml
  - effect:blockmask{m=ice;r=20;d=600} @self
```

**INFERENCE.** Các biến thể Arctic đổi trình tự và vật liệu của các lớp mask.

## Giới hạn và kiểm chứng

**INFERENCE.** Đo packet/client FPS, thời gian khôi phục khi nhiều lớp chồng nhau.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/bien-the-cung-id.md)
