# Hỏa Cầu Thuật · ví dụ được người dùng kiểm chứng

**Bối cảnh.** Bài 03, skill PvE do player thi triển trong arena thử. Bản r1 nhắm theo hướng nhìn, tầm tối đa 12 block, cooldown 3 giây, sát thương cấu hình 6 và bán kính nổ 2 block. [Đề và ca thử](../../../tests/training-sandbox/020-curriculum-fireball/README.md)

**Cách làm.** Projectile bay theo `@Forward`, còn `onTick` vẽ vệt lửa tại `@origin`. Hai sự kiện va chạm `onHit` và `onHitBlock` trỏ đến cùng một metaskill dùng particle tại origin và chọn mục tiêu bằng `@EntitiesNearOrigin`. Điều kiện `lineofsightfromorigin` xét đường nhìn từ tâm nổ. Cấu hình lọc người chơi và armor stand khỏi sát thương vùng. [YAML r1](../../../tests/training-sandbox/020-curriculum-fireball/Skills/player-skill.yml) · [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) · [Line of Sight From Origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/lineofsightfromorigin)

**Lý do.** Dùng chung một metaskill impact để hai kiểu va chạm có cùng bán kính, hiệu ứng và luật damage. Gắn nổ vào callback va chạm giữ được yêu cầu bay hết tầm chỉ tắt vệt. Dùng particle để minh họa vụ nổ và giữ việc gây damage ở một dòng riêng. Với phát bắn xuyên, chiêu nổ khi hết tầm, PvP hoặc luật đồng minh, chọn lại điểm kích hoạt và bộ lọc.

**Bằng chứng.** Người dùng báo đã chạy đúng trong Minecraft và chấp nhận r1. Build thực tế và các quan sát riêng từng ca chưa được cung cấp. Đây là ví dụ của một hợp đồng gameplay cụ thể. [Xác nhận theo bản YAML](../../../tests/training-sandbox/020-curriculum-fireball/evidence/user-confirmation-r1.md)
