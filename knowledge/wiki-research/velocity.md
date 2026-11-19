# Velocity · sửa vận tốc của entity

**Chức năng và cú pháp.** `velocity{...} @targeter` sửa vector vận tốc entity đã chọn, gồm cả player. `m=SET` đặt giá trị, `ADD` cộng vào vận tốc hiện tại. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/velocity), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/velocity.md)

**Thuộc tính.** `mode` (`m`) mặc định `SET`; `x/y/z` mặc định 1. `relative` mặc định false. Với `relative=true`, trục z theo trước/sau, x theo trái/phải, y theo trên/dưới.

**Ví dụ và trường hợp dùng.** `velocity{m=SET;x=0;y=0;z=0} @self` dừng đà hiện tại. Có thể dùng trước một bước giữ điểm. Với dash cần đạt vị trí chính xác, cần kiểm tra va chạm và độ lệch; nếu thiết kế cho phép dịch chuyển thì [Teleport](teleport.md) xác định đích rõ hơn. [Ví dụ Vạn Kiếm](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L35)

**Lỗi thường gặp.** Bỏ trục vì nghĩ sẽ giữ vận tốc cũ. `SET` với mặc định 1 có thể cấp thêm vận tốc ở trục bỏ qua. Xóa vận tốc một lần cũng không khóa vị trí trước trọng lực, knockback hoặc input sau đó. Thử trên player survival và mob có cấu hình NoGravity.

**Phiên bản và xác minh.** `Documented`, đối chiếu thuộc tính với snapshot và wiki ngày 14/11/2026. Chưa đo di chuyển trong game.
