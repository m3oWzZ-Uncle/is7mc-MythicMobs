# Foundation · Đánh giá cuối Cấp 1

Ngày mở 2026-11-15. Người dùng yêu cầu bắt đầu bài kiểm tra trước Cấp 2. Bản đánh giá đang mở. Kết quả mốc chính thức phụ thuộc vào hồ sơ gameplay của các bài 01–05 và ca đánh giá.

| Bài | Bằng chứng đến thời điểm mở |
| --- | --- |
| [01 · Kiếm Khí Trảm](../../tests/training-sandbox/018-curriculum-sword-wave/evidence/user-confirmation-r1.md) | Người dùng xác nhận r1 chạy đúng trong Minecraft. Còn thiếu phiên bản, log nạp và hồ sơ kết quả từng ca. |
| [02 · Ảnh Bộ](../../tests/training-sandbox/019-curriculum-shadow-step/README.md) | Phản hồi phân biệt lướt ngang và lướt sát nền. Chờ kết quả ca A/B. |
| [03 · Hỏa Cầu Thuật](../../tests/training-sandbox/020-curriculum-fireball/evidence/user-confirmation-r1.md) | Người dùng xác nhận r1 chạy đúng trong Minecraft. Còn thiếu phiên bản, log nạp và hồ sơ kết quả từng ca. |
| [04 · Hộ Thể](../../tests/training-sandbox/021-curriculum-body-guard/README.md) | Có quyết định về giảm sát thương theo hệ thống damage. Chờ thử nghiệm cấu hình và biến thể. |
| [05 · Toàn Phong Trảm](../../tests/training-sandbox/022-curriculum-whirlwind/README.md) | Người dùng đánh giá r1 phù hợp với skill không model. Chờ kết quả thử r1 và biến thể có model. |

Tại thời điểm mở, công cụ báo 0 bài có đủ hồ sơ `GAMEPLAY_VERIFIED`. Có hai xác nhận trực tiếp và ba nhóm phản hồi thiết kế. Nhật ký ghi 0 lần sửa YAML do phản hồi trong nhóm này. Dữ liệu hiện tại chưa đủ để kết luận có lỗi lặp hoặc ghi nhận câu hỏi đã tránh.

**Bài vận dụng · CT-BM-04.** Tái sử dụng mốc cảnh báo và chém tách khỏi truy vấn damage. Điểm mới cần đo là vùng cố định theo yaw lúc cast, kể cả khi caster đổi hướng và đích thay đổi sau cảnh báo. Chọn tọa độ kế thừa để tránh thêm biến hoặc Totem cho một nhịp chém. Lưu ca dương, đổi hướng, đổi đích sớm/muộn, hụt và nhiều người ngay trong [sandbox đánh giá](../../tests/training-sandbox/023-foundation-assessment-decoy/README.md). Cập nhật kết luận và bộ nhớ sau kết quả thực tế.
