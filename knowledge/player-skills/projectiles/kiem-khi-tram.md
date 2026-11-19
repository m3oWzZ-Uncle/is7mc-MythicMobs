# Kiếm Khí Trảm · ví dụ được người dùng kiểm chứng

**Bối cảnh.** Bài 01 của chương trình 40 bài. Active Player Skill PvE trong arena thử. Người chơi vung tay và phóng một vệt kiếm thẳng theo hướng nhìn. Thông số bản r1 gồm tầm 16 block, damage 4 và cooldown 3 giây. [Đề và cách thử](../../../tests/training-sandbox/018-curriculum-sword-wave/README.md)

**Cách thực hiện.** `playanimation` chạy trên caster khi cast. Projectile nhận điểm ngắm từ `@Forward`, gọi VFX bằng `onTick` tại `@origin`, và gọi damage bằng `onHit` trên target kế thừa. Cấu hình `hp=false`, `hnp=true`, `sB=true`, `sE=true` phục vụ làn thử PvE, dừng ở tường đặc hoặc entity đủ điều kiện. [YAML r1](../../../tests/training-sandbox/018-curriculum-sword-wave/Skills/player-skill.yml) · [Wiki Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile)

**Lý do thiết kế.** Projectile biểu diễn được thời gian bay và va chạm. Cú vung tay vẫn thấy khi hụt. Vệt và damage dùng hai callback của cùng projectile nên không cần quét vùng thứ hai để quyết định ai trúng. Một chiêu xuyên, nổ vùng, hỗ trợ PvP hoặc tương tác pet cần xác định lại chính sách va chạm.

**Bằng chứng.** Người dùng báo đã chạy đúng trong Minecraft và chấp nhận nguyên bản r1. Mốc đối chiếu wiki là 5.14.0. Build chạy thật, log nạp và kết quả từng kịch bản chưa được cung cấp. Đây là một quyết định theo bài, được dùng như ví dụ cho ngữ cảnh tương tự. [Xác nhận kèm hash](../../../tests/training-sandbox/018-curriculum-sword-wave/evidence/user-confirmation-r1.md)
