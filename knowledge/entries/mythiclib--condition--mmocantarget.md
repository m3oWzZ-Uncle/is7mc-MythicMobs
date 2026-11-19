# mmoCanTarget

**Loại** `condition` · **Plugin** `mythiclib` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic)

## Chức năng và cú pháp

**FACT · wiki.** Kiểm tra quyền tương tác theo MythicLib. [Trang mục](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic)

Cú pháp đọc trong nguồn: `mmoCanTarget{interaction=SUPPORT_ACTION}`.

## Thuộc tính và mặc định

Phoenix xác nhận hai giá trị SUPPORT_ACTION và OFFENSE_ACTION. Mặc định chưa có bằng chứng ở trang này.

## Chọn target, condition và trigger

Đặt TargetConditions khi lọc từng ứng viên. Xác định caster thực sau SudoSkill.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Support của Sacred Ward. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MythicMobs/Skills/AssistantSkill.yml#L264)

```yaml
  - mmoCanTarget{interaction=SUPPORT_ACTION} true
```

**FACT · YAML.** Offense tại AoE va chạm. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L43)

```yaml
  - skill{s=VKQT_SWORD_DAMAGE} @EntitiesNearOrigin{r=2.5;limit=8;sort=NEAREST;conditions=[- isLiving true - entitytype{t=ARMOR_STAND} false - mmoCanTarget{interaction=OFFENSE_ACTION} true]}
```

**INFERENCE.** Sacred Ward dùng support, Vạn Kiếm dùng offense ở va chạm và AoE.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử ally, enemy, party, vùng bảo vệ và edition cho condition inline.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/multiplayer-safety.md)
