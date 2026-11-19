# 009 · Đổi hệ trục cục bộ sang tọa độ thế giới

Tính offset 2 block trước, 1 block phải và 1 block cao từ yaw. Đổi độ sang radian trước sin/cos.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingLocalCoordinates`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `yaw-zero` | Yaw 0°, dự kiến offset (−1,1,2) từ chân. |
| `yaw-ninety` | Yaw 90°, dự kiến offset (−2,1,−1) từ chân. |
| `pitch` | Giữ yaw, đổi pitch. Marker vẫn ở cùng offset. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/../advanced-math/geometry.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
