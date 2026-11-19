# EndProjectile · kết thúc một projectile đang chạy

**Chức năng và cú pháp.** `endprojectile` gọi từ ngữ cảnh projectile để kết thúc projectile đó. Wiki ghi thao tác này kích hoạt `onEnd`. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/endprojectile), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/endprojectile.md)

**Thuộc tính.** `conditions` (`condition`, `cond`, `con`) đặt điều kiện bổ sung trước khi kết thúc. Có thể dùng điều kiện inline ở dòng mechanic như ví dụ wiki.

**Ví dụ và trường hợp dùng.** Ví dụ wiki gọi `endprojectile ?hasaura{auraName=explode}` trong callback tick rồi xử lý nổ qua `onEnd`. Hợp cho kích nổ theo tín hiệu hoặc hủy theo trạng thái. Nếu chỉ kết thúc khi đủ tầm hoặc va chạm, dùng thuộc tính lifecycle của projectile. [Projectile](../entries/mythicmobs--meta-mechanic--projectile.md), [HasAura](../entries/mythicmobs--condition--hasaura.md)

**Lỗi thường gặp.** Gọi từ skill không có projectile hoặc dùng `onEnd` gây sát thương trong nhánh chỉ muốn hủy. Đặt guard cho damage cuối và thử hủy, hết tầm, va chạm riêng. Đếm số lần callback khi đồng thời có `onHit` và `onEnd`.

**Phiên bản và xác minh.** Changelog ghi tính năng mới ở 5.1.1. `Documented`, ngày 14/11/2026, chưa thử callback trong game. [Changelog 5.1.x](https://wiki.mythiccraft.io/mythicmobs/changelogs/5.1.x_changelogs#511)
