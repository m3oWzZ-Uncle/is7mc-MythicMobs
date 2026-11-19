# Kiểm kê bộ học tập ngày 13/11/2026

Trước khi bổ sung Knowledge Base, `knowledge/` chỉ có hai README khung. `docs/wiki/` có trang chỉ dẫn đến wiki, còn `prompts/` có bốn prompt cho khởi động, phân tích YAML, ghi nhận lỗi và áp dụng sang project khác. `feedback/` có hai template và chưa có case. `tests/` có trình đọc cú pháp YAML. `incoming/` và bốn nhóm `examples/` chỉ có README. Qua kiểm kê workspace, chưa có YAML thật, log nạp plugin, kết quả thử trong game hoặc hồ sơ phiên bản server.

| Ưu tiên | Phần còn thiếu | Dữ liệu cần bổ sung |
| --- | --- | --- |
| 1 | Một mob và skill đã biết hành vi | File mob, file skill được gọi, build/edition, thao tác thử, kết quả và log nạp |
| 2 | Chuỗi combat, đổi target, projectile hoặc aura | Các callback và phụ thuộc, mốc cảnh báo/va chạm, số lần trúng, điều kiện hủy và cleanup |
| 3 | Boss nhiều phase | Mốc phase, luật khi vượt nhiều ngưỡng, hồi máu và reset, YAML add/spawner/arena nếu được tham chiếu, log/video khi có nhiều người chơi |
| 4 | ModelEngine | Phiên bản plugin, model ID, tên state, thời lượng/loop, mốc chạm đòn, cấu hình liên kết và kết quả test với resource pack. [Wiki ModelEngine State](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State) |
| 5 | Case lỗi và hồ sơ hiệu năng | Bản lỗi và bản sửa, bước tái hiện, kết quả hồi quy. Với hiệu năng, thêm số người chơi/mob, số lượt cast và số liệu trước/sau cùng kịch bản. [PaperMC Profiling](https://docs.papermc.io/paper/profiling/) |

Sau lần bổ sung này, [mục lục Knowledge Base](../knowledge/README.md) có đủ bảy nhóm. [Ví dụ tương tác](../examples/simple/README.md) là cấu hình thực hành viết theo wiki. Các ví dụ combat, boss và ModelEngine sẽ có giá trị nhất khi đi kèm cấu hình và bằng chứng từ server thật. Bắt đầu bằng [một hồ sơ trong `incoming/`](../incoming/README.md).
