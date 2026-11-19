# Dữ liệu bản ghi bộ nhớ

Bản ghi JSON UTF-8 có đường dẫn `memory/<category>/<id>.json`. `id`, `topic`, tag và điều kiện dùng chữ thường ASCII, chữ số và dấu gạch nối. Cùng một vấn đề dùng cùng `topic` để đối chiếu lựa chọn.

```json
{
  "id": "simple-full-gameplay",
  "category": "preferences",
  "title": "Chọn kiến trúc đơn giản nhất đáp ứng gameplay",
  "topic": "architecture-complexity",
  "summary": "Chọn phương án đơn giản nhất giữ đủ hành vi yêu cầu.",
  "context": "Dùng khi các lựa chọn đều đạt cùng mục tiêu gameplay.",
  "exceptions": "Đánh giá phương án đủ hành vi nếu phương án đơn giản làm mất hành vi yêu cầu.",
  "scope": "global",
  "claim": "PREFERENCE",
  "confidence": "CONFIRMED",
  "recorded": "2026-11-13",
  "answer": "simplest-complete-design",
  "tags": ["gameplay", "kien-truc"],
  "requires": ["gameplay-requirements-known", "equivalent-gameplay"],
  "sources": [{"type": "user", "ref": "AGENTS.md", "note": "Quy tắc kiến trúc do người dùng xác nhận."}]
}
```

Mỗi bản ghi có `id`, `category`, `title`, `topic`, `summary`, `context`, `exceptions`, `scope`, `claim`, `confidence` và `recorded`. Bằng chứng dùng `sources` với `type` (`user`, `document`, `yaml`, `test`, `observation`), `ref` (đường dẫn tương đối từ repo, có thể kèm mốc dòng, hoặc URL HTTPS) và `note` nêu điều được chứng minh. Ghi phiên bản và phạm vi trong `context` hoặc bằng chứng nếu có. Ghi trích dẫn ngắn hoặc diễn giải sát nghĩa tại hồ sơ nguồn khi người dùng xác nhận. Chỉ lưu thông tin cần cho nhiệm vụ về sau.

| Độ tin cậy | Ý nghĩa |
| --- | --- |
| `CONFIRMED` | Dữ kiện có bằng chứng phù hợp. `PREFERENCE` và quyết định đã xác nhận cần nguồn trực tiếp từ người dùng. |
| `OBSERVED` | Có quan sát từ nhiều trường hợp, chưa có xác nhận thành quy tắc chung. |
| `INFERRED` | Suy luận có căn cứ, chỉ dùng với `INFERENCE`. |
| `UNKNOWN` | Chưa đủ dữ liệu để xác định. |

`claim` là `FACT`, `INFERENCE` hoặc `PREFERENCE`. Độ tin cậy của quyết định và mức kiểm thử MythicMobs là hai trường riêng. Nếu có `verification`, dùng nhãn và bằng chứng theo [hướng dẫn kiểm thử](../tests/README.md). `server-loaded` và `verified-in-game` cần một nguồn `test` có đường dẫn bằng chứng, trường `build` và `result`. Khi có bằng chứng mới cho một suy luận, thêm kết luận có nguồn và dùng `resolves` để giữ lịch sử.

| Trường bổ sung | Cách dùng |
| --- | --- |
| `answer` | Slug của lựa chọn trong `decisions` và `preferences` đã xác nhận. Hai hồ sơ mô tả cùng lựa chọn dùng cùng slug. |
| `tags`, `requires`, `excludes` | Từ khóa, các điều kiện phải có và các điều kiện loại trừ. `context` và `exceptions` giải thích bằng lời. |
| `related` | ID bộ nhớ liên quan. Dẫn tới mechanic, pattern hoặc bài kiểm tra ngoài bộ nhớ qua `sources`. |
| `supersedes` | ID quyết định trước, cùng chủ đề. Chỉ thay thế trong bối cảnh mà quyết định mới khớp. |
| `resolves` | ID điểm chưa rõ, suy luận hoặc hồ sơ lỗi mở đã giải quyết. Dùng cùng chủ đề, phạm vi và điều kiện. |
| `decision` | Trong `questions`, ID quyết định hoặc ưu tiên đã xác nhận. Dùng cùng chủ đề và phạm vi. |
| `status`, `regression` | Hồ sơ `corrections` dùng `open`, `checking`, `confirmed` hoặc `technical`. `confirmed` có xác nhận người dùng và đường dẫn bài hồi quy. `technical` dành cho kết quả có bằng chứng về công cụ, độc lập với xác nhận gameplay. |
| `result`, `question` | Trong `conversations`, dùng `reused-answer` và ID câu hỏi đã trả lời khi một nhiệm vụ thật sự dùng câu trả lời đó. |
