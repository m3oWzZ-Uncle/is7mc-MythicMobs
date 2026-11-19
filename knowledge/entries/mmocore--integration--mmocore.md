# MMOCore

**Loại** `integration` · **Plugin** `mmocore` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://docs.phoenixdevt.fr/mmocore/skills/config.html)

## Chức năng và cú pháp

**FACT · wiki.** Khai báo skill class người chơi và ngữ cảnh active/passive của MMOCore. [Trang mục](https://docs.phoenixdevt.fr/mmocore/skills/config.html)

Cú pháp đọc trong nguồn: `skills:`.

## Thuộc tính và mặc định

Phoenix mô tả level, max-level, unlocked-by-default, needs-bound và trigger trong class. Bản dataset có khóa passive-type cần đối chiếu build.

## Chọn target, condition và trigger

Truy ID class tới MythicLib rồi tới MythicMobs. Xác nhận đúng trigger và modifier.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Sacred Ward xuất hiện trong class. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MMOCore/classes/Assistant.yml#L32)

```yaml
    SACRED_WARD:
```

**FACT · YAML.** Khóa passive ở bản nguồn. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MMOCore/Skills/holy-cry.yml#L11)

```yaml
passive-type: TIMER
```

**INFERENCE.** Assistant có Sacred Ward và Holy Cry, dùng hai đường active/passive cần thử riêng.

## Giới hạn và kiểm chứng

**INFERENCE.** Kiểm tra cooldown nhiều lớp, resource cost và dạng trigger theo phiên bản.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/cau-noi-mmocore-mythiclib.md)
