# Metaskills

**Loại** `metaskill` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills)

## Chức năng và cú pháp

**FACT · wiki.** Định nghĩa skill tree có tên, có thể gọi từ mob và các metaskill khác. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills)

Cú pháp đọc trong nguồn: `InternalSkillName:`.

## Thuộc tính và mặc định

Trang mô tả ID, điều kiện, cooldown, mục tiêu rỗng, failure và target kế thừa. Các khóa có mục riêng trong catalog.

## Chọn target, condition và trigger

Xác định caller, trigger và target kế thừa trước khi đặt guard. Tách child khi dùng lại.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Caller của metaskill wave. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L15)

```yaml
  - skill{s=VKQT_WAVE;repeat=23;repeatInterval=10}
```

**FACT · YAML.** Caller của metaskill damage. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L30)

```yaml
  - skill{s=lccv_danhthuong_Attack_DAMAGE;delay=18}
```

**INFERENCE.** Vạn Kiếm chia entry và wave; Lục Cốt dùng chung damage cho các nhánh tay.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử thiếu ID, không target, cooldown và thay đổi điều kiện sau delay.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/multi-stage-skill.md)
