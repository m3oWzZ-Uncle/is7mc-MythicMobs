# Skill đơn giản

## Mob tương tác và metaskill hai bước

Ví dụ thực hành được viết dựa trên wiki MythicCraft, mốc đọc **MythicMobs 5.14.0** ngày 13/11/2026. Trạng thái `syntax-checked`. `tests/check_yaml.py` với PyYAML 6.0.3 đọc thành công cả hai file. Kiểm tra tĩnh xác nhận `TrainingGreeter` gọi đúng ID `TrainingGreeting`. Bước tiếp theo là nạp và chạy kịch bản trên server thử. [Nguồn và phiên bản](../../docs/wiki/README.md), [các mức bằng chứng](../../tests/README.md)

- [Mobs/TrainingGreeter.yml](Mobs/TrainingGreeter.yml) khai báo mob và gọi skill từ `~onInteract`. `@trigger` chọn người chơi đã tương tác. [On Interact](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onInteract), [Skill](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill)
- [Skills/TrainingGreeting.yml](Skills/TrainingGreeting.yml) lọc target kế thừa bằng `isPlayer`, gửi hai dòng chat cách nhau 20 tick, với `Cooldown: 5` giây theo caster. [IsPlayer](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/isplayer), [Message](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/message), [Delay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/delay), [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078)

### Kịch bản thử

1. Sao chép hai file vào `Mobs` và `Skills` tương ứng của MythicMobs trên server thử. Dùng `/mm reload`, xem log và chạy `/mm mobs spawn TrainingGreeter`. [Essential Commands](https://wiki.mythiccraft.io/mythicmobs/Guides/%28Step-4%29-Essential-Commands)
2. A click phải vào mob, B đứng cạnh và không click. Kỳ vọng A nhận `Da nhan tuong tac.` rồi `Da qua 20 tick.`, B không nhận hai tin. Đây là hành vi suy ra từ cấu hình.
3. Trong vòng 5 giây từ lần gọi đầu, thử cho A hoặc B click cùng mob. Kỳ vọng mob không bắt đầu chuỗi tin mới. Sau khi hết cooldown, B click và nhận hai tin. Thử thêm mob thứ hai để đối chiếu cooldown riêng theo caster.
4. Ghi build, edition, log nạp và kết quả thực tế vào hồ sơ của lần thử. Xem [bằng chứng cho từng trạng thái](../../tests/README.md).
