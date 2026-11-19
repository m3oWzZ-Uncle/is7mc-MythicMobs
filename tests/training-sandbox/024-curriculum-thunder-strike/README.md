# Cấp 2 · Bài 01 · Thunder Strike

**Bài 06 của chương trình · r1 · Player-cast, PvE.** Ngắm mặt trên của một block đầy trong tầm 16 block rồi cast. Vòng sáng báo vùng sét. Sau 20 tick, sét đánh xuống điểm đã báo, gây 6 điểm damage cấu hình trong vùng bán kính 2 block. Hồi chiêu 5 giây theo caster. Các thông số này là mặc định của bài thử. Đối chiếu MythicMobs **5.14.0 Premium**. [Đề RPG](../../../training/levels/rpg.md#06--thunder-strike)

## Thiết kế

1. `@TargetBlock` lấy tọa độ đúng một lần. Targeter bỏ block không khí. Metaskill mặc định dừng nếu không nhận được điểm hợp lệ. Metaskill nhận block nâng origin 0,6 block từ tâm, dự kiến đặt nó cao hơn mặt trên block đầy 0,1 block. Bản thử dùng mặt trên của block đầy. Cần đo lại mốc này nếu muốn dùng slab, cầu thang hoặc mặt bên. [TargetBlock](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/TargetBlock) · [Thuộc tính targeter](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#common-location-targeters-attributes) · [CancelIfNoTargets](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cancelifnotargets)
2. Vòng báo và sét dùng cùng `@origin`. Sau 20 tick, `FakeLightning` vẽ sét và phát âm thanh. Chỉ dòng `damage` gây sát thương. VFX vẫn xuất hiện nếu đích đã rời vùng. Đây là cách tách hiệu ứng khỏi sát thương đã dùng ở Hỏa Cầu Thuật và tách điểm báo khỏi truy vấn mục tiêu như bài Đánh lạc hướng. [FakeLightning](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/FakeLightning) · [Hỏa Cầu Thuật](../../../knowledge/player-skills/projectiles/hoa-cau-thuat.md) · [Đánh lạc hướng](../023-foundation-assessment-decoy/README.md)
3. Tại mốc đánh, `@EntitiesNearOrigin` quét một lần, loại player và armor stand. `lineofsightfromorigin` xét vật cản từ tâm sét để chặn hit xuyên sàn đặc. Thuộc tính `origin` và inline target condition cần Premium theo wiki. Một lượt chỉ tạo một vòng báo, một hiệu ứng sét và một lần truy vấn damage. Tâm sét thuộc lượt cast nên hai người có thể đánh hai vùng riêng. [Thuộc tính mechanic](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#universal-attributes) · [Inline Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Inline-Conditions) · [EntitiesNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesNearOrigin) · [Line of Sight From Origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/lineofsightfromorigin)

## Thử trong Minecraft

Chép [YAML](Skills/thunder-strike.yml) vào `Skills/` của server thử. Chạy lệnh cast bằng người chơi Survival có quyền test. Đánh dấu block ngắm và vị trí đứng. Dùng mặt trên của block đầy. Chờ hơn 5 giây giữa các lượt của cùng một caster. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)

```text
/mm reload
/mm test cast TrainingThunderStrike
```

Có thể dựng đích test bằng lệnh sau ở từng vị trí. Đứng gần đúng con cần đo khi đọc máu. Dùng mái che để zombie không cháy nắng trong ca đo.

```text
/summon minecraft:zombie ~ ~ ~ {NoAI:1b,PersistenceRequired:1b,Tags:["training_thunder_strike"]}
/data get entity @e[type=minecraft:zombie,tag=training_thunder_strike,sort=nearest,limit=1] Health
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `warning-and-single-hit` | Đặt một mob cạnh tâm và một mob ngoài 2 block. Quay video và đo máu. Vòng báo xuất hiện trước. Mob gần mất máu đúng một lần lúc sét đánh, mob xa giữ nguyên. |
| `locked-aim` | Sau khi vòng hiện, lập tức quay về một block khác trước khi sét đánh. Vòng và sét vẫn trùng ở block ban đầu, mob tại điểm ngắm mới giữ nguyên máu. |
| `target-enters-and-leaves` | Đưa mob ban đầu ra ngoài và đưa mob thứ hai vào tâm sau cảnh báo, trước sét. Chỉ mob thứ hai mất máu. Lặp khi vùng trống để kiểm tra sét vẫn xuất hiện. |
| `stacked-floors` | Dựng sàn đầy với hai tầng và nhắm lần lượt từng mặt sàn từ vị trí nhìn được mặt trên. Đặt một mob sát tâm cùng tầng và một mob ở dưới sàn. Nếu cần tách phép thử đường nhìn khỏi bán kính, đặt thêm đích trong tầm 2 block nhưng sau vách chắn đặc, ví dụ dùng heo để tránh kẹt ở khoảng trống thấp. Đích sau vật cản giữ máu. Ghi cao độ tâm và vị trí đích trong mỗi lượt. |
| `no-secondary-damage-or-fire` | Một lượt ở world thử trời quang, có cháy lan, đặt block dễ cháy gần tâm. Sau sét, đếm đúng một lượt mất máu, theo dõi thêm vài giây để chắc không có cháy block hay damage do cháy. |
| `invalid-aim` | Ngắm trời trống, rồi thử ngắm block ngoài tầm. Không có vòng báo, sét hay damage tại chân caster. |
| `multiplayer` | A và B ngắm hai vùng tách biệt và cast gần đồng thời. Mỗi sét đi đúng vùng cảnh báo của người cast. Một người đứng trong vùng sét không mất máu. |

Dọn mob thử bằng `/kill @e[type=minecraft:zombie,tag=training_thunder_strike]` trong world thử. Ghi build, edition, log nạp, kết quả và xác nhận trong [hồ sơ bài](case.json). Điểm cần kiểm tra trên server là cao độ thật của origin, đường nhìn qua sàn, và đúng một lần mất máu khi sét xuất hiện.
