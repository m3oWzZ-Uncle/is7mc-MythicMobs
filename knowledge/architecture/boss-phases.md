# Boss phases

Mốc đọc **MythicMobs 5.14.0**. Phần kiến trúc dưới đây là mẫu thiết kế dựa trên các cơ chế đã đối chiếu. Trạng thái triển khai của mẫu là `unverified`. [Nguồn và phiên bản](../../docs/wiki/README.md)

## Chọn cơ chế theo luật của trận

| Yêu cầu gameplay | Thiết kế phù hợp | Việc cần kiểm chứng |
| --- | --- | --- |
| Thay tập skill theo HP hiện tại và cho phép trở lại khi hồi | Dùng các khoảng HP để điều kiện hóa skill. Dùng `HealthPercent` trong ngữ cảnh caster khi xét HP boss. | Kiểm tra ở ngay ngưỡng, hồi máu qua ngưỡng, khoảng chồng lấn và trường hợp không có khoảng nào hợp lệ. [HealthPercent](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HealthPercent) |
| Chạy một hành động đơn giản dưới ngưỡng đúng một lần | Wiki ghi health modifier `=90%` chạy tối đa một lần khi dưới 90%. Đặt trên dòng mob có trigger đã chọn. | Thử thứ tự cập nhật HP trong trigger, hit vượt ngưỡng, hồi máu và reset cùng mob. Changelog 5.10.0 có sửa parser health conditional trên trigger. [Health Modifiers](https://wiki.mythiccraft.io/mythicmobs/Skills/Skills#health-modifiers), [Changelog 5.10.0 mục Conditions](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd) |
| Một phase giữ nguyên sau khi chuyển và có side effect như summon hoặc đổi bộ skill | Mẫu thiết kế dùng biến `CASTER` cho phase, điều kiện kiểm tra phase hiện tại và ngưỡng HP, rồi ghi phase mới trước thao tác có delay. | Thử hai người dồn damage cùng tick. Chọn trước cách xử lý đòn vượt nhiều ngưỡng và cách phục hồi nếu chuyển phase bị ngắt giữa chừng. [Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables), [VariableEquals](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableequals), [SetVariable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable) |

Ví dụ luật thiết kế cho boss ba phase. Boss bắt đầu ở P1, có ngưỡng 70% và 30%. Nếu P2 bắt buộc có một đoạn chuyển cảnh, hit từ 75% xuống 25% vẫn đưa boss qua P2 và chỉ xét P3 sau khi P2 đã hoàn tất phần bắt buộc. Nếu trận cho phép bỏ qua P2, đường P1 → P3 cần chỉ rõ cleanup và hiệu ứng nào của P2 được bỏ qua. Ghi lựa chọn trong hồ sơ trước khi viết YAML. Các tên P1/P2/P3 là trạng thái của ví dụ thiết kế.

## Lập hồ sơ vòng đời

1. Ghi trạng thái ban đầu, các phase hợp lệ, đường chuyển và trigger. `~onDamaged` gắn với sự kiện nhận damage. Nếu dùng nó để kiểm tra ngưỡng, đo HP được đọc trước hay sau hit trên build thật. Nếu dùng `~onTimer`, xét sai số giữa hai lượt kiểm tra và lưu ý timer dùng đồng hồ chung. [On Damaged](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onDamaged), [On Timer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer)
2. Với từng phase, ghi tập skill được phép, đối tượng nhận cảnh báo, mục tiêu tại lúc đánh, độ trễ, hitbox, damage, cooldown và luật khi đang cast mà chuyển phase. Nếu dùng ModelEngine, đối chiếu mốc animation chạm đòn với thời điểm thực thi damage. [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078), [ModelEngine State](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State)
3. Ghi các đường kết thúc trận. Wiki liệt kê `~onDeath`, `~onDespawn` và `~onDropCombat`, trong đó `~onDropCombat` cần threat tables. Thử đường phù hợp với arena thực tế, kể cả khi mất mục tiêu, người cuối rời arena hoặc dungeon reset. Ghi ai thu dọn add, aura, projectile, animation, cờ bận và boss bar tùy chỉnh. [Triggers](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers), [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura), [BossBar](https://wiki.mythiccraft.io/mythicmobs/Mobs/BossBar)

## Ma trận thử trên server

| Kịch bản | Bằng chứng cần ghi |
| --- | --- |
| HP ngay trên, đúng bằng và dưới từng ngưỡng | HP trước/sau, phase trước/sau, thời điểm và số lần chuyển |
| Một hit vượt hai ngưỡng, hoặc hai người đánh cùng tick | Thứ tự chuyển phase, số lần gọi skill, summon hoặc thay đổi UI |
| Boss hồi máu qua ngưỡng | Luật phase tiến/lùi và tập skill sau hồi máu |
| Mất target hoặc đổi target giữa telegraph và hit | Người thấy telegraph, mục tiêu thực nhận hit, cooldown được áp dụng |
| Chết, despawn hoặc reset giữa chuỗi có delay | Cast còn chạy hay dừng, add/aura/model còn sót, phase và cooldown khi kéo lại |
| Hai boss cùng loại đồng thời | Mỗi boss giữ đúng phase và cleanup chỉ tác động trận tương ứng |

Lưu kết quả theo [quy trình thử nghiệm](../../tests/README.md) và [hồ sơ boss](../../examples/bosses/README.md).
