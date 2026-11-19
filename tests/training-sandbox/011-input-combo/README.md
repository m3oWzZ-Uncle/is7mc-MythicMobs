# 011 · Hai lần vung tay trong một cửa sổ

Item bridge được cô lập bằng lệnh test để mở cửa sổ 40 tick. Hai lần vung tay đến từ các event riêng nên dùng caster scope và TTL. Kết thúc dọn aura và counter. Điều kiện ngưỡng 2 là luật gameplay.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingInputCombo`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `two-inputs` | Cast rồi vung tay hai lần vào không khí trong 2 giây. Thấy một VFX ở lần thứ hai. |
| `timeout` | Một lần swing rồi chờ hết cửa sổ. Swing muộn không hoàn thành combo. |
| `multiplayer` | Hai player mở cửa sổ và xen kẽ swing. Mỗi bên cần đủ hai input riêng. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/handlers.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
