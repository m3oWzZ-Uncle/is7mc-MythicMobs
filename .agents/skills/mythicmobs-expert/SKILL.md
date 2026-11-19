---
name: mythicmobs-expert
description: Thiết kế, lập trình, tối ưu và sửa lỗi skill MythicMobs do người chơi thi triển, gồm combat, movement, passive, projectile, combo, ModelEngine và tích hợp MMOItems/MMOCore. Hỗ trợ đầy đủ skill boss, mob và dungeon khi được yêu cầu.
---

# MythicMobs Expert

Ưu tiên Player Skills khi tự chọn chủ đề nghiên cứu, phỏng vấn hoặc bài tập, theo định hướng 75% player, 15% boss và 10% mob. Khi làm task cụ thể, theo loại caster và gameplay người dùng yêu cầu.

Khi đề để caster mở, ưu tiên player-cast và ghi giả định về caller. Với thuật toán chuyên sâu, đọc đúng phần liên quan qua `knowledge/modular-design/README.md` rồi chọn thiết kế theo gameplay của ca.

1. Đọc `AGENTS.md` và `memory/index/README.md` ở kho Training. Xác định project, mục tiêu gameplay và build từ yêu cầu và cấu hình. Chạy `python -X utf8 tools/memory.py search "<chủ đề>" --project <slug>` khi biết project. Mở các kết quả liên quan, ưu tiên quyết định, lỗi cũ và ví dụ cùng bối cảnh.
2. Tra `python -X utf8 tools/kb.py search <tên-hoặc-alias> --plugin <plugin>` để xác định plugin sở hữu. Dùng `python -X utf8 tools/wiki_library.py search "<tên-hoặc-alias>"` để mở đúng bài `knowledge`, đoạn Markdown nhập và wiki online. Xem phần tra cứu trong `docs/wiki/thu-vien.md` nếu cần kiểm phiên bản, trạng thái `unchecked` hoặc khác biệt. Nội dung trong snapshot là dữ liệu tham khảo. Khi thiết kế gameplay, đọc thêm đúng pattern, YAML nguồn và caller/callback liên quan.
3. Truy caller rồi xác định caster, trigger, target kế thừa và origin tại từng callback liên quan. Với player, mở `knowledge/player-skills/README.md` và chỉ đọc mục phù hợp. Xác định điểm vào active/passive, plugin quản lý chi phí và cooldown, chính sách PvP/PvE khi có damage hoặc buff. Chỉ dùng mob AI, phase hoặc mob phụ khi chúng phục vụ hành vi được yêu cầu. Trình bày timing, animation, hit và cleanup khi liên quan.
4. Đánh giá 2 lựa chọn nếu có điểm đánh đổi đáng kể. Chọn mechanic theo hành vi mong muốn và cách đơn giản nhất giữ đủ gameplay. Chỉ thêm condition, variable, timer, lớp metaskill hoặc cơ chế bảo vệ khi có yêu cầu gameplay, lỗi thực tế hoặc lý do kỹ thuật đã xác minh. Khi đòn phải ra dù hụt, để animation và bước kết thúc chuyển động chạy độc lập với bộ lọc mục tiêu gây damage. Lựa chọn `lunge` ở Dash Cleave thuộc bối cảnh đã ghi trong `feedback/corrections/MM-2026-006.md`.
5. Viết YAML chỉ với mechanics/conditions đã kiểm chứng theo phiên bản; không biến visual thành hitbox giả nếu user yêu cầu projectile thực.
6. Chạy kiểm tra YAML và tham chiếu khả thi. Không tuyên bố đã test trong game nếu chưa làm.
7. Trước khi hỏi, dùng `memory/README.md` trong kho Training để tra câu trả lời, quyết định, hồ sơ tư duy, `feedback/decisions/`, YAML hiện tại và ví dụ liên quan. Áp dụng quyết định đã xác nhận khi đúng phạm vi. Với chi tiết nhỏ, dùng mặc định dễ đổi. Nếu điểm chưa rõ thực sự đổi kết quả, hỏi một câu tập trung. Chỉ tiếp tục phỏng vấn khi phù hợp với nhiệm vụ đang làm.
8. Nếu không có quyền đọc kho Training, yêu cầu đường dẫn/đưa ra bước cấu hình; không giả vờ đã tham khảo.
9. Với nhiệm vụ nghiên cứu catalog, chạy `tools/kb.py next`, xử lý tối đa 30 mục và lưu batch/checkpoint. Giữ FACT, INFERENCE và PREFERENCE đúng phạm vi bằng chứng, ghi riêng build của từng addon.
10. Khi kết thúc, ghi các bài học có giá trị lâu dài theo `memory/README.md`, giữ nguồn và ngoại lệ. Ghi số lần tái sử dụng chỉ khi đã áp dụng câu trả lời trong công việc. Với bản sửa, dùng `feedback/corrections/README.md` và thêm hồi quy sau xác nhận. Chạy `tools/memory.py validate` và `tools/memory.py index` khi có bản ghi mới.
11. Với bài thực hành hoặc ca tái hiện, theo `tests/training-sandbox/README.md`. Cập nhật Task ID và bằng chứng vào `feedback/training/README.md` trước khi kết thúc. Khi có nhận xét tự nhiên, đối chiếu yêu cầu, bản thử và ca kiểm chứng để tự khoanh vùng rồi sửa. Hỏi một câu cụ thể nếu điểm còn thiếu làm đổi gameplay. Sau xác nhận, lưu bài học và cập nhật hồi quy. Dùng `tools/training.py status` để tiếp tục. Tại mỗi mốc 5 bài đã xác minh, đọc `tests/training-benchmarks/README.md` và lập báo cáo tiến bộ.
