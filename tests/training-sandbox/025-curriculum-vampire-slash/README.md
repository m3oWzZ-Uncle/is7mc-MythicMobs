# Cấp 2 · Bài 02 · Vampire Slash

**Bài 07 · r2 · Player-cast, PvE.** Vung kiếm một lần với particle vanilla, đánh tối đa một mục tiêu cận chiến và hồi theo 50% sát thương thực, tối đa 3 điểm máu (1,5 tim) mỗi lượt. Các số thử là tầm 3 block, nón có `a=45`, 8 damage gốc và hồi chiêu 3 giây. Mốc đối chiếu là **MythicMobs 5.14.0 Premium**, dùng công thức trong `heal`. [Đề RPG](../../../training/levels/rpg.md#07--vampire-slash) · [Changelog 5.14.0 · Damage](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#damage) · [Hỗ trợ công thức trong Heal](https://wiki.mythiccraft.io/mythicmobs/changelogs/4.7.x_changelogs#mathplaceholders)

## Thiết kế

1. Vung tay ngay lúc cast. `@LivingInCone` chọn mục tiêu gần nhất trong nón. `?@lineofsight` xét đường nhìn sau khi chọn. Nếu mục tiêu chính bị tường che, lượt chém hụt. Player và armor stand bị lọc trong bản PvE. Cách đặt animation trước bước chọn đích giữ cú vung khi hụt, theo kinh nghiệm Dash Cleave. [Living In Cone](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone) · [Changelog 5.14.0 · Conditions](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#conditions) · [Phản hồi Dash Cleave](../../../feedback/corrections/MM-2026-006.md)
2. Metaskill chém giữ cùng thực thể qua `@TargetedTarget`. Nó ghi máu của mục tiêu vào biến `skill.vampire_hp_before` ngay trước `damage`. Đây là trần để cú kết liễu chỉ tính đến lượng máu mục tiêu còn. Scope `skill` thuộc lượt cast và tự hết theo vòng đời skill. Chọn `damage` với lượng cơ sở cố định để tách ảnh hưởng từ giáp của đích khi so hai ca. [Targeted Target](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetedTarget) · [Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes) · [Damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage)
3. `then` gọi nhánh hồi của đòn này. Changelog mô tả `damage-dealt` là sát thương sau giáp và Resistance. Nhánh hồi chỉ chạy khi giá trị này lớn hơn 0, vì callback có thể vẫn được gọi khi khiên chặn. Công thức là `min(3, 0.5 × min(damage-dealt, máu mục tiêu trước đòn))`. Hồi trên `@self`, phụ thuộc vào caster và dữ liệu lượt cast nên nhánh này cho phép thực thi khi mục tiêu đã chết. `heal` mặc định tắt overheal. [Changelog 5.14.0 · Damage](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#damage) · [Math](https://wiki.mythiccraft.io/mythicmobs/Skills/Math) · [Heal](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/heal)

## Hiệu ứng r2

- **Lúc vung kiếm.** Một `sweep_attack` trắng trước mặt làm điểm nhấn. `slash` lấy 16 điểm để vẽ cung chéo đỏ rượu chuyển sang hồng đỏ bằng `dust_color_transition`. `onPoint` chỉ vẽ hạt, còn hitbox tiếp tục do `@LivingInCone` quyết định. Cả hai lớp hiệu ứng được gọi cùng nhịp ra đòn và vẫn xuất hiện khi hụt. Độ nghiêng, tầm nhìn và khoảng cách với đích là các số cần quan sát trong game. [Sweep Attack](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Sweep_Attack) · [Slash](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/slash) · [Dust Color Transition](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle/Particle-Types/Dust_Color_Transition)
- **Lúc hút máu.** Hai hạt tim xuất hiện trên caster nếu đòn gây sát thương dương và caster đang thiếu máu. Phép so máu hiện tại chỉ áp dụng cho dòng particle. Mỗi cast cấu hình tối đa 19 hạt, gồm 1 điểm nhấn, 16 mẫu và 2 hạt tim. [Particle](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle) · [Compare Values](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/CompareValues) · [Phản hồi r1 và diff](../../../feedback/corrections/MM-2026-008.md)

Ảnh hưởng của absorption và plugin sửa sát thương sau callback cần đối chiếu trên build thực tế. Bài thử chính dùng damage core, đích không có absorption và caster thiếu máu trước đòn.

## Thử trong Minecraft

Chép [YAML](Skills/vampire-slash.yml) vào `Skills/` của server thử. Cast khi đứng ở Survival và dùng cùng vị trí, hướng nhìn và vũ khí trong các lượt so sánh. Chờ hơn 3 giây giữa hai lượt của cùng caster. Ghi máu trước và sau khi cast, cô lập hồi máu tự nhiên trong lúc đo. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)

```text
/mm reload
/mm test cast TrainingVampireSlash
/data get entity @s Health
```

Dùng bò đứng yên để kiểm mitigation và tránh nhiễu từ cháy nắng. Đứng ở điểm đặt đích rồi chạy `/summon`. Có thể thêm tag riêng cho từng con nếu đo nhiều đích cùng lúc. Liều Resistance II dưới đây tạo mức giảm đủ rõ để hai ca dễ phân biệt khi áp trần hồi.

```text
/summon minecraft:cow ~ ~ ~ {NoAI:1b,Tags:["training_vampire_slash"]}
/data get entity @e[type=minecraft:cow,tag=training_vampire_slash,sort=nearest,limit=1] Health
/effect give @e[type=minecraft:cow,tag=training_vampire_slash,sort=nearest,limit=1] minecraft:resistance 20 1 true
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `single-target-and-cap` | Đặt hai bò thẳng hàng trước caster trong tầm, ở hai khoảng cách. Chỉ con gần mất máu. Khi đích mất từ 6 điểm máu và caster còn thiếu ít nhất 3 điểm, caster hồi đúng 3 điểm. |
| `mitigation` | So đích trần với đích có Resistance II. Ghi lượng máu mục tiêu mất và lượng caster hồi. Ở lượt giảm sát thương dưới 6 điểm, caster hồi một nửa lượng mất đo được. Có thể kiểm thêm mob có giáp. |
| `miss-and-cover` | Cast vào khoảng trống, rồi thử mob ngoài nón, ngoài tầm hoặc bị tường đặc che. Vẫn vung tay. Cả caster và các đích đều giữ nguyên máu. |
| `immune-or-cancelled` | Gọi bò bằng lệnh mẫu với thêm `Invulnerable:1b`. Cast ở Survival. Máu đích và máu caster giữ nguyên. Nếu server có plugin hủy damage, lặp với một đòn đã được log là hủy. |
| `lethal-hit` | Gọi bò bằng lệnh mẫu với thêm `Health:2.0f`. Khi đòn kết liễu và caster thiếu trên 1 điểm máu, lượng hồi kỳ vọng là 1 điểm. Kiểm cả nhánh callback sau cú kết liễu. |
| `near-full-health` | Khi caster chỉ thiếu 1 điểm máu, đánh đích đầy máu. Caster về tối đa và không có máu vượt trần hoặc tim thêm. |
| `multiplayer` | A và B bị thương, đứng ở hai làn riêng và cast gần đồng thời. Một làn đích đầy máu, một làn đích còn 2 máu. Mỗi player nhận lượng hồi theo đòn của mình. Một người khác đứng ở vùng chém không nhận damage trong bản PvE. |
| `particle-arc-and-heal-cue` | Đặt Particles ở All và dùng ngôi ba hoặc nhờ một người quan sát từ bên cạnh. Cast theo hai hướng vuông góc rồi thử ngắm lên và xuống. Vệt đỏ phải đọc được theo cú vung trước mặt ở tầm cận chiến, không gợi một đòn chém sau lưng. Thử chém hụt, chém đích miễn damage, trúng khi đang thiếu máu và trúng khi đầy máu. Cả bốn lượt có vệt chém, chỉ lượt trúng gây damage dương khi thiếu máu có hạt tim. Ở ca trúng, ghi hình để kiểm vệt và damage cùng nhịp. |

Để đếm nhánh hồi, dùng bản đo riêng trên server thử. Thêm dòng sau vào đầu `Skills` của `TrainingVampireSlashHeal` rồi reload. Mỗi dòng console tương ứng một lần nhánh đã qua điều kiện sát thương dương. Ghi hash của bản đo riêng khi lưu log.

```yaml
- log{message="VampireSlash caster=<caster.name> dealt=<skill.var.damage-dealt> hpBefore=<skill.var.vampire_hp_before>"} @None
```

Nếu cần kiểm đối chứng khiên, dùng bản đo riêng trong arena PvP, đổi `targetplayers=false` thành `targetplayers=true` và thử khi người phòng thủ đứng đối diện, giơ khiên trước lúc cast. Lượt chặn hoàn toàn phải có **0 máu hồi**, kể cả khi engine có gọi callback. Lưu kết quả này cùng build thực tế.

Dọn đích thử bằng `/kill @e[type=minecraft:cow,tag=training_vampire_slash]` trong world thử. Ghi build, edition, log nạp, số đo và xác nhận trong [hồ sơ bài](case.json). Đang chờ gameplay Minecraft.
