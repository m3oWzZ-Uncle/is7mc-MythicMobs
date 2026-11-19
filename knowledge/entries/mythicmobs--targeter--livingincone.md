# LivingInCone

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** `@EIC`, `@entitiesInCone`, `@LEIC`, `@livingEntitiesInCone`, `EIC`, `entitiesInCone`, `LEIC`, `livingEntitiesInCone`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone)

## Chức năng và cú pháp

**FACT · wiki.** Chọn entity sống trong cone theo hướng. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone)

Cú pháp đọc trong nguồn: `@EIC{a=225;r=6.5}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| angle | a | — | 90 |
| range | r | — | 16 |
| rotation | rot | — | 0 |
| usepitch | pitch, p | — | false |
| yoffset | yo | — | 0 |
| livingonly | lo | — | true |

Đọc thuộc tính về góc, khoảng và hướng. Giữ hitbox dự kiến khi chỉnh animation.

## Chọn target, condition và trigger

Dùng cho melee định hướng. Gọi ở đúng tick chạm và kiểm tra lúc lấy hướng.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Hitbox cone cho đòn tay. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L57)

```yaml
  - mmodamage{amount="<mmostat.attack_damage> * (<modifier.damage> / 100)";pkb=false;hnp=true;hp=true;types=SKILL,PHYSICAL} @EIC{a=225;r=6.5}
```

**INFERENCE.** Lục Cốt dùng cone cho đòn tay và vùng tròn cho đòn xoay.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử đổi hướng, khoảng ranh giới, nhiều mục tiêu và ally.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/dong-bo-animation-damage.md)
