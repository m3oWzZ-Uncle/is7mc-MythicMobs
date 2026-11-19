# Hồ sơ tư duy thiết kế MythicMobs

Hồ sơ tóm tắt cách người dùng chọn giải pháp trong những bối cảnh đã có bằng chứng. Mỗi kết luận dẫn về yêu cầu trực tiếp hoặc hồ sơ quyết định để phiên Codex sau kiểm tra lại phạm vi áp dụng. [Chỉ mục phỏng vấn và quyết định](../feedback/decisions/README.md)

Tra các quyết định theo project, chủ đề và điều kiện trong [bộ nhớ dài hạn](../memory/index/README.md).

## Nguyên tắc đã xác nhận

| Loại | Nguyên tắc | Phạm vi | Nguồn |
| --- | --- | --- | --- |
| PREFERENCE | Chọn kiến trúc đơn giản nhất đáp ứng đầy đủ hành vi được yêu cầu. | Khi so sánh các phương án đều giữ được gameplay yêu cầu. | [Quy tắc project](../AGENTS.md) |
| PREFERENCE | Chỉ thêm condition, variable, timer, lớp metaskill hoặc bảo vệ khi có yêu cầu, lỗi thực tế hoặc lý do kỹ thuật đã xác minh. | Thiết kế và sửa MythicMobs. | [Phản hồi Dash Cleave](../feedback/corrections/MM-2026-006.md) |
| PREFERENCE | Ưu tiên Player Skills khi tự chọn chủ đề học, phỏng vấn và bài tập theo định hướng 75%/15%/10%. | Định hướng học. Nhiệm vụ cụ thể đi theo yêu cầu gameplay. | [Quyết định Player Skills](../memory/decisions/player-skill-training-priority.json) |

Trong Dash Cleave, người dùng quan sát `lunge` phù hợp hơn cho cú lướt nhắm người chơi. Đánh giá mechanic lại theo hành vi nếu chuyển sang player dash, đổi cách ngắm hoặc cần thao tác vận tốc trực tiếp. [Quyết định Dash Cleave](../memory/decisions/dash-cleave-lunge.json)

## Phỏng vấn đang mở

| Hồ sơ | Chủ đề | Trạng thái |
| --- | --- | --- |
| [MM-D-2026-001](../feedback/decisions/MM-D-2026-001.md) | Khóa hướng đòn quét của boss và khoảng né khi có hai người chơi | Chờ người dùng trả lời |
| [MM-D-2026-002](../feedback/decisions/MM-D-2026-002.md) | Ưu tiên đòn đã báo hay phase mới khi chạm ngưỡng máu | Chờ xác nhận dự đoán |

Sau mỗi câu trả lời, cập nhật hồ sơ tình huống trước. Thêm vào bảng nguyên tắc khi người dùng nêu rõ tiêu chí có thể dùng lại và phạm vi của nó. Nếu hai quyết định khác nhau, giữ cả hai kèm điều kiện cụ thể và hỏi về điểm phân biệt khi điều đó ảnh hưởng đến thiết kế.
