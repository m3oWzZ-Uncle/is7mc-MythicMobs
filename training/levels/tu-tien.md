# Tu Tiên

Đọc được nhiều giai đoạn và giữ quyền sở hữu của caster. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 11 · Ngự Kiếm Phi Hành

- **Gameplay.** Người chơi cưỡi kiếm VFX và bay trong một lượt hữu hạn.
- **Bắt buộc.** Có đoạn lên, di chuyển và kết thúc an toàn trên arena. Dọn hình kiếm và trả quyền điều khiển theo hành vi đã chọn.
- **Tình huống biên.** Chạm trần, người thoát giữa lượt, hai kiếm cạnh nhau.
- **Kiểm thử.** Quay mốc lên/xuống, kiểm tra model thuộc đúng người và vẫn đi lại sau kết thúc.

## 12 · Vạn Kiếm Quy Tông

- **Gameplay.** Bay lên rồi lơ lửng, mở vòng ma pháp và phóng loạt kiếm.
- **Bắt buộc.** Lên khoảng 12–20 block trong 1,5–1,75 giây. Vòng xuất hiện khoảng 1 giây rồi idle trong lúc bắn. Kiếm đi thẳng theo các điểm lệch trên, dưới, trái, phải và không dồn hết vào một người. Giới hạn số lượt bắn.
- **Tình huống biên.** Trần thấp, rời vùng lúc nâng, hai caster và mất model giữa lượt.
- **Kiểm thử.** Quay mốc tới điểm neo, hiện/idle và luồng kiếm. Kiểm đường bay, số kiếm và dọn vòng khi kết thúc hoặc gián đoạn.

## 13 · Hỏa Liên Nghiệp

- **Gameplay.** Vùng sen lửa nở theo ba vòng báo trước.
- **Bắt buộc.** Mỗi vòng có thời điểm damage và ranh giới tương ứng hình báo. Một mục tiêu chỉ nhận số hit đã quy định cho từng vòng.
- **Tình huống biên.** Đứng giữa hai vòng, nhảy qua biên, hai vùng chồng nhau.
- **Kiểm thử.** Đặt đích ở ba bán kính khác nhau. Lập bảng vòng, tick và hit quan sát.

## 14 · U Minh Ảnh Bộ

- **Gameplay.** Lướt bóng để thoát vị trí, để lại dư ảnh ngắn.
- **Bắt buộc.** Dư ảnh đứng tại điểm rời, thuộc caster và tự biến mất. Người chơi vẫn giữ quyền điều khiển sau lướt.
- **Tình huống biên.** Bị chặn ngay điểm khởi hành, quay gấp, spam theo cửa hồi.
- **Kiểm thử.** Quay vị trí thật và dư ảnh từ bên. Kiểm tra đúng owner và không còn entity sau hết hạn.

## 15 · Thái Cực Trận

- **Gameplay.** Đặt một trận nhỏ với hai nửa tác dụng khác nhau.
- **Bắt buộc.** Tâm và hướng lấy khi cast. Mỗi nửa có hiệu ứng riêng dễ phân biệt, dùng quan hệ mục tiêu đã định trong fixture.
- **Tình huống biên.** Đứng đúng đường chia, đổi nửa khi tick và hai trận giao nhau.
- **Kiểm thử.** Dùng đích ở hai phía, trên biên và ngoài vòng. Lặp với trận quay 90° và hai caster.
