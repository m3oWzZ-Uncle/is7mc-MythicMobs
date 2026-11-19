# remove

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `delete`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/remove)

## Chức năng và cú pháp

**FACT · wiki.** Loại entity được chọn. Trang wiki ghi mechanic này không áp dụng cho player. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/remove)

Cú pháp đọc trong nguồn: `remove @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/remove#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| onRemoveSkill | onRemove, then | — | — |

onRemoveSkill/then là callback ghi trong wiki, mặc định để trống. delay là thuộc tính chung khi dùng ở một dòng.

## Chọn target, condition và trigger

Chọn @self trong entity dùng một lần, hoặc @Children theo đúng trận. Kiểm tra quan hệ đối với entity spawn bằng lệnh.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Timeout của thương rơi. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L152)

```yaml
  - remove @self
```

**FACT · YAML.** Boss dọn children khi chết. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L18)

```yaml
  - remove @Children ~onDeath
```

**INFERENCE.** Thương rơi tự dọn sau thời hạn, Conductor dọn con khi chết.

## Giới hạn và kiểm chứng

**INFERENCE.** Kiểm tra cleanup bị gọi hai lần, mất liên kết khi unload và callback dọn tương thích build.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
