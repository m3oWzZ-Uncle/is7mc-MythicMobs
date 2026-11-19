# Ring

**Loại** `targeter` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Ring)

## Chức năng và cú pháp

**FACT · wiki.** Trả về tập vị trí trên một vòng. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Ring)

Cú pháp đọc trong nguồn: `@Ring{radius=16;points=60}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Ring#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| radius | r | — | 5 |
| points | p | — | 10 |
| rotationx | rotx, rx | — | 0 |
| rotationy | roty, ry | — | 0 |
| rotationz | rotz, rz | — | 0 |
| offsetx | offx, ox | — | 0 |
| offsety | offy, oy | — | 0 |
| offsetz | offz, oz | — | 0 |
| relative | — | — | false |

radius xác định kích thước. points là số điểm, ảnh hưởng số thao tác downstream.

## Chọn target, condition và trigger

Dùng để phát pattern theo nhiều hướng. Nếu mechanic cần entity, chọn hoặc truy entity ở bước riêng.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Vioar có ring 60 điểm. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L331)

```yaml
  - projectile{oE=Vioar_Aura_Low-END;v=25;mr=16;i=1;hR=1;vR=1;hp=false;sE=false;hs=true} @Ring{radius=16;points=60}
```

**FACT · YAML.** Circle of Might dùng ring nhỏ. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MythicMobs/Skills/AssistantSkill.yml#L60)

```yaml
  - projectile{onTick=Assistant_SKILL_2-Tick;onHit=Assistant_SKILL_2-Hit;onEnd=Assistant_SKILL_2-End;v=8;i=1;hR=1;vR=1;mr=15;sfo=0} @Ring{r=6-10;p=1-3}
```

**INFERENCE.** Vioar dùng ring để phát projectile; Circle of Might dùng ring làm đích của projectile.

## Giới hạn và kiểm chứng

**INFERENCE.** Kiểm tra chi phí theo points, số caster và vị trí không hợp lệ.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/toi-uu-timer-va-callback.md)
