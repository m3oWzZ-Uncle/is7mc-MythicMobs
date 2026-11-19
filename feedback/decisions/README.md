# Phỏng vấn và quyết định thiết kế

| Hồ sơ | Chủ đề | Trạng thái |
| --- | --- | --- |
| [MM-D-2026-001](MM-D-2026-001.md) | Khóa hướng đòn quét boss trong trận hai người | Chờ người dùng trả lời |
| [MM-D-2026-002](MM-D-2026-002.md) | Đổi phase khi Wu đang báo đòn | Chờ xác nhận dự đoán |
| [MM-D-2026-003](MM-D-2026-003.md) | Ảnh Bộ đi sát nền so với lướt ngang | Tiêu chí gameplay đã xác nhận. Chờ A/B biến thể offset. |
| [MM-D-2026-004](MM-D-2026-004.md) | Hộ Thể giảm sát thương theo thời gian và hệ stat | Ưu tiên thiết kế đã xác nhận. Chờ thử biến thể giảm damage. |
| [MM-D-2026-005](MM-D-2026-005.md) | Model báo hiệu, model chém 180° và vùng damage | Kinh nghiệm đã được người dùng mô tả. Chờ asset và kiểm thử biến thể. |
| [Player Skills là trọng tâm](../../memory/decisions/player-skill-training-priority.json) | Ưu tiên nghiên cứu, phỏng vấn và thực hành | Người dùng xác nhận |

## Tiếp tục qua phiên Codex

1. Mở hồ sơ đang chờ và đọc [hồ sơ tư duy](../../knowledge/learning-profile.md). Nếu người dùng đã trả lời, ghi ngày, lời xác nhận hoặc diễn giải sát nghĩa, lựa chọn, lý do và bối cảnh. Nếu họ chọn mà chưa nêu lý do, lưu lựa chọn trong phạm vi tình huống.
2. Khi người dùng nói “tùy trường hợp” hoặc một điểm còn mơ hồ, hỏi một câu về điều kiện có thể làm họ đổi lựa chọn. Khi đã đủ rõ, chọn tình huống thực tế kế tiếp, nêu 2–4 phương án, so sánh ngắn và hỏi một câu. Lưu câu hỏi vào hồ sơ trước khi gửi để có thể tiếp tục ở phiên khác. [Mẫu quyết định](TEMPLATE.md)
3. Cập nhật trạng thái ở đây và trong hồ sơ tư duy. Đưa tiêu chí vào hồ sơ tư duy khi có lời xác nhận hoặc quy tắc rõ ràng do người dùng viết. Ghi điều kiện, ngoại lệ và bằng chứng cùng tiêu chí. Với nhiệm vụ thực tế, ghi điều vừa học vào hồ sơ có liên quan rồi cập nhật chỉ mục.
4. Thêm quyết định và câu hỏi đã trả lời vào [bộ nhớ dài hạn](../../memory/README.md) để tra lại được theo project và chủ đề.

## Dùng YAML làm bằng chứng

Tìm ví dụ qua [chỉ mục dữ liệu](../../knowledge/dataset-index.md) hoặc [thư viện pattern](../../knowledge/patterns/README.md). Truy từ trigger đến targeter, conditions, metaskill và kết quả dự kiến. Với combat, xét timing, animation, hitbox, damage, cooldown, interrupt, cleanup và multiplayer. Ghi đường dẫn hoặc dòng nguồn, build nếu biết, phạm vi đã kiểm tra, ưu nhược điểm và phương án khác. Nếu cách hiểu ý đồ ảnh hưởng đến thiết kế, dùng một câu hỏi để xác nhận với người dùng.

| Loại | Cách ghi |
| --- | --- |
| FACT | Chi tiết xác nhận được từ tài liệu, dòng YAML hoặc kết quả kiểm thử, kèm nguồn và giới hạn của bằng chứng. Nội dung hiện diện trong YAML chứng minh cấu hình đã được viết. Hành vi trong game cần bằng chứng gameplay. |
| INFERENCE | Cách diễn giải luồng hoặc ý đồ có căn cứ. Ghi điều còn cần xác nhận. |
| PREFERENCE | Lựa chọn hoặc tiêu chí người dùng xác nhận, kèm tình huống và phạm vi. Một lựa chọn trong case chỉ áp dụng cho case đó đến khi có thêm căn cứ. |

Khi đã có quyết định phù hợp để đối chiếu, dùng một tình huống mới để kiểm tra dự đoán. Ghi dự đoán và các mã quyết định làm căn cứ trước khi hỏi. Sau phản hồi, lưu kết quả đúng, sai hoặc đúng có điều kiện và cập nhật phạm vi nguyên tắc dựa trên lời người dùng. [Mẫu quyết định](TEMPLATE.md)

Các nguyên tắc gameplay có thể dùng lại thuộc [kiến trúc](../../knowledge/architecture/README.md). Lỗi và bản sửa đi qua [quy trình ghi nhận lỗi](../corrections/README.md).
