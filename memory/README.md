# Bộ nhớ dài hạn MythicMobs

Codex học từ các hồ sơ trên đĩa, tra cứu chúng khi làm việc và ghi bài học có căn cứ sau nhiệm vụ. Các hồ sơ gốc nằm trong `knowledge/`, `feedback/`, `examples/` và `incoming/`. Bộ nhớ lưu tóm tắt và đường dẫn tới bằng chứng. Việc này không thay đổi trọng số mô hình.

## Tra cứu khi làm việc

Chạy tại thư mục `MythicMobs-AI-Training` với Python 3.10 trở lên. Công cụ dùng thư viện chuẩn. Nếu Windows trỏ `python` tới alias Microsoft Store, dùng đường dẫn Python đã cài hoặc lệnh `py -3` nếu có.

```powershell
python -X utf8 tools/memory.py search "khóa hướng boss telegraph"
python -X utf8 tools/memory.py search "Conductor callback" --project carimc --category corrections
python -X utf8 tools/memory.py resolve architecture-complexity --project tutien --context gameplay-requirements-known --context equivalent-gameplay --impact minor
python -X utf8 tools/memory.py resolve boss-cleave-direction --project tutien --context boss --context melee-cleave --context multiplayer --impact material
python -X utf8 tools/memory.py report
```

1. Đọc `AGENTS.md` và [chỉ mục bộ nhớ](index/README.md). Xác định project, mục tiêu gameplay và điều kiện từ yêu cầu, YAML hiện tại và ví dụ liên quan. Tra cứu theo thuật ngữ hoặc alias. `search` hỗ trợ từ khóa tiếng Việt có dấu hoặc không dấu. Mở các bản ghi phù hợp và kiểm tra nguồn khi áp dụng. Với cú pháp và phiên bản, tiếp tục qua [catalog](../knowledge/catalog-guide.md).
2. Trước khi hỏi, tìm theo chủ đề và từ khóa đồng nghĩa trong `questions`, `decisions`, `profile`, `preferences`, [nhật ký quyết định](../feedback/decisions/README.md), cấu hình hiện tại và ví dụ cũ. Khi đã biết `topic`, dùng `resolve` với project và các `--context` đã có bằng chứng. Đọc cả `context` và `exceptions` của bản ghi phù hợp. Khi câu trả lời cũ đã đủ cho trường hợp này, tự áp dụng và ghi lần sử dụng lại.
3. `apply` gợi ý một lựa chọn đã xác nhận. `review-conflict` yêu cầu đọc các nguồn và phạm vi trước khi chọn. Nếu còn điểm chưa rõ có thể đổi gameplay, hỏi đúng một câu về điểm đó. Với chi tiết nhỏ dễ đổi, dùng mặc định hợp lý. Với pattern gần giống, ghi giả định quan trọng rồi kiểm tra phạm vi áp dụng. Tiếp tục công việc độc lập với câu hỏi đang mở.

`--project tutien` xét hồ sơ `global` và `project:tutien`. Tương tự với `survival`, `skyrng`, `carimc` hoặc slug khác đã xác định từ nguồn. Khi bỏ `--project`, chỉ xét `global`. Thiếu một điều kiện `requires` hoặc có một điều kiện `excludes` sẽ khiến quyết định nằm trong nhóm cần đọc thêm. Hai lựa chọn trái nhau cùng khớp thì giữ mâu thuẫn để xem bằng chứng. Dùng `supersedes` khi hồ sơ xác nhận thay thế quyết định cũ và ghi rõ phạm vi thay thế.

Dùng `--impact material` khi chọn sai có thể đổi gameplay hoặc gây nhiều việc phải sửa. Dùng `--impact minor` cho chi tiết nhỏ có thể đổi dễ dàng.

## Cập nhật sau nhiệm vụ

Khi tự chọn ca học hoặc câu hỏi tiếp theo, ưu tiên player skill theo [quyết định định hướng](decisions/player-skill-training-priority.json). Tra [chỉ mục Player Skills](../knowledge/player-skills/README.md) và xác định caster từ caller trước khi áp dụng kinh nghiệm cũ. Với task boss/mob, tra các quyết định đúng bối cảnh loại caster đó. Tỷ lệ học định hướng việc chọn ca và không giới hạn nhiệm vụ được giao.

