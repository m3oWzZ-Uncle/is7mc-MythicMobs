# 008 · Kiếm quay quanh người chơi

Orbital hiển thị một kiếm item quay quanh caster. Bài quan sát bán kính, mốc kết thúc và scope chủ thể, chưa gắn sát thương.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingOrbitBlades`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `orbit` | Cast rồi đi vài block. Kiếm dự kiến quay quanh đúng người cast. |
| `expiry` | Giữ góc nhìn tới hết 60 tick và ghi liệu item hiển thị đã biến mất. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/slash-projectile.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
