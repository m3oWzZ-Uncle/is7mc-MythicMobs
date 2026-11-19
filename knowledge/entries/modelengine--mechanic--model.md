# Model

**Loại** `mechanic` · **Plugin** `modelengine` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/Model)

## Chức năng và cú pháp

**FACT · wiki.** Thêm hoặc gỡ model ModelEngine trên entity. [Trang mục](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/Model)

Cú pháp đọc trong nguồn: `model{mid=...} @self`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/Model#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| modelid | m, mid, model | String | — |
| remove | r | Boolean | false |

[When remove false](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/Model#when-remove-false)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| hitbox | h | Boolean | true |
| invisible | i, invis | Boolean | true |
| damagetint | d, tint | Boolean | true |
| nametag | n, name | String | — |
| drive | — | Boolean | false |
| ride | — | Boolean | false |
| lockpitch | lp, lpitch | Boolean | false |
| lockyaw | ly, lyaw | Boolean | false |
| step | s | Double | — |
| radius | rad | Integer | 0 |
| viewrange | vr | Double | 4096 |
| scale | — | Double | 1 |
| hitboxscale | — | Double | scale |
| usestatemachine | usm, state, statemachine | Boolean | false |
| initrender | init | Boolean | true |
| showhitbox | — | Boolean | true |
| showshadow | — | Boolean | true |
| syncbody | — | Boolean | true |
| save | — | Boolean | false |
| rootbone | root, rt | String | — |
| track | — | Boolean | true |
| invisupdate | iu | Boolean | false |
| seeself | vs, see | Boolean | true |
| pivot | pv | Boolean | false |
| camerapivot | campivot | Boolean | false |
| renderfire | rf | Boolean | — |
| forcefire | ff | Boolean | — |

[When remove true](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/Model#when-remove-true)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| killowner | ko | Boolean | false |

modelid và remove chọn thao tác. Bảng add có nhóm hitbox/scale, tracking/render, mount và state machine. killowner thuộc nhánh gỡ.

## Chọn target, condition và trigger

Chọn entity giữ model, ví dụ VFX mob tại onSpawn. Xác nhận mid đăng ký và đo hitbox server nếu dùng override.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Model của kiếm gắn khi spawn. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_mobs.yml#L12)

```yaml
  - model{usestatemachine=true;mid=vankiemquytong_sword;lockpitch=true} @self ~onSpawn
```

**FACT · YAML.** Boss gắn model khi spawn. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L14)

```yaml
  - model{mid=the_conductor;nametag=false} @Self ~onSpawn  #Toggle nametag display here
```

**INFERENCE.** Vạn Kiếm gắn model ở mob bullet, Conductor gắn model lên chính boss.

## Giới hạn và kiểm chứng

**INFERENCE.** Tên asset và model ID có thể lệch. Kiểm tra phiên bản ModelEngine, resource pack và mật độ model.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/dong-bo-animation-damage.md)
