# BodyRotation

**Loại** `mechanic` · **Plugin** `modelengine` · **Alias** `bodyclamp`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/BodyRotation)

## Chức năng và cú pháp

**FACT · wiki.** Điều khiển quay thân model theo cơ chế ModelEngine. [Trang mục](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/BodyRotation)

Cú pháp đọc trong nguồn: `BodyRotation{...} @self`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/BodyRotation#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| headuneven | hu, head | Boolean | Last Value |
| maxhead | mh, mxh | Float | Last Value |
| minhead | mnh | Float | Last Value |
| bodyuneven | bu, body | Boolean | Last Value |
| maxbody | mb, mxb | Float | Last Value |
| minbody | mnb | Float | Last Value |
| playermode | m, mode, player | Boolean | Last Value |
| stable | s | Float | Last Value |
| rdelay | rde | Integer | Last Value |
| rduration | rdu | Integer | Last Value |

Đọc các tùy chọn player mode, độ ổn định và thời gian quay theo bảng của build.

## Chọn target, condition và trigger

Dùng trên entity đã gắn model, kiểm tra hình quay theo hướng khi spawn hoặc dash.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Cấu hình quay thân ở slash. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_mobs.yml#L12)

```yaml
  - BodyRotation{playermode=false;stable=0;rdelay=0;rduration=0} @self ~onSpawn
```

**INFERENCE.** Xích Huyết áp BodyRotation ở các mob VFX slash và dash.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử client góc nhìn khác nhau, quay giữa cast và phiên bản ModelEngine.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/movement-combat-ai.md)
