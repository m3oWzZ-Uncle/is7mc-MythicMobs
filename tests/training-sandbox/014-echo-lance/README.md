# 014 · Thương vọng · nhắm, cảnh báo và bắn theo loạt

Player khóa điểm ngắm, báo trước rồi bắn hai đạn từ player đến điểm đó. Mỗi đạn tự xử lý va chạm. Hướng có thể thay đổi nếu player di chuyển vì chỉ lưu điểm đích. Đây là ca PvE trên arena thử; cấu hình cần kiểm tra các loại entity hợp lệ trước khi dùng ngoài arena.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingEchoLance`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `timing` | Đo cảnh báo, đạn thứ nhất tại 12 tick và đạn thứ hai tại 18 tick. Không có damage trước đạn chạm. |
| `anchor` | Quay giữa lúc chờ và thử thêm lượt đi ngang. Đạn vẫn nhắm điểm cảnh báo, đường bay đổi nếu vị trí phát thay đổi. |
| `isolation` | Hai caster dùng hai làn và hai dummy. Kiểm tra đạn, neo và cooldown độc lập. |
| `wall` | Dựng tường đặc giữa người chơi và đích. Đạn bị chặn. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/handlers.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
