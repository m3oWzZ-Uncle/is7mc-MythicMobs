# ModelEngine

Asset, điểm neo, state và gameplay độc lập với phần nhìn. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 26 · Long Hồn Xuất Thế

- **Gameplay.** Rồng hiện trên caster, bay tới điểm gọi rồi tan.
- **Bắt buộc.** Ghi asset, model ID và state xuất hiện/bay/tan. Nếu có damage, chỉ tại mốc lao trúng đã định.
- **Tình huống biên.** Model không nạp, quay caster sau lúc gọi, hủy giữa animation.
- **Kiểm thử.** Đọc log đăng ký, quay chuyển state và điểm hit. Kiểm còn entity/model sau khi kết thúc.

## 27 · Kiếm Trận Lục Hợp

- **Gameplay.** Sáu kiếm hiển thị sáu điểm của trận rồi cùng giáng.
- **Bắt buộc.** Giữ bố cục đúng theo tâm, phân biệt thời điểm hiện và damage, giới hạn số hit lên cùng người.
- **Tình huống biên.** Một điểm bị tường che, hai trận chồng, độ trễ client.
- **Kiểm thử.** Đếm sáu model và ghi tick impact. So vùng trong/ngoài và kiểm model thuộc đúng cast.

## 28 · Dragon Fist

- **Gameplay.** Nắm đấm rồng đi cùng nhát đấm của player.
- **Bắt buộc.** Có pose chuẩn bị, frame impact và recovery. Hitbox theo vùng chạm đã mô tả. Chém hụt vẫn chạy recovery.
- **Tình huống biên.** Đích né phút cuối, caster quay trong warm-up, animation đổi tốc độ.
- **Kiểm thử.** So video giữa frame chạm và damage. Kiểm trường hợp hụt và khi thử hai tốc độ trên cùng build.

## 29 · Shadow Doppelganger

- **Gameplay.** Tạo một phân thân mô phỏng một hành động rồi tan.
- **Bắt buộc.** Model và owner rõ ràng, bản sao chỉ làm hành động được cho phép. Xác định ai là caster damage và dọn phân thân.
- **Tình huống biên.** Hai player tạo clone, người gốc rời arena, clone gặp tường.
- **Kiểm thử.** Quan sát hai clone giống nhau nhưng không nhầm owner, không gây hit lặp, không tồn tại sau timeout.

## 30 · Thiên Kiếm Giáng Thế

- **Gameplay.** Kiếm lớn xuất hiện trên điểm ngắm và giáng xuống vùng đã báo.
- **Bắt buộc.** Model spawn/fall/impact khớp mốc; mốc hit dùng cùng vùng cảnh báo và chính sách trần/tường được công bố.
- **Tình huống biên.** Trần thấp, đích chạy qua mép, một asset nạp lỗi.
- **Kiểm thử.** Quay cảnh báo và impact từ bên. Kiểm hai cao độ và xem log nạp model, rồi đo điểm chạm.
