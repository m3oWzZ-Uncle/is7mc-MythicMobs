# 005 · Cung kiếm khí

Slash lấy 16 điểm trên cung cấu hình và vẽ theo nhịp. Bài cô lập hình dạng trước khi đưa damage vào ca 013.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingArcBlade`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `arc` | Quay hai hướng trên sàn phẳng, cast một lần mỗi hướng. Cung xoay theo người cast. |
| `duration` | Quay video, kiểm tra cung hiện theo trình tự và hết hạt sau lượt. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/slash-projectile.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
