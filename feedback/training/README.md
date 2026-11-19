# Nhật ký huấn luyện thực hành

| Ngày | Task ID | Kết quả và bước tiếp |
| --- | --- | --- |
| 2026-11-15 | [015 · Khiên hấp thụ cá nhân](../../tests/training-sandbox/015-personal-guard/README.md) | Đã chọn potion theo wiki và triển khai ca player-only. Bản hiện tại đạt kiểm tra tĩnh. Chờ log nạp, thử hấp thụ/timeout/cooldown và xác nhận trên đúng bản YAML. |
| 2026-11-15 | [016 · Thanh tẩy có chọn lọc](../../tests/training-sandbox/016-selective-cleanse/README.md), [017 · Hồi máu có báo trước](../../tests/training-sandbox/017-delayed-self-heal/README.md) | Hai ca thực hành tiếp theo đã có YAML và kịch bản. Chờ thử Minecraft. |
| 2026-11-15 | [Chương trình 40 bài · Bài 01](../../training/progress.md) | Bản r1 đã chuẩn bị. Chờ kết quả sáu ca và xác nhận. Mốc chương trình theo dõi riêng. |
| 2026-11-15 | [Chương trình 40 bài · Bài 01 r1](../../tests/training-sandbox/018-curriculum-sword-wave/evidence/user-confirmation-r1.md) | Người dùng báo chạy đúng trong Minecraft, chấp nhận cách triển khai. Build và báo cáo từng ca chưa có. |
| 2026-11-15 | [Chương trình 40 bài · Bài 02](../../tests/training-sandbox/019-curriculum-shadow-step/README.md) | Bản r1 đã kiểm tra tĩnh. Chờ thử lướt ngang, tường, mép bậc và cooldown. |
| 2026-11-15 | [Chương trình 40 bài · Bài 03](../../tests/training-sandbox/020-curriculum-fireball/README.md) | Bản r1 đã kiểm tra tĩnh. Chờ va chạm mob, vị trí nổ khi chạm tường và kiểm tra không nổ khi hết tầm. |
| 2026-11-15 | [Chương trình 40 bài · Bài 03 r1](../../tests/training-sandbox/020-curriculum-fireball/evidence/user-confirmation-r1.md) | Người dùng xác nhận đã chạy đúng trong Minecraft và chấp nhận r1. Chưa ghi build và kết quả từng ca. |
| 2026-11-15 | [Chương trình 40 bài · Bài 04](../../tests/training-sandbox/021-curriculum-body-guard/README.md) | Bản r1 có 5 ca. Chờ thử hấp thụ, vỡ sớm, tự hết hạn và cooldown riêng. |
| 2026-11-15 | [Chương trình 40 bài · Bài 05](../../tests/training-sandbox/022-curriculum-whirlwind/README.md) | R1 có 6 ca thử mốc chém, bốn hướng, giới hạn cao độ, đích di chuyển và chém hụt. |
| 2026-11-15 | [CT-BM-04 · Kiểm tra cuối Cấp 1](../../tests/training-sandbox/023-foundation-assessment-decoy/README.md) | Đã mở r1 theo yêu cầu. Chờ thử tọa độ qua delay, đổi đích, chém hụt và hai caster. [Báo cáo Cấp 1](curriculum-005.md) |
| 2026-11-15 | [Chương trình 40 bài · Bài 06 Thunder Strike](../../tests/training-sandbox/024-curriculum-thunder-strike/README.md) | Bản r1 có 7 ca. Chờ thử điểm sét khi đổi hướng, sàn nhiều tầng, một lượt damage và không cháy block. |
| 2026-11-16 | [Chương trình 40 bài · Bài 07 Vampire Slash](../../tests/training-sandbox/025-curriculum-vampire-slash/README.md) | Bản r1 có 7 ca. Chờ đo damage, máu hồi, cú kết liễu, đánh hụt và hai caster. |
| 2026-11-16 | [Bài 07 Vampire Slash r2](../../tests/training-sandbox/025-curriculum-vampire-slash/README.md) | Điều chỉnh particle theo phản hồi. Thêm ca quan sát vệt chém và dấu hiệu hút máu. [Hồ sơ bản sửa](../corrections/MM-2026-008.md) |
| 2026-11-16 | [Bài 08 · Hàn Băng Địa Mạch r1](../../tests/training-sandbox/026-curriculum-frost-ground-surge/README.md) | Đề thay thế của Cấp 2. Có 8 ca để đo bám địa hình, dừng tường, hit, stun, khôi phục mask và ngân sách VFX. |

