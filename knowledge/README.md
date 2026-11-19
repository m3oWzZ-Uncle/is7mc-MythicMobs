# Knowledge Base MythicMobs

Bắt đầu từ [hướng dẫn tra cứu catalog](catalog-guide.md) để tìm theo tên, alias, plugin hoặc mục đích. [Checkpoint nghiên cứu](research-checkpoint.json) lưu các mục đã hoàn thành và hàng chờ.

Tra [thư viện wiki đã nhập](../docs/wiki/thu-vien.md) để tìm Markdown gốc theo chủ đề, so phiên bản và xem các batch đối chiếu trong [`wiki-research`](wiki-research/README.md).

Khi cần áp dụng tiêu chí thiết kế của người dùng hoặc tiếp tục phỏng vấn, mở [hồ sơ tư duy](learning-profile.md) và [chỉ mục quyết định](../feedback/decisions/README.md).

Đối chiếu ngày 13/11/2026 với wiki MythicCraft. Mốc tham chiếu là **MythicMobs 5.14.0**, bản phát hành của Lumine. Build Minecraft, nền server, bản Free/Premium và các addon của project thực tế sẽ lấy từ hồ sơ trong `incoming/`. Mỗi bài phân biệt phần wiki mô tả với thay đổi có mốc rõ trong changelog và các kịch bản cần chạy trên server. [Nguồn và phiên bản](../docs/wiki/README.md)

| Nhóm | Nội dung |
| --- | --- |
| [Player Skills](player-skills/README.md) | Điểm vào active/passive, caster người chơi, combat, movement, projectile, combo, model và tích hợp MMO |
| [IonTech và thiết kế module](modular-design/README.md) | Kiểm kê, phụ thuộc, thuật toán, handler và checkpoint |
| [Advanced Math](advanced-math/README.md) · [Advanced Variables](advanced-variables/README.md) | Vector, biến đổi tọa độ, va chạm, scope và danh sách |
| [Mechanics](mechanics/README.md) | Dòng skill, thời gian, damage, projectile, aura, interrupt |
| [Targeters](targeters/README.md) | Caster, trigger, mục tiêu AI, origin, kế thừa và bộ lọc |
| [Conditions](conditions/README.md) | Đối tượng được xét, condition actions, ngưỡng máu và inline conditions |
| [Variables](variables/README.md) | Scope, kiểu, khởi tạo, vòng đời và dữ liệu giữa các lượt cast |
| [Metaskills](metaskills/README.md) | Gọi skill, cooldown, mục tiêu rỗng, kế thừa và phân nhánh |
| [Boss phases](architecture/boss-phases.md) | Ngưỡng máu, chuyển phase một lần, reset, cleanup và multiplayer |
| [Hiệu năng](architecture/performance.md) | Timer, target scan, projectile, particle và đo với spark |

Đọc [kiểm kê dữ liệu](../docs/kiem-ke.md) để chọn case đầu tiên, dùng [hướng dẫn nạp dữ liệu](../incoming/README.md) để ghi lại build và bằng chứng. [Ví dụ tương tác](../examples/simple/README.md) có cặp file mob và skill riêng để thử quy trình.

Dữ liệu thực tế trong `incoming/` có [chỉ mục dataset](dataset-index.md) và [checkpoint từng đợt](dataset-checkpoint.json).

[Mục lục pattern theo nhu cầu](patterns/README.md) dẫn đến các kỹ thuật rút từ YAML thực tế, kèm trích đoạn nguồn, sơ đồ và mức xác minh.
