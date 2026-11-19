# Projectile và va chạm

Chọn hướng bay, quy tắc dừng và mục tiêu damage theo gameplay. Wiki mô tả `onHit` nhận mục tiêu va chạm và `onTick` có thể đặt VFX tại `@origin`. Giữ mục tiêu kế thừa nếu chỉ entity bị chạm nên nhận damage. Nếu có nổ vùng, ghi rõ bước chọn mục tiêu riêng và phạm vi. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile)

So sánh [Kiếm khí định hướng](../../../tests/training-sandbox/002-directional-sword-wave/README.md) với [Vạn Kiếm có AoE tại điểm trúng](../../patterns/projectile-va-cham.md). Kiểm thử đứng trên/ngoài đường bay, tường, và nhiều caster. Tốc độ cao hoặc nhiều điểm nội suy cần đo cả số lần trúng lẫn tải callback. [Tối ưu timer và callback](../../patterns/toi-uu-timer-va-callback.md)

[Kiếm Khí Trảm r1](kiem-khi-tram.md) là ví dụ PvE đã được người dùng thử và chấp nhận trong Minecraft. Bài ghi bối cảnh, lý do thiết kế và phạm vi của xác nhận.

[Hỏa Cầu Thuật r1](hoa-cau-thuat.md) là ví dụ AoE PvE đã được người dùng thử và chấp nhận. Dùng để tra các chiêu chỉ nổ khi va chạm và cần xét vật chắn từ điểm nổ.

[Hàn Băng Địa Mạch](../../../tests/training-sandbox/026-curriculum-frost-ground-surge/README.md) là bài thử projectile bám địa hình, tách callback tường khỏi hết tầm, lấy mẫu BlockMask và quản lý lồng băng theo thời hạn stun. Đã kiểm tra tĩnh, chờ thử trong Minecraft.
