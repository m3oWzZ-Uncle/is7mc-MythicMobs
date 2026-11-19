# Thực hành MythicMobs

Mỗi bài là một thư mục có ID riêng, hướng dẫn, YAML và hồ sơ bằng chứng. Các ví dụ và dữ liệu nguồn dùng để tra cứu. Bài thực hành chỉ ghi YAML trong thư mục này.

## Quy trình mỗi bài

1. **Tra cứu.** Đọc quyết định, lỗi cũ và pattern cùng bối cảnh qua [chỉ mục bộ nhớ](../../memory/index/README.md). Đối chiếu ví dụ nguồn, wiki của plugin sở hữu và build. Tự áp dụng câu trả lời đã xác nhận trong phạm vi phù hợp.
2. **Thiết kế.** Ghi hành vi kỳ vọng, lý do chọn cách triển khai và giả định có thể đổi kết quả. Khi có lựa chọn ảnh hưởng rõ đến gameplay, ghi điểm đánh đổi. Tách FACT (tài liệu hoặc kiểm thử), INFERENCE (từ YAML), và PREFERENCE (người dùng đã xác nhận).
3. **Triển khai.** Tạo bài có `README.md`, `case.json`, và các thư mục `Mobs/`, `Skills/`, `Items/` cần dùng. Đặt ID riêng để tránh trùng trên server test. Ghi mốc MythicMobs và addon cần thiết trong hồ sơ.
4. **Tự kiểm tra.** Chạy `check`. Đọc lại đường gọi và tham chiếu (kể cả callback/ID mà công cụ không thấy), trigger, targeter, condition, scope, timing/cooldown, animation/hitbox/damage khi liên quan, interrupt/cleanup, ảnh hưởng giữa nhiều người chơi và rủi ro tải. Ghi phần không áp dụng trong hướng dẫn nếu tác động đến phạm vi ca.
5. **Kiểm thử gameplay.** Chuẩn bị lệnh reload, kiểm tra ID, spawn và cleanup, cùng thao tác và kết quả kỳ vọng từng ca. Lưu log nạp, bản Minecraft/Paper và build/edition của plugin, kết quả quan sát và bằng chứng. Khi chưa có server, để trạng thái chờ runtime.
6. **Sửa theo phản hồi.** Khi có lỗi, lưu bản ban đầu hoặc diff trong [hồ sơ lỗi](../../feedback/corrections/README.md), tự tái hiện và khoanh vùng từ bằng chứng. Sửa trong sandbox, chạy lại kiểm tra tĩnh và cập nhật ca hồi quy. Chờ người dùng xác nhận kết quả sửa.
7. **Ghi bài học sau xác nhận.** Liên kết trong hồ sơ lỗi thiết kế ban đầu, lỗi, nguyên nhân, bản sửa cuối, nơi áp dụng và ngoại lệ, cùng bằng chứng. Ghi ca đã đạt trong hồ sơ bài, tạo hồi quy có thể chạy lại và lập chỉ mục qua [quy trình bộ nhớ](../../memory/README.md#bài-thực-hành-và-phản-hồi). Nếu bài đạt ngay, ghi cách làm, phạm vi và bằng chứng, không tạo lỗi giả.
8. **Đánh giá sau mỗi 5 bài.** Chạy `status` và `review <mốc>` khi đến hạn. Tổng kết trong [nhật ký](../../feedback/training/README.md), chọn [đề độc lập chưa dùng](../training-benchmarks/README.md) và giải trong ca `assessment` có `after_completed` bằng mốc. Nối lại ca đang mở nếu đã có. Ca đánh giá không tính vào nhóm 5. Chọn độ khó tiếp theo dựa trên kết quả có bằng chứng.

Cuối mỗi lượt, cập nhật Task ID, bản thử và bằng chứng vào nhật ký. Các bước chuẩn bị, xác minh kỹ thuật và xác nhận gameplay có thể tiến triển ở những lượt khác nhau.

## Kiểm tra và tiếp tục

```powershell
python -X utf8 tools/training.py check 001-counter-guard
python -X utf8 tools/training.py status
python -X utf8 tools/training.py review 5
python -B -X utf8 -m unittest discover -s tests -p test_training.py -v
```

Cài PyYAML nếu môi trường chưa có. Lệnh `check` dùng bộ đọc YAML hiện có để tìm parse lỗi, khóa/ID trùng trong bài và một số tham chiếu literal như `skill{s=...}`. Công cụ cần các đích tham chiếu literal được đóng gói cùng bài. Đọc bằng tay các ID động, inline, cú pháp addon và các tham chiếu chưa nhận diện. Kết quả tĩnh không xác nhận schema MythicMobs hoặc behavior runtime.

## Hồ sơ và bằng chứng

Xem [case.json của bài 001](001-counter-guard/case.json) để tạo hồ sơ ban đầu. `kind` là `practice` hoặc `assessment`. Chọn `level` theo độ khó và khai báo mọi kịch bản bắt buộc trong `required_scenarios`. `mythicmobs_target` là bản đối chiếu tài liệu. `dependencies` là danh sách addon cần chạy. Khi có bằng chứng thực tế, thêm đối tượng `runtime` với các trường dưới đây.

| Trường trong `runtime` | Bằng chứng cần ghi |
| --- | --- |
| `yaml_sha256` | Map đường dẫn YAML tương đối tới SHA-256, lấy từ lệnh `check` cho chính bản đã đưa lên server. |
| `environment` | `minecraft`, `server_build`, `mythicmobs_build`, `edition` và `addons` (map tên addon tới build thực tế). Nếu bản thực tế khác mốc đối chiếu, ghi chênh lệch và cách đã đối chiếu lại trong hướng dẫn bài. |
| `load` | `result` (`pass` hoặc `fail`), `artifact` (đường dẫn tương đối đến log), `registered` (danh sách `mob/ID`, `metaskill/ID` hoặc `item/ID` xác nhận trong lần nạp). |
| `scenarios` | Map từ ID kịch bản đến `result` (`pass` hoặc `fail`), `observed` (mô tả hoặc số liệu thực tế), `artifact` (đường dẫn tương đối đến log, ảnh, clip, hoặc biên bản có nguồn và điều kiện cụ thể). |

Lưu bằng chứng trong `evidence/` của bài, giữ lịch sử lần fail khi sửa. Có thể dùng chung tệp bằng chứng cho nhiều kịch bản nếu tệp ghi riêng hành vi từng ca. Rà nội dung trước khi ghi `pass`. Công cụ kiểm tra tệp tồn tại, hồ sơ đủ trường và hash khớp. Khi YAML thay đổi, chạy lại kiểm thử và thêm hồ sơ cho bản mới. Xác nhận của người dùng để ghi bài học cần lưu riêng với ngày, bối cảnh và liên kết tới ca đạt.

## Bài hiện có

- [001 · Bia phản kích khi bị đánh](001-counter-guard/README.md)
- [002 · Kiếm khí định hướng (bài #1 của người dùng)](002-directional-sword-wave/README.md)
- [003 · Lướt chém nhiều mục tiêu (bài #2 của người dùng)](003-boss-dash-cleave/README.md)
- [004 · Lướt theo hướng nhìn của người chơi](004-player-forward-dash/README.md)
- [005–014 · Mười bài Player Skill theo nghiên cứu IonTech](../../knowledge/player-skills/advanced/README.md)
- [015 · Khiên hấp thụ cá nhân](015-personal-guard/README.md)
- [016 · Thanh tẩy có chọn lọc](016-selective-cleanse/README.md)
- [017 · Hồi máu có báo trước](017-delayed-self-heal/README.md)
- [Chương trình 40 bài](../../training/curriculum.md) · [Bài 01 Kiếm Khí Trảm](018-curriculum-sword-wave/README.md) · [Bài 02 Ảnh Bộ](019-curriculum-shadow-step/README.md) · [Bài 03 Hỏa Cầu Thuật](020-curriculum-fireball/README.md) · [Bài 04 Hộ Thể](021-curriculum-body-guard/README.md) · [Bài 05 Toàn Phong Trảm](022-curriculum-whirlwind/README.md)

## Chọn bài thực hành và đánh giá

Khi tự chọn tình huống, ưu tiên theo định hướng 75% Player Skills, 15% Boss Skills và 10% Mob Skills. Giữ nguyên các bài cũ và chọn theo yêu cầu trực tiếp khi người dùng giao ca cụ thể. Sau mỗi 5 bài thực hành đạt, chọn tình huống mới chưa có trong bộ ví dụ theo quy trình ở trên. [Định hướng đã xác nhận](../../memory/decisions/player-skill-training-priority.json)

| Chủ đề player | Năng lực cần thể hiện |
| --- | --- |
| Dash và movement | Xác định player caster từ caller. Thử hướng nhìn, va chạm, cách kết thúc chuyển động và sự độc lập giữa hai player. |
| Kiếm combo và võ thuật | Thử thứ tự input, cửa sổ nối đòn, mốc hit, chém hụt và điều kiện hủy khi có yêu cầu. |
| Phép projectile | Kiểm tra đường bay, điểm va chạm, vùng damage và người đứng ngoài. |
| Triệu hồi | Kiểm tra owner, giới hạn theo caster nếu được yêu cầu, hết hạn và cleanup. |
| Phòng thủ và hỗ trợ | Kiểm tra đối tượng được bảo vệ, mốc buff và sự kiện phải chặn nếu có. |
| ModelEngine | Kiểm tra state trên đúng model, lúc hit và đường kết thúc hoặc ngắt. |
| Multiplayer và skill nhiều giai đoạn | Thử hai player cast giao nhau, scope dữ liệu, chi phí/cooldown đúng một lần và chính sách PvP/PvE của ca. |

Dùng các bài boss/mob để đánh giá riêng AI target, mốc chém của boss, chuyển phase hoặc dọn add khi phù hợp. Chọn độ khó theo kết quả đã có bằng chứng.
