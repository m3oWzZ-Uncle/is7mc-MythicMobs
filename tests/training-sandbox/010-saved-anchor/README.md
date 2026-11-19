# 010 · Giữ điểm neo qua các giai đoạn

Lưu LOCATION trong skill tree. Hai VFX đọc một neo tại hai thời điểm dù player quay hoặc đi chỗ khác.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingSavedAnchor`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `move` | Cast rồi quay và di chuyển trong 12 tick. Hai hiệu ứng vẫn xuất hiện tại điểm cũ. |
| `two-casters` | A và B cast gần nhau ở hai hướng. Mỗi người có mốc riêng. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/../advanced-variables/README.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
