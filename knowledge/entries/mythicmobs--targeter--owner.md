# Owner

**FACT · phạm vi theo bản.** Snapshot mô tả owner của mob. Wiki online bổ sung trường hợp dropped item, khi đó chọn người chơi sở hữu item nếu họ đang online. Changelog ghi mở rộng ở 5.14.0. Kiểm tra nhánh owner offline và nhầm owner với parent khi dùng chung helper. [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Targeters/Owner.md), [Wiki online](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner), [Changelog](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#dropitem-owner)

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner)

## Chức năng và cú pháp

**FACT · wiki.** Chọn owner của caster. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Owner)

Cú pháp đọc trong nguồn: `@Owner`.

## Thuộc tính và mặc định

Trang mục ghi không có thuộc tính riêng. Đường lấy owner phụ thuộc loại thực thể.

## Chọn target, condition và trigger

Dùng sau khi đã xác nhận caster là summon có owner. Kiểm tra trường hợp owner vắng mặt.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Projectile quay về owner. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L237)

```yaml
  - projectile{bulletType=MOB;mob=VFX_XHPTT_RETURN_SPEAR;bmd=true;oT=XHPTT_Spear_Return_TICK;oH=XHPTT_Spear_Return_HIT;v=32;i=1;mr=24;hR=0.8;vR=1;hp=true;hnp=false;sE=true;sB=false;hto=true;rlos=false;immuneDelay=20;ham=true} @Owner
```

**INFERENCE.** Xích Huyết nhắm projectile recall về owner, trong khi pickup dùng owner như condition.

## Giới hạn và kiểm chứng

**INFERENCE.** Đo owner đổi world hoặc offline, projectile hụt, và cleanup thương ẩn.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
