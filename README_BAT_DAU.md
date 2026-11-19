# BẮT ĐẦU TỪ ĐÂU?

Đây là bộ học tập MythicMobs có Knowledge Base đối chiếu với wiki chính thức và ví dụ thực hành. Dữ liệu MythicMobs của bạn sẽ được bổ sung theo từng case, kèm phiên bản và bằng chứng từ server.

- [Kiểm kê tài liệu và ví dụ còn thiếu](docs/kiem-ke.md)
- [Mục lục Knowledge Base](knowledge/README.md)
- [Thiết kế và kiểm thử skill người chơi](knowledge/player-skills/README.md)
- [Thư viện wiki MythicMobs đã nhập](docs/wiki/thu-vien.md)
- [Bộ nhớ dài hạn và cách tra cứu](memory/README.md)
- [Quy trình nạp dữ liệu thực tế](incoming/README.md)

## 1. Giải nén
Đặt thư mục `MythicMobs-AI-Training` trong cùng thư mục cha với project TuTien/Survival nếu tiện.

## 2. Mở Codex
Mở terminal tại thư mục này và chạy `codex` (nếu đã cài Codex CLI). Bạn cũng có thể mở thư mục này bằng Codex trong IDE.

## 3. Giao nhiệm vụ đầu tiên
Dán nội dung ở `prompts/01-khoi-dong.md` cho Codex.

## 4. Nạp dữ liệu
Chọn một mob đã có hành vi quen thuộc. Sao chép YAML mob, các skill được gọi và bằng chứng vào một thư mục case trong `incoming/`. Điền [mẫu hồ sơ](incoming/TEMPLATE.md) và dùng [prompt phân tích YAML](prompts/02-hoc-tu-yaml.md).
Với case lỗi, sao chép cả bản lỗi và bản sửa khi có thể.
KHÔNG đặt mật khẩu, API key, dữ liệu người chơi hoặc config bí mật vào bộ dữ liệu.

## 5. Dùng cho các project khác
Cài skill trong `.agents/skills/mythicmobs-expert` vào `~/.agents/skills/mythicmobs-expert` (Linux), hoặc project khác tham chiếu bằng AGENTS.md tới đường dẫn tuyệt đối có thể đọc.
Để bộ kiến thức được truy cập, giữ đường dẫn ổn định và chỉ dẫn Codex đúng vị trí.

## 6. Cập nhật lâu dài
Mỗi lần sửa sai, dùng [prompt ghi nhận lỗi](prompts/03-ghi-nhan-loi.md). Chỉ gắn `verified-in-game` khi có bằng chứng kiểm thử trong game. Xem [cách xác định trạng thái](tests/README.md).

## Các giới hạn
- Không có cấu hình MythicMobs nào trong bộ khởi động này được tự nhận là đã test.
- Không tự động 'train' trọng số mô hình.
- Kiểm tra YAML chỉ phát hiện được một số lỗi; hành vi trong Minecraft vẫn phải test thực tế.
