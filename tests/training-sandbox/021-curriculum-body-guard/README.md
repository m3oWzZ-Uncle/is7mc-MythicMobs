# Bài 04 · Hộ Thể

Player tự cấp **Absorption I** trong 100 tick, khoảng 5 giây ở 20 TPS. Cooldown là 8 giây theo từng người cast. Giữ nguyên cơ chế của [bài khiên cá nhân 015](../015-personal-guard/README.md) với ID mới `TrainingHoThe` để theo dõi chương trình riêng. Hai thông số thời gian là mặc định của bài, dùng MythicMobs core 5.14.0 làm mốc đối chiếu. [Đề Foundation](../../../training/levels/foundation.md#04--hộ-thể)

`potion` dùng cơ chế hấp thụ và hết hạn có sẵn. `level=0` là Absorption I. `@self` nhận đúng player caster. Bài không cần lưu lượng khiên bằng biến hoặc tự chặn sự kiện damage. Cấu hình dùng trong ca thử mà người chơi chưa có Absorption từ nguồn khác. [Wiki Potion](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/potion) · [Cooldown](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cooldown) · [Quy tắc thiết kế đơn giản](../../../memory/decisions/require-evidence-for-defensive-logic.json)

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server. Dùng hai người chơi Survival. Bỏ giáp và hiệu ứng thay đổi sát thương hoặc hồi máu để dễ đối chiếu tim vàng với tim thường. Dùng cùng một đòn nhẹ ở lượt có và không có khiên. Đợi qua cooldown giữa các ca độc lập.

```text
/mm reload
/mm test cast TrainingHoThe
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `caster-only` | A cast cạnh B. Chỉ A có tim vàng và hiệu ứng. |
| `absorbs-damage` | A nhận một hit nhẹ khi khiên còn. Tim vàng giảm trước, máu thường giữ nguyên nếu khiên đủ. So lại với cùng đòn khi không có khiên. |
| `early-depletion` | A cast và nhận lượng damage đủ dùng hết khiên trước 5 giây. Đòn kế tiếp qua khoảng miễn sát thương trừ máu thường. Khiên không tự đầy lại trong cùng lượt. |
| `natural-expiry` | A cast và đứng yên, không nhận hit. Tim vàng biến mất khi hết thời lượng. |
| `independent-cooldown` | A thử cast lại sau khi khiên hết nhưng trước 8 giây từ lần đầu. B cast trong cùng khoảng đó. A chưa nhận khiên mới, B có khiên. A cast lại sau hơn 8 giây. |

Ghi build, log nạp và kết quả từng ca vào [hồ sơ bài](case.json). Bản r1 đang chờ thử gameplay. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)

**Phản hồi thiết kế.** Biến thể Hộ Thể giảm sát thương suốt cửa sổ bảo vệ được ghi riêng theo hệ stat của server. Các ca ở trên áp dụng cho đề khiên hấp thụ ban đầu. [Quyết định và ca đối chiếu](../../../feedback/decisions/MM-D-2026-004.md)
