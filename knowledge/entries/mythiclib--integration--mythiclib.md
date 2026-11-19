# MythicLib

**Loại** `integration` · **Plugin** `mythiclib` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic)

## Chức năng và cú pháp

**FACT · wiki.** Nối custom skill của MythicLib tới metaskill MythicMobs. [Trang mục](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic)

Cú pháp đọc trong nguồn: `source: mythicmobs:SkillId`.

## Thuộc tính và mặc định

Tài liệu mô tả source, trigger, parameters và extra-skills. Bản ví dụ cũ dùng mythicmobs-skill-id, cần kiểm tra build trước khi đổi.

## Chọn target, condition và trigger

Xác định nguồn modifier và caller thật. Kiểm tra registry trước khi thử damage.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Source của LCCV_SUMMONED. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_mythiclib.yml#L41)

```yaml
  source: mythicmobs:luccotchivuong
```

**FACT · YAML.** Mapping Sacred Ward cũ. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/Mythiclib/skill/AS_ML_SKILL.yml#L15)

```yaml
  mythicmobs-skill-id: Assistant_SKILL_3_MMOCORE
```

**INFERENCE.** Lục Cốt dùng source, Assistant dùng khóa bridge cũ.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử tương thích plugin, giá trị modifier, cast trực tiếp so với class.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/cau-noi-mmocore-mythiclib.md)
