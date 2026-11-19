# 013 · Vùng trúng lấy mẫu cùng cung VFX

Cùng Slash làm nguồn mẫu VFX và va chạm. Bán kính 0,6 mở rộng mẫu, nên cần đo biên dựa trên vị trí thật. Chọn đường nhìn để kiểm tra đòn qua tường.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingHitzoneVfx`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `edge` | Dùng dummy/mob thụ động, đứng trong mẫu và ngoài biên. Đo hit ở biên trong và ngoài. |
| `once` | Một đích đứng chồng nhiều mẫu, đích chỉ nhận một hit cho mỗi lượt Slash. |
| `wall` | Đích ở trong cung nhưng giữa hai bên có tường đặc. Kiểm tra lọc đường nhìn. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/slash-projectile.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
