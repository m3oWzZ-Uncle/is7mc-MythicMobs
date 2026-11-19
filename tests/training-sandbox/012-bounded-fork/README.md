# 012 · Phân nhánh đạn, tối đa ba lượt tạo

Đạn cha sinh hai đạn VFX trong callback `onEnd` để việc chia nhánh gắn với kết thúc đường bay. Hai đạn con chỉ có callback vẽ vệt, không gọi bước sinh tiếp. Kiểm tra context hướng ở mốc cha kết thúc và số đạn trên build mục tiêu. Cấu hình không có bước đặt block. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) · [ProjectileForward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/ProjectileForward)

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingBoundedFork`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `hit` | Bắn vào một mob đứng yên. Ghi một cha và đúng hai vệt con. |
| `end-at-range` | Bắn theo hành lang trống. Hai nhánh xuất hiện một lần khi cha hết đường bay rồi biến mất. |
| `packed` | Xếp hai mob gần nhau. Kiểm tra giới hạn ba lượt tạo, hướng tách và không có thế hệ sau. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/slash-projectile.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
