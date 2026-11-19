# Targeters

Mốc đọc **MythicMobs 5.14.0**. Chọn targeter bằng hai thông tin: mechanic cần entity hay location, và vị trí dùng làm tâm hoặc nguồn của lần cast. [Nguồn và phiên bản](../../docs/wiki/README.md), [Targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters)

| Cần lấy | Targeter và ngữ cảnh |
| --- | --- |
| Mob đang cast | `@self` chọn caster. Dùng khi đặt trạng thái lên chính mob. |
| Entity kích hoạt sự kiện | `@trigger` lấy entity của trigger. Với `~onInteract` đó là người tương tác. `~onTimer` không có entity trigger liên kết. |
| Mục tiêu hiện tại của caster | `@target` lấy mục tiêu của caster. Kiểm tra tình huống mob chưa có mục tiêu hoặc đổi mục tiêu trong chuỗi có delay. |
| Mục tiêu từ skill cha | Dòng con có thể kế thừa target từ `skill{…}`. `@TargetedTarget` tham chiếu entity kế thừa. Khi dòng con khai báo targeter khác, targeter đó áp dụng cho dòng con. |
| Vị trí thực thi | `@origin` là vị trí origin của skill, có thể là vị trí projectile trong callback. `@SelfLocation` lấy vị trí caster. |
| Một nhóm người chơi | `@PlayersInRadius` chọn theo bán kính quanh caster. `@PlayersNearOrigin` chọn quanh origin. Xác nhận tâm ở bước va chạm khi muốn đánh AoE. |

[Bảng Targeters và kế thừa](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters), [PlayersInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/PlayersInRadius?version_id=bac0dc7ec57ea2dbb360bd48e311e0bc5071bc9b), [On Interact](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onInteract), [On Timer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer), [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile)

## Lọc, sắp xếp và giới hạn

- Kiểm tra `DefaultEntityFilters` trong `config-skills.yml` của server và các bộ lọc của mechanic/targeter. Khi kết quả khác dự kiến, ghi rõ loại entity, game mode và quan hệ với caster, sau đó thử lại với một đối tượng mỗi loại. [Target Filters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#target-filters), [Config Skills](https://wiki.mythiccraft.io/mythicmobs/config/config-skills)
- Wiki ghi `sort` và `limit` có từ **5.0.4** với entity/location targeters. Ví dụ `@PlayersInRadius{r=12;sort=NEAREST;limit=2}` giới hạn danh sách trả về còn hai người gần origin nhất trong tập đã chọn. Với targeter có nhiều bước, kiểm tra thứ tự lọc, sắp xếp và kết quả khi không đủ mục tiêu. [Target Limits](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#target-limits)
- **5.13.0** thêm filter `mythic`/`vanilla` cho `target`/`ignore` và bộ lọc dành cho các loại display/interaction. **5.14.0** thêm `@bound` cho entity sống trong một vùng, với các hình được mô tả trong changelog. Các targeter từ addon cần đúng plugin và build. [Changelog Targeters](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd), [Additional Targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#additional-targeters)

Trong một bài test, cho A kích hoạt skill, B giữ aggro và C đứng gần điểm va chạm. Ghi ai nhận cảnh báo và ai mất HP. Lặp lại với danh sách rỗng, hai mục tiêu cùng tầm, và một mục tiêu rời tầm trong lúc delay. Xem [metaskills](../metaskills/README.md) và [projectile](../mechanics/README.md).
