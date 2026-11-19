# Mechanics

Mốc đọc **MythicMobs 5.14.0**. Các mô tả dưới đây lấy từ wiki và changelog. [Nguồn và phiên bản](../../docs/wiki/README.md)

| Nhóm | Cách đọc một cấu hình | Nguồn |
| --- | --- | --- |
| Dòng skill | Trong `Skills` của mob, trigger cho biết lúc gọi, targeter chọn đầu vào và mechanic thực hiện tác vụ. Health modifier và chance là phần tùy chọn của dòng mob. Trigger đặt tại điểm gọi từ mob. | [Skills](https://wiki.mythiccraft.io/mythicmobs/Skills/Skills), [Triggers](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers) |
| Hiệu ứng và timing | `message` gửi chat cho player được chọn. `delay 20` dời phần tiếp theo của skill tree 20 tick. Thuộc tính `delay` trên một mechanic dời mechanic đó. `cooldown` dạng số dùng giây, còn `repeatInterval` và `targetInterval` dạng số dùng tick. | [Message](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/message), [Delay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/delay), [Universal Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics#universal-attributes) |
| Damage | Đọc lượng damage khai báo cùng các tùy chọn giáp, miễn nhiễm và trigger liên quan. Khi test, ghi HP trước/sau, hit bị chặn và số lần `~onAttack`/`~onSkillDamage` chạy. | [Damage](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/damage?version_id=7acedee9f265756e99f74259d405af133f1cbc52), [Changelog 5.14.0](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd#damage) |
| Projectile | Theo dõi nơi bắn, hướng, bán kính trúng ngang/dọc, khoảng cập nhật, thời lượng, tầm tối đa và điều kiện dừng. `onHit` nhận các entity trúng làm mục tiêu kế thừa. `@origin` trong callback dùng vị trí projectile theo mô tả wiki. | [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [Targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters) |
| Aura và interrupt | Aura có vòng đời và callback. `terminable` kiểm tra điều kiện mỗi tick và có thể hủy chuỗi `onStart`, với `onTerminate` để gọi skill khi bị hủy. Xác định riêng hiệu ứng, summon hoặc projectile nào cần thu dọn. | [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura), [Terminable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/terminable) |

## Những điểm phụ thuộc phiên bản

- **5.12.0** viết lại aura theo component. Khi mang một aura cũ sang build khác, đọc cả trang aura và changelog của build đang dùng. **5.12.1** thêm hậu tố đơn vị như `5s` và `20t` cho cooldown và nhiều duration/interval. Kiểm tra trường cụ thể trước khi áp dụng. [Changelog 5.12.0–5.12.1](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd)
- **5.14.0** ghi nhận `then` cho callback damage và `<skill.var.damage-dealt>` để đọc damage thực tế theo ngữ cảnh được mô tả. Changelog cũng ghi `triggerSkillDamage` khi cần kết hợp với `triggerSkills`. Đo riêng trường hợp nhiều mục tiêu, giáp, khiên và miễn nhiễm. [Changelog 5.14.0 mục Damage](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd#damage)

## Đọc và kiểm thử một đòn

Ghi theo thứ tự trigger → target → telegraph → animation → hitbox và damage → cooldown → interrupt và cleanup. Với projectile, thử trúng entity, trúng tường, hết tầm, nhiều người đứng trên đường bay, và caster chết khi projectile còn tồn tại. Ghi riêng mốc hình ảnh, sự kiện va chạm và lượng HP mất để kiểm tra đồng bộ. Đây là kịch bản thử đề xuất cho dữ liệu thật. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [ModelEngine State](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State)

[Ví dụ tương tác và delay](../../examples/simple/README.md) dùng cặp mob và metaskill. Xem [hiệu năng](../architecture/performance.md) khi tăng tần suất hoặc số mục tiêu.
