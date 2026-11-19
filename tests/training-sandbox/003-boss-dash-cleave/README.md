# Bài #2 · Lướt chém nhiều mục tiêu

Boss Husk nhận nhấp phải để thử đòn. Người nhấp là mục tiêu cú lướt. Khi kết thúc lướt, boss vung tay kể cả khi không còn ai trong vùng chém. Đối chiếu MythicMobs core 5.14.0, không cần addon. [Phản hồi và lịch sử bản sửa](../../../feedback/corrections/MM-2026-006.md)

## Luồng thực thi

| Mốc | YAML và mục đích |
| --- | --- |
| Tick 0 | Hạt lửa trên boss báo trước. Cooldown 4 giây tránh hai người nhấp tạo hai lượt lướt cùng lúc. |
| Tick 12 | `look{force=true} @trigger` quay boss về người đã nhấp. `lunge @trigger` dùng vị trí người đó lúc bắt đầu lướt. `velocityY=0` đặt thành phần dọc của cú lướt về 0. |
| Tick 18 | `velocity` đặt vận tốc về 0. `playanimation{a=0} @self` cho boss vung tay chính ngay cả khi chém hụt. |
| Tick 18, sau vung tay | `@LivingInCone{a=90;r=4;usepitch=false}` chọn mục tiêu từ vị trí và hướng boss lúc chém. Metaskill damage lọc người chơi và đường nhìn, rồi gây 6 điểm sát thương cấu hình. |

**FACT · tài liệu.** `@Forward{f=5}` chọn một điểm trước caster. `~onInteract` gắn người nhấp vào `@trigger`. `@target` là mục tiêu chiến đấu hiện tại và boss thử đã bỏ AI chọn mục tiêu. Danh mục Mechanics mô tả `lunge` đưa caster về phía mục tiêu. `velocity` thao tác vectơ của entity đích, gồm cả đặt ba trục về 0. [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [onInteract](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onInteract) · [Mechanics](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics) · [Velocity](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/velocity)

**PREFERENCE · phản hồi đã xác nhận.** Người dùng cho biết `lunge` cho kết quả lướt tốt hơn `velocity` trong bài này. Người dùng yêu cầu boss vẫn chém khi người chơi né. Phản hồi không kèm build, số liệu so sánh hoặc log. [Hồ sơ gốc](../../../feedback/corrections/MM-2026-006.md)

**INFERENCE · cần thử.** Cú lướt dự kiến lấy hướng theo vị trí người nhấp tại tick 12, rồi di chuyển theo quán tính tới tick 18. Mốc 12/6 tick và lực 0,85 là thông số thử trên sàn phẳng trong tầm nhấp phải. Cần đo quãng lướt, hướng thân sau `look`, và kiểm tra cone khi mục tiêu né. Arm swing là animation vanilla của Husk. [Look](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/look) · [PlayAnimation](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/PlayAnimation) · [LivingInCone](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/LivingInCone)

## Thử trong Minecraft

Chép [mob](Mobs/boss-dash-cleave.yml) và [skill](Skills/boss-dash-cleave.yml) vào `Mobs/` và `Skills/` trên bản sao server. Dùng sàn phẳng, người chơi Survival không giáp và khu vực cho phép mob gây damage. Dùng tài khoản thứ hai để đo hit nhiều người. Quay từ bên cạnh để so mốc hạt, chuyển động, vung tay và mất máu.

```text
/mm reload
/mm mobs list
/mm mobs spawn TrainingDashCleaveBoss
```

| Ca | Thao tác và kết quả kỳ vọng |
| --- | --- |
| `dash-to-trigger` | A nhấp từ bên hông hoặc phía sau boss ở khoảng cách 2–3 block, B đứng phía trước hướng ban đầu. Boss quay và lướt về phía A. Đo quãng thực tế. |
| `no-early-damage` | Đứng trong đường lướt hoặc vùng chém và quay clip. Máu giữ nguyên khi cảnh báo và khi lướt, chỉ tụt lúc chém nếu đứng trong vùng. |
| `multi-target-cone` | Đặt A và B trong cone tại điểm dừng thực tế, một người thứ ba ngoài cone nếu có. A và B nhận một hit mỗi người, người ngoài giữ nguyên máu. |
| `dodge-during-windup` | A đổi sang bên khác trước khi boss lướt. Kiểm tra boss nhắm vị trí mới của A ở mốc bắt đầu lướt. |
| `dodge-during-dash` | A nhấp rồi né ngang khi boss đã bắt đầu di chuyển. Không còn ai trong cone lúc chém. Boss vẫn dừng và vung tay, cả hai người giữ nguyên máu. |
| `blocked-dash` | A kích hoạt từ phía boss nhìn thấy, B đứng trong tầm nhưng sau tường. Có thể dựng tường chắn đường sau khi bắt đầu cảnh báo trong ca riêng. Kiểm tra boss dừng theo va chạm và B không bị chém xuyên tường. |
| `recovery-and-cooldown` | Nhấp liên tục từ hai người khi cast. Sau một lượt chém hụt, đợi hơn 4 giây tính từ cảnh báo rồi dùng lại cùng boss. Mỗi lượt hợp lệ có đúng một lần lướt và vung tay. |
| `interrupted-cast` | Dọn boss giữa cảnh báo hoặc giữa lướt. Quan sát có hit muộn không. Ghi bằng chứng nếu xảy ra để quyết định guard phù hợp với build. |

Dọn bằng `/mm mobs kill TrainingDashCleaveBoss`. Giữ log reload, phiên bản server/MythicMobs và kết quả từng ca trong [hồ sơ bài](case.json). Bản rút gọn đang chờ kiểm thử Minecraft. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
