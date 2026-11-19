# hasaurastacks

**Loại** `condition` · **Plugin** `mythicmobs` · **Alias** `aurastacks`, `buffstacks`, `debuffstacks`, `hasbuffstacks`, `hasdebuffstacks`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/hasaurastacks)

## Chức năng và cú pháp

**FACT · wiki.** So số stack của aura trên entity đang được xét. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/hasaurastacks)

Cú pháp đọc trong nguồn: `hasaurastacks{auraName=...;stacks=...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/hasaurastacks#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| aura | auraname, b, buff, buffname, debuff, debuffname, n, name | — | — |
| stacks | s | — | 1 |

aura chọn tên, stacks là điều kiện số lượng. Dùng action true/false theo luật cụ thể.

## Chọn target, condition và trigger

Ở pickup, đặt target condition trên người nhặt. Ở recall, xét stack caster trước khi chọn child.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Guard trên người nhặt. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L158)

```yaml
  - hasaurastacks{auraName=XHPTT_SPEAR_CHARGE;stacks=2} false
```

**FACT · YAML.** Guard ở entry Recall. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L213)

```yaml
  - hasaurastacks{auraName=XHPTT_SPEAR_CHARGE;stacks=2} false
```

**INFERENCE.** Xích Huyết dùng guard cùng tên aura ở cả pickup và recall.

## Giới hạn và kiểm chứng

**INFERENCE.** Test đúng ngưỡng, refresh, tiêu hao stack và hai callback cùng tick.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
