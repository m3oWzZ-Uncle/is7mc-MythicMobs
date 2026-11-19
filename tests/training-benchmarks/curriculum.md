# Đề đánh giá độc lập cho chương trình 40 bài

Mỗi mốc chọn một đề chưa làm. Đề mô tả kết quả quan sát, giữ lời giải riêng ở case đánh giá sau khi được yêu cầu làm. Dùng [tiêu chí chung](README.md#tiêu-chí-chung) và ghi mức bằng chứng vào [tiến độ](../../training/progress.md).

| Đề | Yêu cầu gameplay | Đối chứng và tiêu chí |
| --- | --- | --- |
| CT-BM-01 · Ấn kiểm tra đường ngắm | Một điểm sáng xuất hiện trên bề mặt player đang ngắm. Ngoài tầm hoặc nhìn trời thì phát tín hiệu hụt, không đặt điểm. | Thử tường ở ba cự ly, hai yaw và an toàn khi không có block. Bystander không nhận tín hiệu riêng của caster. |
| CT-BM-02 · Nhịp giải cứu | Người chơi hỗ trợ một đồng đội theo hai nhịp. Đồng đội phải còn trong vùng khi nhịp 2 chạy. | Đích rời, người khác thế chỗ và hai ca đồng thời. Kiểm đúng người và nguồn hồi, đúng hai nhịp ở ca đạt. |
| CT-BM-03 · Hành lang dấu chân | Player để lại ba dấu theo quãng đường đã đi trong một cửa sổ hữu hạn. Đứng yên không tạo dấu mới. | So đi thẳng, đứng yên, quay đầu và hai caster. Kiểm số dấu, thứ tự và điểm dọn. |
| CT-BM-04 · Đánh lạc hướng | Sau cảnh báo, đích ban đầu có thể né. Đòn cuối đi theo hướng đã báo và chỉ trúng mục tiêu mới nếu vào vùng. | Đổi mục tiêu trong hai nhịp khác nhau. So hướng tại mốc báo và mốc impact, chém hụt vẫn có hồi đòn. |
| CT-BM-05 · Ba cổng góc | Player kích hoạt đúng một trong ba cổng dựa vào góc đến theo trục của arena. Quy tắc hòa phải công bố. | Thử trục chuẩn, ranh giới, góc âm và arena quay 90°. Ghi input và cổng được chọn. |
| CT-BM-06 · Hình chiếu mặt nạ | Model bám đúng player qua hai state rồi tách ở một mốc quan sát được. Khi thiếu asset, ghi lỗi và chứng minh đường kết thúc có thể kiểm tra. | So thời gian state, vị trí trước/sau tách và hai đồng thời. Kiểm asset lỗi và không sót model. |
| CT-BM-07 · Chọn phép theo tài nguyên | Một entry chọn giữa hai phép có chi phí khác nhau. Chỉ phép hợp lệ đầu tiên chạy và trừ chi phí đúng một lần. | Thử đủ cả hai, chỉ đủ một và không đủ. Ghi entry được chọn và tài nguyên trước/sau. |
| CT-BM-08 · Hủy chuỗi giữa trận | Hai player có chuỗi callback độc lập. Tín hiệu hủy của A giải phóng toàn bộ phần việc của A; B tiếp tục theo ngân sách đã khai báo. | Gửi hủy ở hai mốc, lặp tín hiệu, đo callback tồn dư, số lần dọn và ảnh hưởng tới B. |
