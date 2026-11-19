# Kiểm tra cuối Cấp 1 · Đánh lạc hướng

**CT-BM-04 · r1 · Player-cast, PvE.** Báo một vùng trước mặt. Sau 20 tick, chém đúng vùng đã báo kể cả khi caster quay mặt hoặc bước sang bên. Mục tiêu còn trong vùng tại tick chém nhận một lượt damage. Chém hụt vẫn hiện hiệu ứng kết thúc. Đây là ca arena phẳng, vùng tròn bán kính 2 block trên sàn, cách vị trí cast 3 block theo yaw lúc cast. Damage cấu hình là 4 điểm, hồi chiêu 4 giây theo caster. Hiệu ứng dùng particle. Mốc đối chiếu là MythicMobs 5.14.0 và hồ sơ không khai báo addon. [Đề CT-BM-04](../../training-benchmarks/curriculum.md)

## Vì sao chọn cách này

- **Điểm chém được chọn một lần.** Metaskill chính dùng `@Forward{f=3;lockpitch=true}` để truyền tọa độ. Metaskill nhận tọa độ dùng `@TargetedLocation` cho cả hai hiệu ứng và `@LivingNearTargetLocation` để chọn mục tiêu khi chém. Cách này dựa vào target kế thừa của mỗi lần gọi và không cần biến chung hay đánh dấu mob. Cần xác minh việc giữ tọa độ qua delay và truy vấn quanh location kế thừa trên build thực tế. [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills) · [Targeted Location](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetedLocation) · [Living Near Target Location](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingNearTargetLocation)
- **Hiệu ứng chém và damage cùng nhịp.** Vòng chém chạy sau `delay 20` và trước dòng damage. Khi vùng trống, dòng hiệu ứng vẫn có tọa độ. Chỉ dòng damage truy vấn thực thể và lọc player, armor stand. Thiết kế có một lần truy vấn damage và không tạo model, entity phụ hoặc vòng lặp nền. Tái sử dụng phần phù hợp của bài Toàn Phong Trảm và phản hồi Dash Cleave về chém hụt. [Delay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/delay) · [ParticleRing](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ParticleRing) · [Target filters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#target-filters) · [Bài 05](../022-curriculum-whirlwind/README.md) · [Dash Cleave](../../../feedback/corrections/MM-2026-006.md)
- **Lựa chọn khác.** Một Totem cố định có thể làm tâm nếu gameplay cần để lại vùng nhiều nhịp. Ca này chỉ có một đòn theo vị trí đã báo nên dùng tọa độ kế thừa. Kinh nghiệm dùng model báo hiệu và model chém 180° thuộc biến thể có asset. [Totem](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/totem) · [Quyết định về model và vùng damage](../../../feedback/decisions/MM-D-2026-005.md)

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên server thử. Dùng arena phẳng, thoáng, đích PvE cùng cao độ và player Survival. Chạy lệnh cast bằng player có quyền, từ trong game. Giữ hai lần cast của cùng người cách nhau hơn 4 giây trừ ca thử hồi chiêu. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)

```text
/mm reload
/mm test cast TrainingFoundationDecoy
```

Có thể dùng các zombie đứng yên có tag riêng để dễ di chuyển, so máu và dọn sau bài. Đứng đúng điểm cần đặt đích để chạy lệnh summon. Chạy lệnh đọc máu trước và sau mỗi lượt trên đích gần nhất, hoặc thêm tag riêng cho từng con. Thử dưới mái che để tránh nắng làm sai số.

```text
/summon minecraft:zombie ~ ~ ~ {NoAI:1b,PersistenceRequired:1b,Tags:["training_ct_bm_04"]}
/data get entity @e[type=minecraft:zombie,tag=training_ct_bm_04,sort=nearest,limit=1] Health
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `warning-then-hit` | Một mob tại tâm, một mob ngoài biên rõ ràng trên cùng tầng. Vòng báo hiện ngay. Chỉ mob trong biên mất máu đúng một lần ở nhịp vòng chém. |
| `turn-and-step` | Đặt một đích ở vùng sẽ báo và một đích ở phía nhìn mới ngoài vùng cũ. Cast, bước sang bên rồi quay 90° hoặc 180° trước impact. Vòng chém vẫn ở vùng cũ và chỉ đích vùng cũ mất máu. |
| `early-target-swap` | Nhờ người thứ hai đưa mob X ra ngoài và mob Y vào tâm ngay sau cảnh báo. X giữ máu, Y nhận một lượt damage. |
| `late-target-swap` | Lặp với đổi đích ngay trước vòng chém. Ghi hình để xác nhận cả hai đã tới vị trí mới trước impact. Lượt đổi sau impact là đối chứng: chỉ X nhận damage. |
| `empty-swing` | Đưa mọi mob ra ngoài trước impact. Vẫn hiện vòng chém ở vùng đã báo. |
| `multiplayer-and-cooldown` | A và B báo vào hai vùng tách biệt gần đồng thời. Đặt một mob trong mỗi vùng và một người đứng trong vùng để thử lọc PvP. Cả hai vùng chém độc lập, người trong vùng giữ máu. A cast lại ngay vẫn trong hồi chiêu và không tạo vòng báo mới. |

Sau khi thử có thể dọn các mob thử bằng `/kill @e[type=minecraft:zombie,tag=training_ct_bm_04]` trong world thử. Ghi build, edition, log nạp, kết quả và xác nhận theo từng ca vào [hồ sơ](case.json). Kết quả server và gameplay đang chờ kiểm thử.
