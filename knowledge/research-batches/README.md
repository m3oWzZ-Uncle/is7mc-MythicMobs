# Tiến độ nghiên cứu catalog

Hai batch đầu dùng [dataset YAML đợt 01](../dataset-batch-01.md), đọc đúng trang của từng mục và dẫn các đoạn nguồn theo file/dòng. [Checkpoint](../research-checkpoint.json) là danh sách ID đã xử lý và thứ tự ưu tiên cho lần tiếp theo.

| Batch | Số mục | Phạm vi chính |
| --- | ---: | --- |
| [01](01.json) | 30 | Projectile, damage, delay, skill, summon, aura, biến, ModelEngine và các guard/targeter liên quan |
| [02](02.json) | 24 | Trigger, phase guards, AoE targeter, scope, metaskill và tích hợp MMO/ModelEngine |

Ảnh chụp ngày 13/11/2026 có 1.762 mục từ 29 nguồn danh mục và changelog. Trong 54 mục có bài riêng, 20 có ít nhất một cạnh tham chiếu khớp, 33 có ví dụ YAML đã parse và một mục có bằng chứng tài liệu. 1.708 mục còn ở trạng thái `indexed`. Tất cả mục chưa có bằng chứng riêng về phiên bản giữ `version.confirmed: null`. Chưa có ca Server Load Tested hoặc Gameplay Verified trong hai batch. [Quy ước kiểm chứng](../catalog-guide.md#mức-kiểm-chứng)

Batch 03 bắt đầu từ orbital, OnDamaged aura component, totem và các mục còn chờ theo `tools/kb.py next`. Các ví dụ vẫn cần build/edition thật để đo va chạm, trạng thái lúc bị ngắt, cleanup và tương tác giữa nhiều người chơi.
