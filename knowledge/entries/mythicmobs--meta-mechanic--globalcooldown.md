# globalcooldown

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `gcd`, `setgcd`, `setglobalcooldown`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/globalcooldown)

## Chức năng và cú pháp

**FACT · wiki.** Đặt GCD trên caster để condition offgcd có thể khóa nhánh. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/globalcooldown)

Cú pháp đọc trong nguồn: `gcd{ticks=650}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/globalcooldown#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| ticks | t | — | 20 |

ticks là thời lượng theo tick. Cơ chế tác động lên caster.

## Chọn target, condition và trigger

Thêm offgcd vào đúng nhánh cần chia sẻ GCD. Giữ cooldown metaskill riêng cho thời gian hồi của từng chiêu.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Ultimate đặt GCD 650 tick. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L203)

```yaml
  - gcd{ticks=650}
```

**INFERENCE.** Ultimate Conductor đặt GCD dài, các nhánh khác có độ dài GCD riêng.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử hai timer cùng tick, nhánh thiếu offgcd và GCD hết trước cleanup của ultimate.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
