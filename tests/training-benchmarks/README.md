# Đề đánh giá độc lập · Player Skills

[Đề đánh giá riêng của chương trình 40 bài](curriculum.md) dùng với `tools/training.py review <mốc> --curriculum`.

Dùng tại các mốc 5, 10, 15… bài thực hành có bằng chứng gameplay. Chạy `python -X utf8 tools/training.py review 5` cho mốc đầu. Đọc các báo cáo trước để chọn năm bài chưa được tổng kết. Chọn một đề chưa dùng và ghi ID vào báo cáo. Thử lời giải trong một ca `assessment` tại sandbox với `after_completed` bằng mốc. Đề này giữ yêu cầu và dữ liệu thử; lời giải của mốc được lưu với ca đánh giá để người làm bài sau dùng đề khác.

## BM-01 · Đổi chỗ theo cặp

A và B là đồng đội trong một fixture có danh sách cặp do đề cung cấp. Cast từ A sẽ đổi chỗ hai người ngay khi cả hai đứng trong vùng hoạt động. Nếu B rời vùng trước lúc xử lý, cả hai giữ nguyên tọa độ. Thử thêm cặp C/D làm đồng thời và kiểm tra không đổi nhầm cặp. Điểm đánh giá là phân biệt caller với đối tác, xử lý thất bại mà không nửa chừng và chọn đúng nơi lưu dữ liệu cặp. Cần nêu cách xác nhận cặp từ fixture hoặc plugin trước khi thiết kế.

## BM-02 · Lấy đà từ hai mẫu

Skill player chỉ tăng lực đẩy tới trước khi người đó đang tiến theo hướng mặt trong cửa sổ lấy mẫu. Người đứng yên, bị đẩy ngược hoặc xoay tại chỗ nhận lực cơ bản. Hai người cast cùng lúc được xét riêng. Đo cùng một quãng đường mẫu ở hai hướng, nêu cách xác định khoảng thời gian lấy mẫu và kiểm tra mốc giảm tốc. Có thể dùng API phù hợp khi đáp ứng chính xác dữ liệu cần đo.

## BM-03 · Chặn trúng đòn kế tiếp

Người chơi bật phòng thủ trong thời gian ngắn. Đòn cận chiến đầu tiên hợp lệ tiêu thụ phòng thủ và phát phản hồi đúng một lần. Một đòn thứ hai trong cùng cửa sổ đi qua bình thường. Projectile và sát thương môi trường được dùng làm đối chứng. Thử hai player và một người đánh chuyển mục tiêu. Nêu event, thứ tự tiêu thụ và cách đo kết quả thực tế.

## Tiêu chí chung

- Bằng chứng gameplay bao gồm case dương, đối chứng âm và ca nhiều player khi liên quan.
- Đánh giá mechanic, thuật toán, caster/target và độ phức tạp theo yêu cầu. Dẫn bằng chứng về lỗi đã sửa hoặc lặp lại. Chỉ kết luận cho phần quan sát được.
- Ghi câu hỏi thực sự đã tránh nhờ bản ghi có sẵn. Các lần tra cứu thông thường được ghi như nguồn thiết kế, không tính là câu hỏi đã tránh.

[Nhật ký và cách ghi báo cáo mốc](../../feedback/training/README.md) · [Các cấp kiểm chứng](../README.md#trạng-thái-và-bằng-chứng)
