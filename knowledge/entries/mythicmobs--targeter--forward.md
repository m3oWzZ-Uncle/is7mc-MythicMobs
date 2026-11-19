# Forward

Đối chiếu ngày 14/11/2026 cho thấy `forward`, `rotate`, `useeyelocation` và `lockpitch` khớp giữa bản nhập và wiki online. Dùng `@Forward` khi cần điểm theo góc nhìn. Khi đòn cần bám entity đang di chuyển, chọn cơ chế homing và targeter theo entity. Nếu đòn chếch lên/xuống, kiểm tra `lockpitch` trước khi chỉnh `tyo`. [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Targeters/Forward.md), [Missile](mythicmobs--meta-mechanic--missile.md)

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward)

## Chức năng và cú pháp

**FACT · wiki.** Tạo vị trí phía trước caster. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward)

Cú pháp đọc trong nguồn: `@Forward{f=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| forward | f, amount, a | — | 5 |
| rotate | rot | — | 0 |
| useeyelocation | uel | — | false |
| lockpitch | — | — | false |

forward/rotate điều khiển độ xa và hướng xoay. useeyelocation và lockpitch thay đổi cách lấy hướng; offsets chung cần xem trang Targeters.

## Chọn target, condition và trigger

Dùng cho đường bay có hướng theo caster. Nếu gameplay khóa hướng tại wind-up, kiểm tra lúc targeter được đánh giá.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Chọn vị trí phía trước cho kiếm. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L29)

```yaml
  - projectile{bulletType=MOB;mob=VFX_VKQT_SWORD;bmd=true;oT=VKQT_SWORD_TICK;oH=VKQT_SWORD_IMPACT;ohb=VKQT_SWORD_IMPACT;v=32;i=1;mr=32;hR=0.55;vR=0.7;hp=true;hnp=true;sE=true;sB=true;hs=false;sfo=1.5;sso=<skill.var.vkqt_side>;eso=<skill.var.vkqt_side>;syo=<skill.var.vkqt_up>;tyo=<skill.var.vkqt_up>;fo=false;rlos=false;tickinterpolation=2;drawhitbox=false;ham=true;hitConditions=[- isLiving true - mmoCanTarget{interaction=OFFENSE_ACTION} true]} @forward{f=32;y=0;lockpitch=true}
```

**FACT · YAML.** Chọn hướng của dash. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L103)

```yaml
  - lunge{velocity=3.2;velocityY=0} @forward{f=16;y=-1;lockpitch=true}
```

**INFERENCE.** Vạn Kiếm dùng forward làm đích, dash Xích Huyết dùng forward cho chuyển động.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử nhìn lên/xuống, mép địa hình và đổi hướng khi delay.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/movement-combat-ai.md)
