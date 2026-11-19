# 015 · Khiên hấp thụ cá nhân

Cấp khiên tạm thời cho người cast. Thời hạn cấu hình 100 tick, khoảng 5 giây ở 20 TPS; cooldown 8 giây riêng cho mỗi caster. Bài chọn `potion` để dùng hiệu lực và vòng đời sẵn có của Minecraft. Bài thử giả định người tham gia không có Absorption sẵn, không mặc giáp và có đủ máu trước khi đo. Không cần biến để tự đếm tim, xử lý event sát thương hoặc timer dọn. `level=0` là cấp hiệu ứng I theo wiki. [Potion](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/potion) · [Cooldown](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cooldown)

Đã tra [quy tắc đơn giản](../../../memory/preferences/simple-full-gameplay.json), [quyết định về guard](../../../memory/decisions/require-evidence-for-defensive-logic.json) và [mẫu hỗ trợ](../../../knowledge/player-skills/combat/README.md). Các thông số thời gian thuộc ca thử. Không có quyết định mới về gameplay cá nhân.

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server. Dùng MythicMobs core với mốc đối chiếu 5.14.0, không khai báo addon. Dùng tài khoản Survival có quyền chạy test. Player chạy lệnh là caster. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [Ví dụ player làm caster](https://wiki.mythiccraft.io/mythicseasons/examples/Common-Examples)

```text
/mm reload
/mm test cast TrainingPersonalGuard
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `caster-only` | A cast khi đứng gần B. Chỉ A có biểu tượng và tim hấp thụ. |
| `damage` | A cast rồi nhận một đòn nhẹ dưới lượng hấp thụ. Tim hấp thụ giảm trước, máu thường giữ nguyên. Làm lại đòn đó sau khi hiệu lực hết để đối chứng và tránh đánh liên tiếp trong miễn damage. |
| `expiration` | Cast trên sàn yên, không nhận hit. Tim vàng mất khi hết khoảng 100 tick. |
| `cooldown` | A cast lại ở khoảng giây 6, sau khi khiên đã hết. B cast ngay sau đó. Kỳ vọng A chưa nhận khiên, B nhận. A cast lại sau hơn 8 giây tính từ lần đầu và nhận khiên. |

**Trạng thái.** Chờ log nạp và gameplay. Lưu build, kết quả quan sát và xác nhận vào [hồ sơ ca](case.json) và [nhật ký](../../../feedback/training/README.md).
