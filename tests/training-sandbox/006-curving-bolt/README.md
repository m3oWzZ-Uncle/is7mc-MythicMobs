# 006 · Đạn đổi hướng

Mỗi lần tick callback quay hướng hiện tại thêm 12°. Độ cong thực tế còn phụ thuộc bước cập nhật và engine. Đạn thử chỉ có VFX.

**Mức kiểm tra:** cấu hình thử độc lập cho player caster, mốc MythicMobs 5.14.0, không yêu cầu cài IonTech. Chép [YAML](Skills/player-skill.yml) vào `Skills/` của bản sao server, chạy `/mm reload`. Người chơi Survival có quyền test gõ `/mm test cast TrainingCurvingBolt`. Dùng khu thử phẳng, có khoảng trống, không giáp hoặc hiệu ứng giảm damage nếu đo máu. Chuẩn bị mục tiêu theo từng ca.

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `curve` | Cast ở sàn rộng, ghi vệt để thấy đạn đổi hướng sau từng bước. |
| `wall` | Bắn vào tường đặc đặt trong đoạn đầu, vệt kết thúc tại tường. |

Lưu kết quả, build, edition và log nạp vào [hồ sơ ca](case.json). Gameplay đang chờ xác minh. [Phân tích nguồn IonTech](../../../knowledge/modular-design/slash-projectile.md) · [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