| Thư mục | Nội dung |
| --- | --- |
| `profile/` | Tóm tắt và đường dẫn tới [hồ sơ tư duy](../knowledge/learning-profile.md). |
| `decisions/` | Lựa chọn đã xác nhận trong một tình huống, dẫn tới [nhật ký](../feedback/decisions/README.md). |
| `preferences/` | Tiêu chí do người dùng xác nhận kèm phạm vi, điều kiện và ngoại lệ. |
| `corrections/` | Hành vi cũ, kết quả mong muốn, nguyên nhân, bản sửa và kiểm thử khi có. Dẫn về [hồ sơ lỗi](../feedback/corrections/README.md). |
| `conversations/` | Tóm tắt các phiên quan trọng và các lần thực sự áp dụng câu trả lời cũ. |
| `questions/` | Câu hỏi đã được trả lời, dẫn đến một quyết định hoặc ưu tiên xác nhận cùng chủ đề và phạm vi. |
| `patterns/` | Mẫu tư duy có bằng chứng hoặc suy luận ghi rõ mức tin cậy, dẫn tới [thư viện pattern](../knowledge/patterns/README.md). |
| `uncertainties/` | Câu hỏi đang mở và các điểm còn thiếu bằng chứng. |
| `index/` | Chỉ mục sinh từ các bản ghi và báo cáo hiện trạng. |

Sau nhiệm vụ, chọn điều có giá trị lâu dài và kiểm tra xem đã có bản ghi tương đương chưa. Ghi xác nhận vào hồ sơ nguồn trước. Khi có phản hồi về bản sửa, ghi hành vi trước, mong đợi, nguyên nhân, bản sửa đã xác nhận, mechanic/pattern liên quan và ca hồi quy. Trong thời gian chờ người dùng, ghi `open` hoặc `checking`. Với câu hỏi đang chờ đã có câu trả lời, tạo quyết định rồi thêm bản ghi `questions` liên kết tới quyết định đó. Ghi `resolves` nếu câu trả lời giải quyết đúng phạm vi đang mở. Giữ các câu trả lời hoặc bản sửa cũ trong lịch sử. [Mẫu bản ghi và trường dữ liệu](schema.md)

```powershell
python -X utf8 tools/memory.py add <duong-dan-den-file-json>
python -X utf8 tools/memory.py validate
python -X utf8 tools/memory.py index
```

`add` tạo bản ghi mới và từ chối ID đã có. `search` và `resolve` đọc các bản ghi hiện tại trên đĩa, nên truy xuất có hiệu lực ngay khi ghi xong. `index` tạo lại `index/records.json` để đọc nhanh và xem thống kê. Nếu trong công việc đã thực sự tái sử dụng một câu trả lời, thêm một bản ghi `conversations` có `result: "reused-answer"` và `question` là ID câu hỏi. Báo cáo đếm cả số câu hỏi khác nhau và số lần áp dụng. Các lượt kiểm thử và truy vấn tra cứu không tính vào số sử dụng thực tế.

## Bài thực hành và phản hồi

Cuối mỗi nhiệm vụ, tự ghi phần đã có bằng chứng vào [nhật ký huấn luyện](../feedback/training/README.md) và trỏ tới Task ID. Ghi phản hồi nguyên văn hoặc diễn giải sát nghĩa khi cần. Giữ giả thuyết dưới trạng thái mở, xác nhận nguyên nhân từ ca tái hiện, rồi dẫn bản gốc và bản được chấp nhận. Sau khi chốt bài, thêm đường dẫn vào [chỉ mục bài học](../knowledge/player-skills/practice-lessons.md).

Tra các bài trong [sandbox](../tests/training-sandbox/README.md) cùng với quyết định và hồ sơ lỗi trước khi làm tiếp. Dùng `tools/training.py status` để tìm bài đang chờ log, ca gameplay còn thiếu hoặc mốc đánh giá đã đến. Trạng thái kiểm thử ở hồ sơ bài theo bản YAML và môi trường chạy. Tóm tắt những gì đã học sau khi người dùng xác nhận kết quả.

- Khi sửa lỗi, lưu thiết kế ban đầu, lỗi, nguyên nhân, giải pháp cuối, điều kiện tái sử dụng và ngoại lệ trong hồ sơ lỗi. Liên kết tới ca hồi quy, bằng chứng thử nghiệm và lời xác nhận. Dùng `corrections` để tìm lại hồ sơ này.
- Với kỹ thuật đã xác minh và có thể lặp lại, ghi FACT với nguồn và phạm vi vào pattern hoặc hồ sơ phù hợp. Giữ phần giải thích nguyên nhân chưa chứng minh ở mức INFERENCE và nêu cách kiểm tra.
- Với lựa chọn gameplay người dùng xác nhận, lưu PREFERENCE vào `decisions` hoặc `preferences` theo bối cảnh và ngoại lệ. Giá trị dùng trong bài, kết quả test và dự đoán của Codex không tự tạo sở thích.
- Sau khi thêm bản ghi, chạy `tools/memory.py validate` và `tools/memory.py index` để phiên sau tra được bài học từ nguồn gốc.
