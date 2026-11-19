# PlayersInRadius

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** `@PIR`, `PIR`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRadius)

## Chức năng và cú pháp

**FACT · wiki.** Chọn player quanh caster. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRadius)

Cú pháp đọc trong nguồn: `@PlayersInRadius{r=6}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRadius#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| radius | r | — | 5 |

radius là tầm chọn. Bộ lọc chung và quyền tác động được kiểm tra riêng.

## Chọn target, condition và trigger

Dùng khi chỉ cần player; thêm TargetConditions để phân phe.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Gọi buff vùng r=6. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MythicMobs/Skills/AssistantSkill.yml#L254)

```yaml
  - skill{s=Assistant_SKILL_3_D;repeat="<modifier.duration>";repeatinterval=20} @PIR{r=6}
```

**INFERENCE.** Sacred Ward chọn player r=6 và giao lọc support cho skill con.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử người rời vùng, đổi party giữa repeat và số target khi đông người.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/conditional-skills.md)
