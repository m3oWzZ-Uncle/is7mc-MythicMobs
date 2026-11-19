# missile

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `mi`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/missile)

## Chức năng và cú pháp

**FACT · wiki.** Biến thể homing theo dõi mục tiêu. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/missile)

Cú pháp đọc trong nguồn: `missile{...}`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/missile#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| Inertia | in, intertia | — | 1.5 |
| Bounces | bounce | — | false |
| BounceVelocity | bv | — | 0.9 |
| startWithParentVelocity | swpv, spv | — | false |
| HugSurface | hs | — | false |
| HugLiquid | hugwater, huglava | — | false |
| HeightFromSurface | hfs | — | 0.5 |
| MaxClimbHeight | mch | — | 3 |
| MaxDropHeight | mdh | — | 10 |
| highAccuracyMode | ham | — | PLAYERS_ONLY |
| hitnonplayers | hnp | — | true |

Kế thừa các thuộc tính được đánh dấu inheritable của Projectile. Inertia tác động mức đổi hướng, bounce/bounceVelocity cần kiểm tra điều kiện Premium. Kiểm tra default hnp riêng của Missile.

## Chọn target, condition và trigger

Chọn entity rõ ràng cho homing và xét quyền nhận hiệu ứng ở callback hit. Gọi qua đúng bridge nếu đó là skill người chơi.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Ray of Vitalis dùng missile và hai callback. [Dòng YAML gốc](../../incoming/no-model/fullclass/0_VipClass/Assistant/MythicMobs/Skills/AssistantSkill.yml#L41)

```yaml
  - missile{onTick=Assistant_SKILL_1-Tick;onHit=Assistant_SKILL_1-Hit;v=8;i=1;hR=1;vR=1;hnp=false;bounce=true;bv=1.9;ham=false}
```

**INFERENCE.** Assistant dùng missile cho nhánh heal, Circle of Might dùng projectile đến vị trí trên ring.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử target biến mất, đổi world, góc cua và bounce. Kiểm tra target kế thừa của cast thật.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/cau-noi-mmocore-mythiclib.md)
