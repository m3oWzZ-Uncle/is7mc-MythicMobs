# Math

Nguồn tọa độ, hình học và giới hạn bước tính. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 21 · Homing Projectile

- **Gameplay.** Đạn đổi hướng để bám một mục tiêu đang chạy.
- **Bắt buộc.** Giới hạn tốc độ đổi hướng, tầm/thời gian sống và va chạm block. Quy định hành vi khi mất mục tiêu.
- **Tình huống biên.** Đích đổi hướng gấp, mất mục tiêu, sát tường và góc quay lớn.
- **Kiểm thử.** Đo quỹ đạo theo tick ở đích đứng yên và chạy ngang. Đạn không quay vô hạn hoặc xuyên tường theo kịch bản.

## 22 · Spiral Blade

- **Gameplay.** Lưỡi kiếm vẽ xoắn theo trục tiến, vùng trúng đi cùng đỉnh xoắn.
- **Bắt buộc.** Khai báo bán kính, bước tiến và đơn vị góc. Đồng bộ cách lấy mẫu VFX với vùng damage.
- **Tình huống biên.** Yaw 0/90/180, tâm gần tường, bước lấy mẫu thưa.
- **Kiểm thử.** Đo ít nhất bốn góc của một vòng và hai yaw. So vị trí đích trong/ngoài dải damage.

## 23 · Orbiting Swords

- **Gameplay.** Một nhóm kiếm quay quanh caster và đánh khi chạm.
- **Bắt buộc.** Quỹ đạo giữ bán kính và khoảng pha, có số kiếm tối đa, thời hạn và giới hạn hit mỗi đích.
- **Tình huống biên.** Người đi nhanh, hai quỹ đạo giao nhau, một đích chạm hai kiếm.
- **Kiểm thử.** Đếm kiếm, đo bán kính/pha và số hit theo thời gian. Kiểm dọn đúng owner khi hết lượt.

## 24 · Ricochet Arrow

- **Gameplay.** Mũi tên nảy theo hướng phản xạ trên tường.
- **Bắt buộc.** Giới hạn hai lần nảy và thời gian sống. Giữ hướng phản xạ phù hợp pháp tuyến bề mặt và hợp đồng va chạm.
- **Tình huống biên.** Va góc, gần song song, đụng tường nhiều lần trong khoảng ngắn.
- **Kiểm thử.** Bắn tường theo góc xiên, đo hướng tới/rời. Xác nhận số lần nảy tối đa và thử đối chứng góc.

## 25 · Parametric Wave

- **Gameplay.** Vệt năng lượng tiến với dao động ngang lặp đều.
- **Bắt buộc.** Khai báo biên độ, chu kỳ và quãng tiến. Từ hệ trục local, xác định VFX và vùng tác động theo chung đường cong.
- **Tình huống biên.** Yaw khác nhau, đầu/cuối sóng, thời gian cập nhật chậm.
- **Kiểm thử.** Đo đỉnh, đáy và điểm qua tâm. So mục tiêu ở đường cong và một điểm chỉ nằm trên đường thẳng nối hai đầu.
