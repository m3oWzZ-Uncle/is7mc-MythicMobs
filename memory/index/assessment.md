# Kiểm thử đọc lại bộ nhớ trong phiên Codex mới

Ngày 2026-11-13. Phiên `01a1d55f-b2ab-76b1-9264-59b83c023449` mở trong project MythicMobs-AI-Training với yêu cầu kiểm thử chỉ đọc. Đề bài nêu ba tình huống mà không cung cấp kết quả mong đợi. Phiên dùng `mythicmobs-expert`, đọc chỉ mục, chạy `search` và `resolve`, rồi kiểm tra các hồ sơ nguồn.

| Tình huống | Kết quả quan sát | Bằng chứng trên đĩa |
| --- | --- | --- |
| Hai cách tổ chức metaskill ở TuTien cho cùng gameplay | `resolve` trả `apply` với `simplest-complete-design`. Phiên chọn cách ít bước hơn. | [Ưu tiên đã xác nhận](../preferences/simple-full-gameplay.json) |
| Thời điểm khóa hướng đòn quét boss hai người | `resolve` trả `review-then-ask-if-needed`. Phiên tìm thấy hồ sơ đang chờ và giữ lựa chọn mở. | [Hồ sơ phỏng vấn](../../feedback/decisions/MM-D-2026-001.md) |
| `UnicodeEncodeError` liên quan `cp1252` khi kiểm tra YAML | Phiên tìm hồ sơ cũ và lệnh `python -X utf8 tests/check_yaml.py examples`. | [Lỗi và hồi quy cũ](../../feedback/corrections/MM-2026-001.md) |

Lần gọi `resolve` đầu tiên cho đòn quét dùng giá trị `--impact gameplay` và bị CLI từ chối. Phiên sửa thành `--impact material` rồi chạy thành công. Hướng dẫn đã có ví dụ cho cả `minor` và `material`. [Cách tra cứu](../README.md)

Các tình huống trên kiểm tra việc truy xuất bộ nhớ từ đĩa. Số câu hỏi thực sự được dùng lại theo công việc nằm trong [báo cáo hiện trạng](records.json). [Bộ hồi quy](../../tests/test_memory.py) kiểm tra thêm giới hạn project, xung đột, nguồn bằng chứng và giữ dữ liệu lịch sử.
