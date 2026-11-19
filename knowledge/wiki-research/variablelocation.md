# VariableLocation · chọn điểm đã lưu

**Chức năng và cú pháp.** `@VariableLocation{var=caster.<tên>}` trả vị trí lưu trong biến. Đây là location targeter. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/VariableLocation), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Targeters/VariableLocation.md)

**Thuộc tính.** `variable` (`name`, `n`, `var`, `key`, `k`) đặt tên biến. Có thể ghi scope trong tên hoặc bằng `scope` (`s`). Các offset location, gồm `y`, xem bảng thuộc tính chung của targeter. [Targeters](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#common-location-targeters-attributes)

**Ví dụ và trường hợp dùng.** Vạn Kiếm đọc điểm caster đã lưu, cộng y-offset để kiểm tra điểm nâng. Dùng khi nhiều bước cần chia sẻ cùng tâm. Với skill cần lấy vị trí hiện tại thay đổi theo caster, dùng `@SelfLocation`. [Ví dụ YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L16), [SetVariableLocation](setvariablelocation.md)

**Lỗi thường gặp.** Đọc scope khác với lúc ghi hoặc dùng với mechanic chỉ nhận entity. Truy biến qua callback và kiểm tra trường hợp biến hết hạn. Offset bằng placeholder và biểu thức trong ca Vạn Kiếm vẫn cần xác nhận trên build đích.

**Phiên bản và xác minh.** `Documented`, ngày 14/11/2026. Chưa có server test cho tổ hợp offset động.
