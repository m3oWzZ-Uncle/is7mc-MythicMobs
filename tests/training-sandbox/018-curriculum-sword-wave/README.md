# Bài 01 · Kiếm Khí Trảm

Player vung tay và bắn một luồng kiếm thẳng theo yaw/pitch lúc cast. Mốc đối chiếu **MythicMobs 5.14.0 core**, không cần addon. Bài chọn PvE trong arena chỉ có mob thử và người chơi. `hp=false` dành cho ca kiểm tra người chơi cắt ngang; đây chưa phải cấu hình lọc thú nuôi, đồng minh hay entity trang trí cho server thật. [Đề Foundation](../../../training/levels/foundation.md)

## Chọn cách làm

Projectile cần thời gian bay và va chạm, nên dùng mechanic projectile và callback hit. `onTick` vẽ vệt ở origin hiện tại, `onHit` dùng đúng đối tượng va chạm đã kế thừa. Player là caster của lệnh thử. Đầu phóng và điểm ngắm cùng cộng độ cao 1 block để hướng bay dự kiến song song hướng nhìn. Vung tay chạy trước khi phóng, kể cả khi phát trượt. Cooldown theo caster, tầm 16 block và damage cấu hình 4 là thông số của bài. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) · [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [PlayAnimation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayAnimation) · [Cooldown](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cooldown)

Đã dùng hình học và callback từ [bài kiếm khí tham khảo](../002-directional-sword-wave/README.md) và [Knowledge Base projectile](../../../knowledge/player-skills/projectiles/README.md). Bài tham khảo chưa có log gameplay. [Quyết định về guard](../../../memory/decisions/require-evidence-for-defensive-logic.json) áp dụng khi chọn ba metaskill cố định và bỏ lớp khóa cast riêng.

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server. Caster ở Survival, cầm kiếm để thấy cú vung. Dùng sàn phẳng và các Husk hoặc mob thử giống nhau, đứng yên, cách người bắn ít nhất vài block và không có hiệu ứng thay đổi damage. Nếu có thể, dùng camera thứ ba ghi lúc vung tay, vệt và thời điểm mất máu. Ghi build, edition, log nạp và kết quả theo [case.json](case.json).

```text
/mm reload
/mm test cast TrainingKiemKhiTram
```

[Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [Ví dụ player caster](https://wiki.mythiccraft.io/mythicseasons/examples/Common-Examples)

| Ca | Thao tác và kết quả kỳ vọng |
| --- | --- |
| `first-mob` | Hai mob cùng trục ở 6 và 9 block. Kiếm bay rồi chỉ đích trước mất máu một lần. Không có hit ở thời điểm vung tay. |
| `off-axis` | Đặt mob ở 6 block, lệch 2 block qua trái rồi qua phải. Mob giữ nguyên máu dù player vẫn vung tay. |
| `wall` | Đặt tường đá cao ít nhất 3 block ở giữa, mob ngay sau tường trên trục. Vệt dừng, mob giữ nguyên máu. Bỏ tường và thử lại để đối chứng. |
| `range` | Đặt mob cùng trục ở 18 block. Skill kết thúc trước khi tới mob. |
| `direction` | Bắn về phía một mob trên bục cao, sau đó quay ngang khi đạn đã bay. Kiếm giữ hướng ban đầu, ghi hướng và mốc hit. |
| `player-and-cooldown` | B đi ngang qua làn trước mob. A bắn như ca đầu, rồi thử cast lại ngay. B thử cast trên làn khác trong khi A hồi. B không nhận damage; A bị cooldown, B vẫn bắn được. |

**Trạng thái.** Người dùng đã thử trong Minecraft và chấp nhận bản r1. Xác nhận áp dụng cho cấu hình tổng thể. Hồ sơ chưa có build thực tế, log nạp hoặc báo cáo riêng cho sáu ca. [Bằng chứng xác nhận](evidence/user-confirmation-r1.md) · [Bài học thiết kế](../../../knowledge/player-skills/projectiles/kiem-khi-tram.md)
