# mmodamage

**Loại** `mechanic` · **Plugin** `mythiclib` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic)

## Chức năng và cú pháp

**FACT · wiki.** Gây damage theo hệ thống MythicLib. [Trang mục](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic)

Cú pháp đọc trong nguồn: `mmodamage{amount=...;types=...}`.

## Thuộc tính và mặc định

Phoenix mô tả tham số damage và loại damage MMO. Wiki không cung cấp bảng mặc định đầy đủ cho các tham số riêng trong ví dụ.

## Chọn target, condition và trigger

Áp lên target hợp lệ. Dùng guard OFFENSE_ACTION khi cần tuân thủ chính sách tương tác MMO.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Damage theo stat và modifier. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L47)

```yaml
  - mmodamage{amount="<mmostat.attack_damage> * (<modifier.damage> / 100)";pkb=false;hnp=true;hp=true;types=SKILL,PHYSICAL}
```

**FACT · YAML.** Cùng công thức với hitbox khác. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L57)

```yaml
  - mmodamage{amount="<mmostat.attack_damage> * (<modifier.damage> / 100)";pkb=false;hnp=true;hp=true;types=SKILL,PHYSICAL} @EIC{a=225;r=6.5}
```

**INFERENCE.** Vạn Kiếm lấy attack_damage nhân modifier; Lục Cốt dùng cùng công thức với cone.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử modifier từ đúng bridge, giáp/stat MMO, PvP và tương thích bản.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/damage-hit-detection.md)