Các bài 001–014 và các phản hồi cũ giữ nguyên hồ sơ; mở [sandbox](../../tests/training-sandbox/README.md) và [hồ sơ lỗi](../corrections/README.md) để tiếp tục.

## Cập nhật khi hết mỗi nhiệm vụ

Ghi Task ID, yêu cầu gameplay, bản MythicMobs/addon và kết quả theo ca. Hồ sơ chính là README và `case.json` trong sandbox. Nếu sửa YAML, giữ bản gốc hoặc diff và dẫn bản được chấp nhận. Khi có phản hồi, soi đúng build, hash và kịch bản. Một nhận xét ngắn đủ để bắt đầu khoanh vùng theo triệu chứng, như animation so với tick gây damage hoặc “logic thừa” so với vai trò thực của từng guard. Khi một khác biệt thực sự đổi thiết kế, hỏi một câu tập trung về hành vi người chơi thấy.

Sau xác nhận, ghi ngày, nguồn xác nhận, lỗi đã xảy ra, nguyên nhân có bằng chứng, cách sửa, quyết định của người dùng, phạm vi và ngoại lệ. Gắn trạng thái gameplay theo hồ sơ runtime. Ghi bài học kỹ thuật trong [chỉ mục bài học](../../knowledge/player-skills/practice-lessons.md), lỗi trong [hồ sơ sửa lỗi](../corrections/README.md) và sở thích đã xác nhận trong [memory](../../memory/README.md). Dùng `CONFIRMED`, `OBSERVED`, `INFERRED` và `UNKNOWN` theo [schema](../../memory/schema.md). Có thể ghi kiểm tra tĩnh, trích dẫn wiki hoặc phản hồi nguyên văn ngay khi có bằng chứng; chờ xác nhận cho bài học tổng kết và lựa chọn gameplay còn mở.

## Báo cáo sau mỗi 5 bài

Khi `tools/training.py status` báo mốc, chạy `tools/training.py review <mốc>`. Nếu chưa có báo cáo của mốc, lưu `milestone-005.md`, `milestone-010.md`… tại đây theo các mục sau.

1. **Nhóm bài:** năm Task ID chưa tổng kết trước đó, build và bằng chứng cho từng bài, hoặc lý do chưa đủ dữ liệu để kết luận. Sau khi chọn, giữ danh sách trong lịch sử dù bản hiện tại của một bài được cập nhật.
2. **Lỗi và hồi quy:** lỗi đã sửa, lỗi còn lặp, trạng thái và hồ sơ từng ca. Nếu chưa từng gặp lỗi, ghi dữ liệu quan sát có sẵn.
3. **Mechanic và thuật toán:** cách đã chọn, nguồn, điểm đánh đổi, kết quả gameplay và giả thuyết còn mở.
4. **Memory:** dẫn ID câu hỏi và bản ghi quyết định được dùng lại. Chỉ đếm lần áp dụng thực tế liên quan nhóm bài. Dùng `tools/memory.py report` để đối chiếu số liệu gốc, có thể bằng 0.
5. **Bài mới:** chọn một [đề độc lập](../../tests/training-benchmarks/README.md) chưa dùng. Tạo đúng một ca `assessment` cho mốc, ghi lý do chọn giải pháp, kết quả quan sát và điều cần cải thiện. Chờ đủ bằng chứng trước khi kết luận đạt.
