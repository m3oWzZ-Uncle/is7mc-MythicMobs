# Chương trình 40 bài MythicMobs

Tám cấp, mỗi cấp năm đề. Caster mặc định là **PLAYER**. Thông số và hành vi ở các đề là hợp đồng bài tập, chưa phải sở thích gameplay đã xác nhận hoặc cam kết engine. Báo build và khả năng cần đối chiếu khi bắt đầu từng bài.

| Cấp | Tập đề | Bài | Trọng tâm |
| --- | --- | --- | --- |
| 1 | [Foundation](levels/foundation.md) | 01–05 | Đường bay, di chuyển, đối tượng nhận hiệu ứng và cửa hồi |
| 2 | [RPG](levels/rpg.md) | 06–10 | Mục tiêu chọn trước, tài nguyên, cửa sổ combo và sự kiện phản công |
| 3 | [Tu Tiên](levels/tu-tien.md) | 11–15 | Đọc được nhiều giai đoạn và giữ quyền sở hữu của caster |
| 4 | [Gameplay](levels/gameplay.md) | 16–20 | Luật mục tiêu, commitment và chính sách ngắt |
| 5 | [Math](levels/math.md) | 21–25 | Nguồn tọa độ, hình học và giới hạn bước tính |
| 6 | [ModelEngine](levels/modelengine.md) | 26–30 | Asset, điểm neo, state và gameplay độc lập với phần nhìn |
| 7 | [Modular](levels/modular.md) | 31–35 | Hợp đồng giữa module, tham số mặc định và hành vi khi lỗi |
| 8 | [Expert](levels/expert.md) | 36–40 | Ngân sách callback, điều phối trạng thái và test tải |

## Cách làm từng bài

1. Chọn đúng bài người dùng yêu cầu. Tra AGENTS, skill, KB, wiki và quyết định đã lưu. Đọc nguồn IonTech khi thuật toán hoặc thiết kế module thực sự liên quan. Cân nhắc các ví dụ đã kiểm chứng trong cùng bối cảnh.
2. Tách gameplay và các tiêu chí đạt khỏi cách triển khai. Ghi giả định quan trọng. Tạo một case sandbox cho bài hiện tại, có build, addon, kịch bản, và căn cứ chọn mechanic. Bài chưa được giao chỉ có đề và cách thử.
3. Chạy kiểm tra tĩnh, lưu hash bản thử cùng hướng dẫn Minecraft. Khi có lỗi, tìm nguyên nhân, giữ diff/hồ sơ và kiểm tra lại ca lỗi lẫn ca từng đạt. Chỉ hỏi phần thiếu làm đổi kết quả.
4. Chỉ gắn **GAMEPLAY_VERIFIED** khi đúng bản YAML có bằng chứng theo ca và xác nhận trực tiếp của người dùng. Sau khi xác nhận, ghi bài học, kỹ thuật và ngoại lệ. Tổng kết mỗi năm bài được chấp nhận. Lời giải benchmark lưu ngoài bộ đề và chỉ triển khai khi người dùng yêu cầu.
   
[Tiến độ và thống kê](progress.md) · [Đề đánh giá độc lập](../tests/training-benchmarks/curriculum.md) · [Sandbox](../tests/training-sandbox/README.md) · [Memory](../memory/index/README.md)

## Bài đang làm

[Cấp 2 · Bài 03 · Hàn Băng Địa Mạch](../tests/training-sandbox/026-curriculum-frost-ground-surge/README.md). [Lịch sử các bài trước](progress.md).
