# Foundation

Đường bay, di chuyển, đối tượng nhận hiệu ứng và cửa hồi. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 01 · Kiếm Khí Trảm

- **Gameplay.** Người chơi vung tay và phóng một vệt kiếm thẳng theo hướng nhìn lúc cast.
- **Bắt buộc.** Một projectile có thời gian bay, dừng khi gặp tường đặc hoặc mục tiêu PvE đầu tiên ở làn thử. Gây 4 điểm damage cấu hình tại va chạm, tầm tối đa 16 block, cooldown 3 giây. Đi ngang qua người chơi mà không gây damage.
- **Tình huống biên.** Đích lệch trục, hai mob xếp hàng, người chơi cắt ngang, đổi hướng sau khi phóng và hết tầm.
- **Kiểm thử.** Dựng đích ở 6 và 9 block. Đích gần mất máu một lần, đích xa giữ nguyên. Lặp với tường ở 3 block, đứng lệch 2 block, ngắm lên bục và cast từ hai người.

## 02 · Ảnh Bộ

- **Gameplay.** Lướt nhanh theo phương ngang dựa trên hướng mặt.
- **Bắt buộc.** Lướt tại chỗ đứng hiện tại theo yaw lúc cast, thời gian và hồi chiêu hữu hạn. Caster lấy lại điều khiển sau lướt.
- **Tình huống biên.** Nhìn lên/xuống, tường sát, ngã khỏi mép, hai người cast cùng lúc.
- **Kiểm thử.** Đo trước/sau với hai yaw, đối chứng cùng yaw khác pitch. Tường phải chặn và player vẫn di chuyển bình thường.

## 03 · Hỏa Cầu Thuật

- **Gameplay.** Cầu lửa bay và nổ nhỏ ở điểm va chạm.
- **Bắt buộc.** Bắn theo ngắm, có vệt lửa. Nổ tại điểm chạm đích hoặc tường, chỉ gây sát thương trong vùng nhìn thấy quanh điểm nổ. Hết tầm chỉ tắt.
- **Tình huống biên.** Mục tiêu sát tường, đứng hai phía vách, phát trượt hết tầm.
- **Kiểm thử.** Đặt mob trong/ngoài bán kính 2 block và ở phía sau vách. Đếm đúng một vụ nổ khi chạm và không có nổ khi hết tầm.

## 04 · Hộ Thể

- **Gameplay.** Tạo lớp hấp thụ ngắn cho caster.
- **Bắt buộc.** Khiên nhận damage trước máu thường, tự hết hạn, hồi chiêu theo người chơi, không làm lan buff.
- **Tình huống biên.** Khiên bị tiêu hết sớm, thử lại trong cooldown, hai người đứng cạnh.
- **Kiểm thử.** So tim thường và tim hấp thụ với cùng đòn nhẹ trước và sau khi khiên hết. Người thứ hai cast được trong cooldown của người đầu.

## 05 · Toàn Phong Trảm

- **Gameplay.** Xoay tại chỗ và chém một vòng quanh caster.
- **Bắt buộc.** Cảnh báo trước, chỉ gây một hit mỗi mục tiêu hợp lệ tại mốc xoay. Quy định bán kính và cao độ arena.
- **Tình huống biên.** Mục tiêu bước vào/ra ở cuối cảnh báo, đứng trên tầng, chém hụt.
- **Kiểm thử.** Bố trí đích ở bốn hướng, mép trong/ngoài và tầng khác. VFX vẫn hiện khi hụt, mỗi đích hợp lệ chỉ nhận một hit.
