# sudoskill

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `sudo`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/sudoskill)

## Chức năng và cú pháp

**FACT · wiki.** Cho entity được chọn làm caster của metaskill con. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/sudoskill)

Cú pháp đọc trong nguồn: `sudoskill{s=ID;setcasterastrigger=true} @Children`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/sudoskill#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| setcasterastrigger | cat | — | false |
| target | t | — | — |
| chained | chain | — | false |

target có thể chọn tập target kế thừa cho child; chained đổi cách chạy trên nhiều entity; setcasterastrigger đổi trigger. Wiki ghi kế thừa thuộc tính của Skill.

## Chọn target, condition và trigger

Dùng @Children có lọc đúng loại hoặc chọn một entity theo luật. Xét owner ở TriggerConditions nếu cần xác thực người gọi ban đầu.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Recall chuyển caster sang thương rơi. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L215)

```yaml
  - sudoskill{s=XHPTT_Spear_Return_CAST;setcasterastrigger=true} @Children{sort=NEAREST;limit=1;conditions=[- mythicmobtype{t=VFX_XHPTT_DROPPED_SPEAR} true - distance{d=<14} true]}
```

**INFERENCE.** Xích Huyết dùng để gọi thương về. Lục Cốt dùng để child phát animation.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử caster/trigger/target bị đổi ra sao, không có child và hai caster đứng gần.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/summon-owner-cleanup.md)
