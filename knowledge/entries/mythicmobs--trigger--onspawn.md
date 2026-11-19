# onSpawn

**Loại** `trigger` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onSpawn)

## Chức năng và cú pháp

**FACT · wiki.** Gọi skill khi Mythic mob spawn. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onSpawn)

Cú pháp đọc trong nguồn: `~onSpawn`.

## Thuộc tính và mặc định

Trang trigger không công bố mặc định thời gian.

## Chọn target, condition và trigger

Gắn khởi tạo vào mob. Dùng @self để khởi tạo chính thực thể.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Đặt score ban đầu. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L17)

```yaml
  - modifytargetscore{objective=drama;action=set;value=0} @Self ~onSpawn
```

**FACT · YAML.** Gắn model khi spawn. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_mobs.yml#L12)

```yaml
  - model{usestatemachine=true;mid=vankiemquytong_sword;lockpitch=true} @self ~onSpawn
```

**INFERENCE.** Vạn Kiếm gắn model, Conductor đặt score và tạo marker.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử spawn trực tiếp, load lại và các phụ thuộc model.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
