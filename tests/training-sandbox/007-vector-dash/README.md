# 007 · Lướt theo vector tới điểm đích

Đo hiệu hai vị trí làm dữ liệu quan sát. Lunge nhận trực tiếp điểm đích để engine tính hướng. Phép trừ không được dùng để tự thay thế cơ chế lướt hoặc ép đến đúng block.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingVectorDash`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `vector` | Ngắm block đặc cách 3–6 ô. So ba thành phần delta với phép trừ tọa độ tại điểm caster và đích. |
| `dash` | Ngắm hai điểm khác hướng ở cùng cao độ. Player lướt theo điểm chọn, quan sát tường và quãng thực tế. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/../advanced-math/vectors.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
