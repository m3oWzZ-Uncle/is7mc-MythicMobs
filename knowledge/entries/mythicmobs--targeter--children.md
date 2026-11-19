# Children

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** `@child`, `@summons`, `child`, `summons`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Children)

## Chức năng và cú pháp

**FACT · wiki.** Chọn entity con đã summon theo quan hệ của caster. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Children)

Cú pháp đọc trong nguồn: `@Children`.

## Thuộc tính và mặc định

Trang mục ghi không có thuộc tính riêng. Tùy chọn chung dùng để lọc, sort và giới hạn khi có hỗ trợ.

## Chọn target, condition và trigger

Dùng cho signal, animation và cleanup thuộc caster. Nếu cần một child, dùng lọc đúng loại và trần rõ.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Cleanup toàn tập child. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Mobs/Conductor.yml#L18)

```yaml
  - remove @Children ~onDeath
```

**FACT · YAML.** Chọn một child đúng loại. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L215)

```yaml
  - sudoskill{s=XHPTT_Spear_Return_CAST;setcasterastrigger=true} @Children{sort=NEAREST;limit=1;conditions=[- mythicmobtype{t=VFX_XHPTT_DROPPED_SPEAR} true - distance{d=<14} true]}
```

**INFERENCE.** Conductor dọn mọi child, Xích Huyết chọn một thương gần nhất.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử player caster, owner/parent, mob sinh bằng command, unload và trận gần nhau.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
