# onTimer

**Loại** `trigger` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer)

## Chức năng và cú pháp

**FACT · wiki.** Kích hoạt theo nhịp tick của đồng hồ chung. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer)

Cú pháp đọc trong nguồn: `~onTimer:<ticks>`.

## Thuộc tính và mặc định

Tick dương nằm trong cú pháp trigger. Không thấy bảng mặc định cho trigger; tránh suy từ thời điểm spawn.

## Chọn target, condition và trigger

Khai báo trên mob; chọn target/conditions rõ vì wiki ghi timer không có entity trigger.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Timer tích lũy drama. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L22)

```yaml
  - skill{s=Conductor_DramaMeter_Buildup} ~onTimer:20
```

**FACT · YAML.** Timer gọi Coral Summon. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L25)

```yaml
  - skill{s=Conductor_CoralSummon} ~onTimer:100
```

**INFERENCE.** Conductor kiểm tra drama mỗi 20 tick, các nhánh summon và barrage dùng nhịp khác.

## Giới hạn và kiểm chứng

**INFERENCE.** Đo nhiều mob đồng pha, nhịp thực khi TPS giảm, và tải callback/packet.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/toi-uu-timer-va-callback.md)
