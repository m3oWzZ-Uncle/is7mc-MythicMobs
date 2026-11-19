# TargetConditions

**Loại** `condition-context` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#targetconditions)

## Chức năng và cú pháp

**FACT · wiki.** Lọc các mục tiêu kế thừa trước khi xử lý hiệu ứng. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#targetconditions)

Cú pháp đọc trong nguồn: `TargetConditions:`.

## Thuộc tính và mặc định

Các condition thuộc loại tương thích với đầu vào entity/location. CancelIfNoTargets được mô tả riêng.

## Chọn target, condition và trigger

Dùng cho support, ownership hoặc lọc target; giữ target kế thừa ở dòng thực thi nếu muốn giữ kết quả lọc.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Lọc quyền SUPPORT_ACTION. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MythicMobs/Skills/AssistantSkill.yml#L264)

```yaml
  - mmoCanTarget{interaction=SUPPORT_ACTION} true
```

**FACT · YAML.** Lọc owner của thương rơi. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L157)

```yaml
  - owner{} true
```

**INFERENCE.** Sacred Ward lọc support, Xích Huyết lọc owner và stack.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử target rỗng, mixed candidates và dòng con override target.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/conditional-skills.md)
