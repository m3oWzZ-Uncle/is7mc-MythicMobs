# setstance

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `stance`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setstance)

## Chức năng và cú pháp

**FACT · wiki.** Ghi stance lên Mythic mob để các condition có thể xét trạng thái. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setstance)

Cú pháp đọc trong nguồn: `setstance{s=...} @self`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/setstance#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| stance | s | — | default |

stance là giá trị cần ghi. Trang mục giới hạn tác dụng vào Mythic mob.

## Chọn target, condition và trigger

Ghi đúng mob, guard stance hiện tại khi chỉ muốn thực hiện side effect ở lúc chuyển.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Boss đổi stance sau khi báo con. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L68)

```yaml
  - setstance{s=Mid} @Self
```

**FACT · YAML.** Vioar nhận signal và đổi stance. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L59)

```yaml
  - setstance{s=Mid} @Self ~onSignal:Mid
```

**INFERENCE.** Conductor đổi stance của chính nó; Vioar đổi stance trong trigger nhận signal.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử reset, nhận signal lặp và trạng thái sau despawn/respawn.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
