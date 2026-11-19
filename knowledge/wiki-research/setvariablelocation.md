# SetVariableLocation · lưu điểm neo

**Chức năng và cú pháp.** `setvarloc{var=caster.<tên>;v=@<targeter>} @self` lưu dữ liệu vị trí được cung cấp. Trang mechanic mô tả kết quả dạng chuỗi chứa world và tọa độ. Trang targeter xác nhận cách đọc lại bằng `@VariableLocation`. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariablelocation), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/setvariablelocation.md)

**Thuộc tính.** `value` (`val`, `v`, `a`, `amount`) mặc định `@self` theo wiki. `var`, `scope`, `duration` và `save` là thuộc tính kế thừa. Chọn scope theo vòng đời dữ liệu và đối chiếu giới hạn của từng scope. [SetVariable](../entries/mythicmobs--meta-mechanic--setvariable.md)

**Ví dụ và trường hợp dùng.** Vạn Kiếm lưu `@selflocation` lúc cast rồi đọc lại trong aura để giữ một điểm qua nhiều tick. Nếu điểm cần theo entity đang di chuyển, gọi location targeter tại thời điểm mỗi lần sử dụng. [Ví dụ YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L6)

**Lỗi thường gặp.** Hai lượt cast của cùng caster ghi cùng tên làm đổi điểm neo đang dùng. Đặt tên theo tác vụ, guard cast chồng hoặc dùng scope phù hợp và dọn khi kết thúc. Thử mất world và việc đọc lại từ callback mới. [VariableLocation](variablelocation.md), [Pattern scope](../patterns/variable-scope.md)

**Phiên bản và xác minh.** `Documented`, ngày 14/11/2026. Cách biểu diễn nội bộ và xử lý world khi đọc trên build cụ thể vẫn cần thử.
