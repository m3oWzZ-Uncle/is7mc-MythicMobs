# Tiến độ chương trình 40 bài

```powershell
python -X utf8 tools/training.py status --curriculum
python -X utf8 tools/training.py review 5 --curriculum
```

Tiến độ chương trình chỉ tính case sandbox có `program: "40-challenge"`. Bài thực hành có thêm `challenge` là số đề. Các bài cũ dùng để tham khảo và không cộng vào tổng chương trình. Status lấy bằng chứng từ `case.json` và hash YAML. Tệp này lưu lịch sử phản hồi và các số liệu cần đọc theo bối cảnh.

| Bài | Case | Bản đang thử | Số lần sửa vì phản hồi | Trạng thái |
| --- | --- | --- | --- | --- |
| 01 | [018-curriculum-sword-wave](../tests/training-sandbox/018-curriculum-sword-wave/README.md) | r1 | 0 | Người dùng đã thử và chấp nhận. Hồ sơ tự động còn thiếu build, log nạp và kết quả riêng từng ca. |
| 02 | [019-curriculum-shadow-step](../tests/training-sandbox/019-curriculum-shadow-step/README.md) | r1 | 0 | `syntax-checked`, chờ kết quả gameplay và xác nhận |
| 03 | [020-curriculum-fireball](../tests/training-sandbox/020-curriculum-fireball/README.md) | r1 | 0 | Người dùng đã thử và chấp nhận. Hồ sơ tự động còn thiếu build, log nạp và kết quả riêng từng ca. |
| 04 | [021-curriculum-body-guard](../tests/training-sandbox/021-curriculum-body-guard/README.md) | r1 | 0 | `syntax-checked`, chờ kết quả gameplay và xác nhận |
| 05 | [022-curriculum-whirlwind](../tests/training-sandbox/022-curriculum-whirlwind/README.md) | r1 | 0 | `syntax-checked`, chờ log nạp, ca gameplay và xác nhận |
| 06 | [024-curriculum-thunder-strike](../tests/training-sandbox/024-curriculum-thunder-strike/README.md) | r1 | 0 | Chờ log nạp, ca gameplay và xác nhận |
| 07 | [025-curriculum-vampire-slash](../tests/training-sandbox/025-curriculum-vampire-slash/README.md) | r2 | 1 | Chờ log nạp, ca gameplay và xác nhận |
| 08 | [026-curriculum-frost-ground-surge](../tests/training-sandbox/026-curriculum-frost-ground-surge/README.md) | r1 | 0 | Chờ log nạp, thử gameplay và xác nhận |
| 09–40 | [Đề bài](curriculum.md) | — | 0 | Chờ người dùng yêu cầu triển khai |

**Kiểm tra cuối Cấp 1:** [CT-BM-04 · Đánh lạc hướng](../tests/training-sandbox/023-foundation-assessment-decoy/README.md) đã mở theo yêu cầu. Bản r1 đang chờ thử trong Minecraft. Bài đánh giá được theo dõi riêng tại [báo cáo Cấp 1](../feedback/training/curriculum-005.md).

## Xác nhận và thống kê

