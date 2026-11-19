# Teleport · dịch chuyển caster tới đích

**Chức năng và cú pháp.** `teleport{...} @targeter` chuyển caster tới entity hoặc location. Khi cần chuyển entity được chọn đến một destination riêng, tra cơ chế `TeleportTo`. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleport), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/teleport.md), [TeleportTo](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/teleportto)

**Thuộc tính.** `spreadh` và `spreadv` mặc định 0, `preservepitch` và `preserveyaw` mặc định true. `unsafe` mặc định false. Đặt `unsafe=true` bỏ bước tìm điểm đáp an toàn và bỏ qua spread.

**Ví dụ và trường hợp dùng.** Vạn Kiếm gọi teleport đến `@VariableLocation` có y-offset sau khi xét ba điểm dọc trục. Hợp với đích xác định cần giữ hướng camera. Dùng chuyển động vật lý khi người chơi cần cảm nhận quán tính hoặc khi việc dịch chuyển liên tục xung đột cơ chế di chuyển của server. [Ví dụ YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L35), [VariableLocation](variablelocation.md), [Velocity](velocity.md)

**Lỗi thường gặp.** Lẫn caster và target khi chọn mechanic. Ba điểm kiểm tra không bao phủ hitbox cạnh block. Thử sát mép, trần, đổi world, anti-cheat và giữ pitch/yaw trên build mục tiêu.

**Phiên bản và xác minh.** `Documented`, ngày 14/11/2026. Phạm vi các thuộc tính đã nêu, chưa xác định phiên bản tối thiểu và chưa thử teleport trên server trong đợt này.
