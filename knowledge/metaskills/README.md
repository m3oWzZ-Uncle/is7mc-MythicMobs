# Metaskills

Mốc đọc **MythicMobs 5.14.0**. Metaskill gom một danh sách mechanic dưới ID nội bộ. Từ `Skills` của mob, `skill{s=ID}` gọi metaskill khi trigger trên dòng mob xảy ra. Skill khác cũng có thể gọi ID đó. [Nguồn và phiên bản](../../docs/wiki/README.md), [Metaskills, revision đã đối chiếu](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078), [Skill](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill)

| Trường hoặc hành vi | Cách đọc |
| --- | --- |
| ID nội bộ | Dùng một ID duy nhất, không có khoảng trắng. Theo dõi tham chiếu từ mob và các callback. |
| `Skills` | Danh sách mechanic. Dùng `delay` để đọc mốc thời gian trong chuỗi. |
| `Cooldown` | Với dạng số, thời gian giữa hai lần thực thi của metaskill trên cùng caster tính bằng giây. `OnCooldownSkill` có thể chạy nhánh riêng khi còn cooldown. |
| `CancelIfNoTargets` | Wiki ghi mặc định `true`. Kiểm thử khi targeter rỗng hoặc `TargetConditions` loại hết mục tiêu. Changelog dòng 5.1.x ghi tùy chọn đặt `false`. |
| Target kế thừa | Targeter trên dòng gọi cung cấp mục tiêu cho các dòng con. Dòng con có targeter riêng sẽ chọn mục tiêu theo dòng đó. |
| Điều kiện | `Conditions`, `TargetConditions` và `TriggerConditions` xét các đối tượng khác nhau. `FailedConditionsSkill` cung cấp nhánh khi condition fail theo mô tả wiki. |

[Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078), [Targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters), [Changelog 5.1.x](https://wiki.mythiccraft.io/mythicmobs/changelogs/5.1.x_changelogs)

## Các lựa chọn ảnh hưởng hành vi

- Một mechanic gắn trực tiếp trên mob phù hợp với một hành động độc lập. Dùng metaskill có tên khi cần nhiều bước, điều kiện/cooldown riêng hoặc gọi từ nhiều nơi. Theo dõi số lần trigger gọi cùng ID khi cooldown dùng chung theo caster. [Skills](https://wiki.mythiccraft.io/mythicmobs/Skills/Skills), [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078)
- **5.12.0** thêm `Charges` và `CooldownMode`. Với skill có charges, ghi số lượt cast liên tiếp và thời điểm từng lượt dùng lại được. Khi đối chiếu cấu hình từ build cũ hơn, kiểm tra mục này trong changelog trước. [Changelog 5.12.0 mục Charges / CooldownMode](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd)
- `branch=true` trên mechanic `skill` tạo nhánh skill tree. Trang `Skill` ghi rằng thay đổi trong nhánh không phản ánh ngược về cây cha. Nếu cần dữ liệu đi qua nhánh, kiểm thử cả giá trị ban đầu ở nhánh và giá trị ở cây cha sau khi ghi. [Skill, Branch Attribute](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill#branch-attribute)
- Khóa số ít `Skill` trong định nghĩa metaskill có hành vi ghép danh sách mechanic của metaskill kia, bỏ qua cooldown và conditions của skill được ghép theo phần mô tả chi tiết của wiki. Nếu cần các guard của skill con, dùng mechanic `skill` trong danh sách `Skills` và thử nhánh cooldown/điều kiện. Skill Parameters được wiki đánh dấu Premium. `Hidden: true` cho metaskill được ghi trong changelog **5.14.0**. [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078), [Changelog 5.14.0](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd#5140)

[Ví dụ mob và metaskill](../../examples/simple/README.md) có điểm gọi từ `~onInteract`, target kế thừa, `TargetConditions`, delay và cooldown để kiểm tra riêng từng phần.
