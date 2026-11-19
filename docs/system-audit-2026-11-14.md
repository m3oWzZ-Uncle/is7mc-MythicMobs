# Kiểm tra MythicMobs-AI-Training · 14/11/2026

Phạm vi gồm cây thư mục project, dữ liệu kiểm kê, catalog, hồ sơ bộ nhớ, hướng dẫn Codex và kiểm thử CLI. Đợt này kiểm tra bằng chứng cục bộ và các liên kết đã lưu. Build MythicMobs 5.14.0 là mốc tham chiếu ghi trong Knowledge Base. [Nguồn và phiên bản](wiki/README.md)

| Hạng mục | Kết quả |
| --- | --- |
| Knowledge Base | 1.762 mục trong catalog. 54 mục có bài chi tiết, gồm 33 `YAML Parsed`, 20 `Reference Checked` và 1 `Documented`. 1.708 mục ở mức chỉ mục. Có 14 pattern, hồ sơ tư duy, tài liệu phase boss và hiệu năng. Catalog bao gồm mechanics, targeters, conditions, triggers, variables, metaskills, attributes, placeholders và tích hợp. [Mục lục](../knowledge/README.md) |
| Dữ liệu YAML | Kiểm kê 386 file trong `incoming/`, gồm 214 YAML rời và 145 archive. Đã phân tích 30 YAML rời ở đợt 01. Còn 184 YAML rời chưa phân tích theo chỉ mục. Nội dung YAML trong archive vẫn chờ xử lý. [Dataset](../knowledge/dataset-index.md) |
| Bộ nhớ dài hạn | Có bản ghi JSON, schema, chỉ mục và lệnh `add`, `search`, `resolve`, `validate`, `index`, `report`. Khi chạy, CLI đọc dữ liệu từ đĩa. Codex dùng hướng dẫn để chọn điều kiện và ghi hồ sơ có căn cứ trong quá trình làm việc. [Quy trình](../memory/README.md) |
| Tích hợp Codex | `AGENTS.md` và `mythicmobs-expert` đều dẫn tới chỉ mục và quy trình. Có bằng chứng phiên Codex mới từ đợt triển khai trước. [AGENTS.md](../AGENTS.md), [Skill](../.agents/skills/mythicmobs-expert/SKILL.md), [Kiểm thử phiên mới](../memory/index/assessment.md) |
| Chống hỏi lặp và ghi lỗi | `resolve` kiểm tra project, điều kiện, xung đột và câu trả lời đã xác nhận. Có quy trình phản hồi, hồ sơ lỗi và mẫu hồi quy. Đã sửa việc mục đã giải quyết vẫn xuất hiện trong `review` ở bối cảnh khớp. [Hồ sơ sửa lỗi](../feedback/corrections/MM-2026-003.md) |
| Thư mục chưa có dữ liệu thực | `memory/decisions/` và `memory/questions/` hiện chỉ có hướng dẫn. Chức năng ghi và tra đã qua kiểm thử. Chúng chờ xác nhận thực của người dùng. `examples/advanced/`, `examples/bosses/` và `examples/modelengine/` trước đây chỉ có mô tả. Nay dẫn tới mẫu nguồn và ca kiểm thử liên quan. Các thư mục này chưa có pack mẫu độc lập. Các thư mục trống dưới `incoming/` thuộc cây dữ liệu nguồn. |

## Kết quả kiểm thử

- `tools/kb.py validate` đạt, kiểm tra 1.762 mục, 54 bài và 14 hash ví dụ. `tools/memory.py validate` đạt với 8 bản ghi thật.
- 11 ca hồi quy Python đạt. Ca liên tiến trình tạo quyết định và câu trả lời bằng `add`, tra bằng `search` và `resolve` trong các tiến trình mới, nhận `apply` và đúng đáp án. Project khác không nhận quyết định. Bộ test xác nhận thư mục tạm đã bị xóa. [Ca kiểm thử](../tests/test_memory.py)
- Báo cáo bộ nhớ thật vẫn có 1 ưu tiên xác nhận, 0 quyết định tình huống, 0 câu hỏi có đáp án và 0 lượt tái sử dụng trong công việc. [Thống kê](../memory/index/records.json)

## Việc còn cần người dùng thực hiện

1. Khi muốn tiếp tục học quyết định, trả lời tình huống đòn quét boss đang mở hoặc xác nhận một lựa chọn từ công việc thật. Codex sẽ ghi lựa chọn và điều kiện vào hồ sơ. [Tình huống đòn quét](../feedback/decisions/MM-D-2026-001.md)
2. Khi muốn nâng mức kiểm chứng gameplay, cung cấp build Minecraft/server/MythicMobs và addon, kèm log nạp và video hoặc kết quả tái hiện. Ưu tiên mốc animation–hitbox Lục Cốt và luồng callback Conductor nếu hai phần này còn dùng. [Kiểm thử server](../tests/README.md)

Đợt này kiểm thử bộ nhớ và bằng chứng cục bộ. Chưa nạp YAML hay kiểm thử gameplay trên Minecraft server.