- **Hoàn thành:** theo `status --curriculum`. Với từng bài, ghi log và kết quả đủ kịch bản theo [hồ sơ runtime](../tests/training-sandbox/README.md#hồ-sơ-và-bằng-chứng). Thêm `runtime.user_confirmation` gồm `date`, `statement` và `artifact` tương đối tới biên bản hoặc bằng chứng cho xác nhận trực tiếp của người dùng. Nêu Task ID và bản đã thử trong biên bản. Hash YAML đổi thì cần kết quả trên bản mới.
- **Lần sửa:** đếm một lần khi bản YAML đã đưa thử được chỉnh vì phản hồi. Mỗi sự kiện ghi Task ID, bản trước → bản sau, mã lỗi, bằng chứng hoặc diff và kết quả retest. Bản r1 không tính là lần sửa.
- **Lỗi và lỗi lặp:** liên kết [hồ sơ lỗi](../feedback/corrections/README.md). Ghi nguyên nhân đã xác minh hoặc giả thuyết riêng. Nếu lỗi từng đóng quay lại, dùng lại ID để nhận diện và ghi lần tái hiện mới.
- **Tái sử dụng:** ghi pattern hoặc ID quyết định, hành vi đã áp dụng và ca kiểm chứng. Nếu thực sự tránh câu hỏi đã có đáp án, ghi ID câu hỏi theo [memory](../memory/README.md). Mở bài cũ để tham khảo chỉ tính là tra cứu.
- **Kỹ thuật được kiểm chứng:** ghi mechanic, build, hành vi, ngoại lệ và ca xác minh trong [chỉ mục bài học](../knowledge/player-skills/practice-lessons.md). Khi chưa có kết quả runtime, giữ trạng thái chờ test.

## Nhật ký sự kiện

| Bài/bản | Lỗi hoặc phản hồi | Kinh nghiệm sử dụng | Kết quả và bằng chứng |
| --- | --- | --- | --- |
| 01/r1 | Chưa có phản hồi gameplay | Pattern đường bay/hit tách biệt và quy tắc chỉ thêm guard có lý do, phạm vi bài PvE | Đã kiểm tra YAML và tham chiếu. Chưa có kỹ thuật gameplay được xác nhận hoặc câu hỏi thực sự được tránh trong chương trình. |
| 01/r1 | Người dùng báo chạy đúng trong Minecraft và chấp nhận bản hiện tại | Giữ minh họa projectile PvE theo hướng nhìn và tách VFX khỏi damage | [Xác nhận kèm hash](../tests/training-sandbox/018-curriculum-sword-wave/evidence/user-confirmation-r1.md) · [Bài học có phạm vi](../knowledge/player-skills/projectiles/kiem-khi-tram.md) |
| 02/r1 | Người dùng yêu cầu tiếp tục Bài 02 | Tra bài 004 để chọn cú đẩy ngang một lần. Không áp quyết định riêng của Dash Cleave. | [Ca Ảnh Bộ](../tests/training-sandbox/019-curriculum-shadow-step/README.md) |
| 02/r1 | Người dùng đánh giá dash chung đúng và phân biệt biến thể Ảnh Bộ đi bộ | Thử hạ điểm ngắm khi gameplay cần cảm giác sát nền | [Quyết định đã xác nhận và ca A/B](../feedback/decisions/MM-D-2026-003.md). Chưa có kết quả A/B. |
| 03/r1 | Người dùng yêu cầu tiếp tục Bài 03 | Tái sử dụng vệt projectile của Kiếm Khí Trảm và callback impact từ pattern AoE | [Ca Hỏa Cầu Thuật](../tests/training-sandbox/020-curriculum-fireball/README.md) |
| 03/r1 | Người dùng báo chạy đúng trong Minecraft và chấp nhận hiện trạng | Giữ ví dụ PvE về va chạm, AoE và đường nhìn từ tâm nổ | [Xác nhận](../tests/training-sandbox/020-curriculum-fireball/evidence/user-confirmation-r1.md) · [Bài học](../knowledge/player-skills/projectiles/hoa-cau-thuat.md) |
| 04/r1 | Người dùng yêu cầu tiếp tục Bài 04 | Tái sử dụng cấu hình khiên cá nhân để thử hấp thụ, hết hạn và hồi chiêu | [Ca Hộ Thể](../tests/training-sandbox/021-curriculum-body-guard/README.md) |
| 04/r1 | Người dùng đề xuất Hộ Thể giảm sát thương trong thời gian buff | Ưu tiên Resistance hoặc stat theo hệ xử lý damage. Tránh dùng lệnh MythicLib mặc định. | [Quyết định đã lưu](../feedback/decisions/MM-D-2026-004.md). Chưa có kiểm thử biến thể. |
| 05/r1 | Người dùng yêu cầu tiếp tục Bài 05 | Tách cảnh báo, animation và truy vấn vùng một lần tại tick chém | [Ca Toàn Phong Trảm](../tests/training-sandbox/022-curriculum-whirlwind/README.md) |
| 05/r1 | Người dùng đánh giá bản không model ổn và mô tả biến thể chém 180° có model | Tách model báo và model chém, chọn Totem hoặc targeter theo hình vùng trúng | [Quyết định và ca đối chiếu](../feedback/decisions/MM-D-2026-005.md). Chưa có xác nhận gameplay bản r1 hoặc biến thể. |
| 06/r1 | Người dùng yêu cầu bài đầu Cấp 2 | Chốt điểm từ lúc báo. Tách sét trang trí và damage, xét đường nhìn từ tâm như bài Hỏa Cầu Thuật. | [Ca Thunder Strike](../tests/training-sandbox/024-curriculum-thunder-strike/README.md). Chờ thử trên MythicMobs Premium. |
| 07/r1 | Người dùng yêu cầu bài thứ hai Cấp 2 | Giữ cú vung khi hụt. Tính hồi trên sát thương sau giảm trừ và máu còn trước đòn. | [Ca Vampire Slash](../tests/training-sandbox/025-curriculum-vampire-slash/README.md). Chờ thử callback trên MythicMobs 5.14.0 Premium. |
| 07/r1 → r2 | Người dùng đánh giá thuật toán ổn và yêu cầu chăm chút hiệu ứng particle vanilla | Thêm cung chém, điểm nhấn trắng và dấu hiệu hút máu. | [Phản hồi và diff](../feedback/corrections/MM-2026-008.md). Chờ thử hiệu ứng và các ca damage/hồi máu trên r2. |
| 08/r1 | Người dùng thay Bài 03 Cấp 2 bằng Hàn Băng Địa Mạch | Dùng HugSurface, nhánh tường riêng, mẫu băng có hạn và lồng hai tầng gắn với stun. | [Ca 026](../tests/training-sandbox/026-curriculum-frost-ground-surge/README.md). Chờ thử bước leo, dừng tường và tải nhiều caster. |

Tại mỗi mốc 5 bài hoàn thành, lưu `curriculum-005.md`, `curriculum-010.md`… trong [nhật ký huấn luyện](../feedback/training/README.md). Tổng kết số lỗi, lỗi lặp, cơ chế tái sử dụng, câu hỏi đã tránh và kỹ thuật có bằng chứng. Chọn một [đề đánh giá mới](../tests/training-benchmarks/curriculum.md) để dùng khi người dùng yêu cầu. Bài đánh giá của chương trình dùng `kind: "assessment"`, `program: "40-challenge"` và `after_completed` bằng mốc.
