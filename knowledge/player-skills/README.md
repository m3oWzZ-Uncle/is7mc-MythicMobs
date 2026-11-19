# Player Skills

Tra theo hành vi người chơi cần thực hiện. Một file trong `Skills/` chỉ định nghĩa metaskill. Caller cho biết ai cast, nguồn kích hoạt, và dữ liệu truyền vào. Một mob dùng làm model, projectile hoặc summon có thể có callback riêng với caster khác. [Skill Trees](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees)

| Nếu đang làm | Đọc |
| --- | --- |
| Bài thực hành thuật toán và skill nhiều module | [Advanced](advanced/README.md) |
| Kinh nghiệm từ lần thử và sửa trước | [Chỉ mục bài học thực hành](practice-lessons.md) |
| Chương trình thực hành từ Foundation đến Expert | [40 đề Player Skill](../../training/curriculum.md) |
| Active skill, utility, kích hoạt từ class hoặc item | [Active](active/README.md) |
| Passive theo sự kiện, aura hoặc timer | [Passive](passive/README.md) |
| Dash, đổi vị trí hoặc nâng người thi triển | [Movement](movement/README.md) |
| Kiếm, võ thuật, phòng thủ, hồi máu hoặc summon | [Combat](combat/README.md) |
| Kiếm khí, phép bay, va chạm và sát thương | [Projectiles](projectiles/README.md) |
| Combo, nhiều giai đoạn hoặc cửa sổ ngắt | [Combos](combos/README.md) |
| ModelEngine, timing và cleanup VFX | [ModelEngine](modelengine/README.md) |
| MMOItems/MMOCore, MythicLib, mana, stamina và cooldown | [Integrations](integrations/README.md) |

## Truy ngữ cảnh trước khi sửa

1. Tìm entry từ lệnh, event, item, class hoặc registry. Ghi caster và trigger nếu entry cấp chúng. `@self` lấy caster hiện tại, `@trigger` lấy thực thể gây sự kiện khi có, và target kế thừa có thể đã được chọn bởi caller. Kiểm tra lại sau `sudoskill`. [Skill Trees](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees) · [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills)
2. Đối với projectile, xác định origin của callback và mục tiêu va chạm. Đối với summon, lần theo owner, skill của summon và nơi dọn. Chọn scope biến theo vòng đời cần thiết, ví dụ scope của skill tree khi dữ liệu chỉ dùng trong lượt cast. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) · [Scope biến](../patterns/variable-scope.md) · [Summon có owner](../patterns/summon-owner-cleanup.md)
3. Ghi hệ thống xử lý chi phí, hồi chiêu, điều kiện PvP/PvE và việc hủy khi chúng thuộc yêu cầu. Chạy thử qua đúng đường gọi thực tế. Lệnh test có thể cô lập metaskill; các ca item và class cần thử qua plugin gọi. [Quy trình test](../../tests/training-sandbox/README.md)

Các mục dưới đây phân biệt nguồn wiki, điều đọc được trong YAML và điều cần kiểm thử. MythicMobs 5.14.0 là mốc đối chiếu của repo. Lấy build và edition thực tế của từng server và addon trước khi kết luận tương thích. [Nguồn và phiên bản](../../docs/wiki/README.md)
