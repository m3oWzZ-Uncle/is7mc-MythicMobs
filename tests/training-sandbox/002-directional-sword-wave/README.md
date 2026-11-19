# Bài thực hành #1 · Kiếm khí định hướng

ID lưu trong sandbox là `002-directional-sword-wave`. Ca này bắn một kiếm khí từ người thi triển, theo yaw và pitch lúc cast. Kiếm dự kiến dừng ở người chơi đầu tiên có va chạm hợp lệ hoặc khi gặp tường đặc. Ca thử dùng MythicMobs core **5.14.0** làm mốc đối chiếu, dạng player khác đứng thử trong khu vực cho phép PvP. Chỉ dùng lệnh thử để kích hoạt và dùng hạt `crit` để quan sát. [Bản phát hành MythicMobs](https://hangar.papermc.io/Lumine/MythicMobs/versions/)

## Nguồn và lựa chọn

- Đã tra quyết định về độ phức tạp và những phân tích projectile/hitbox trong memory. Áp dụng kiến trúc đơn giản nhất đáp ứng đường bay, va chạm và damage. Các giá trị tầm, tốc độ và damage dưới đây là giả định của bài. [Quyết định về kiến trúc](../../../memory/preferences/simple-full-gameplay.json) · [Phân tích projectile khứ hồi](../../../memory/patterns/owner-return-projectile.json)
- Mẫu Vạn Kiếm trong Knowledge Base dùng projectile hướng ra trước và có AoE tại điểm chạm. Bài này giữ đường bay và callback va chạm. Skill damage dùng trực tiếp mục tiêu do callback nhận để người đứng ngoài vùng va chạm không bị đưa vào một lượt chọn AoE. Một ray trace tức thời có thể hợp với đòn hitscan, còn bài này yêu cầu thấy kiếm di chuyển qua không gian. [Pattern projectile và va chạm](../../../knowledge/patterns/projectile-va-cham.md)

## Luồng và kiểm tra tĩnh

1. Lệnh `/mm test cast TrainingDirectionalSwordWave` chạy metaskill từ người đang nhìn. `@Forward{f=16;y=1;uel=false;lockpitch=false}` chọn điểm theo hướng nhìn, giữ pitch. `syo=1` ở đầu phóng và `y=1` ở điểm ngắm bù cùng độ cao từ vị trí chân để đường bay dự kiến song song với góc nhìn. `sfo=0` tránh bỏ qua một khoảng phía trước ở lúc phóng. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [Offset chung của location targeter](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#common-location-targeters-attributes)
2. `projectile` dùng `v=12` block/giây, `i=1` tick, `mr=16` block và `d=30` tick. Ở 20 TPS, mỗi bước danh nghĩa là 0,6 block. Tắt ảnh hưởng mob power lên tốc độ và tầm. `ham=true` bật kiểm tra ray trace theo tick và `sB=true` yêu cầu dừng khi va chạm block đặc. Bán kính phát hiện cấu hình là ngang 0,4 block và dọc 0,6 block. Các giá trị đó là tham số của bộ kiểm tra MythicMobs. Ranh giới theo thân người chơi và mép tường cần kiểm trong game. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile)
3. `onTick` chỉ vẽ hạt tại `@origin`. `onHit` truyền entity va chạm cho `TrainingDirectionalSwordWaveHit`, bên trong chỉ có `damage{a=4}` dùng mục tiêu kế thừa. `hp=true`, `hnp=false` và `hitSelf=false` giới hạn bài vào người chơi khác. `sE=true` đặt yêu cầu dừng tại entity hợp lệ đầu tiên. Không có callback damage khi chạm tường hoặc hết tầm. [Projectile · Special Notes](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile#special-notes) · [Particle](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle) · [Damage](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/damage)

Các hành vi riêng của ca, gồm đường bay theo pitch, ranh giới va chạm và số lần damage, là **INFERENCE** từ YAML và tài liệu. Không có biến, điều kiện phụ, animation model, cooldown hay entity VFX cần dọn. Projectile kết thúc theo va chạm hoặc giới hạn tầm/thời gian. Nên thử từng phát và đợi hơn 2 giây giữa các lần bắn để tránh chồng projectile hoặc cửa sổ miễn damage của Minecraft. Chưa đo hiệu năng khi bắn hàng loạt.

## Thử trong Minecraft

Chép [file YAML](Skills/directional-sword-wave.yml) vào thư mục `Skills/` của MythicMobs trên bản sao server. Dùng ít nhất hai người chơi ở Survival, bỏ giáp và hiệu ứng giảm damage, chọn khu vực cho phép player damage. Đây là ca player cast nên không cần spawn mob. Người bắn cần quyền chạy lệnh thử. Ghi phiên bản và edition MythicMobs, Minecraft, build server và log reload; kiểm tra ba ID metaskill qua danh sách hoàn thành lệnh hoặc log đăng ký.

```text
/mm reload
/mm test cast TrainingDirectionalSwordWave
```

Để dựng mốc, chọn một sàn phẳng và đánh dấu tâm block tại điểm bắn. Bắn về phía Nam với yaw 0°, pitch 0°. Dùng camera ngôi thứ ba hoặc clip của người đứng ngoài để theo dõi vệt. Có thể dùng `/data get entity <tên-người-chơi> Health` từ tài khoản có quyền để ghi máu ngay trước và sau từng phát. Dùng cùng điểm bắn và góc nhìn cho các ca thẳng, lệch và có tường.

| Ca | Bố trí | Kỳ vọng |
| --- | --- | --- |
| `direct-hit` | B đứng đúng trục bắn, xa 6 block. Bắn một phát. | B mất máu một lần. Ghi trước/sau và so với 4 điểm damage đặt trong YAML. Người bắn giữ nguyên máu. |
| `side-miss` | Giữ khoảng cách 6 block rồi dịch B sang trái 2 block. Lặp lại bên phải. | Cả hai lần máu B giữ nguyên; vệt hạt vẫn đi qua trục cũ. |
| `solid-wall` | B đứng đúng trục ở 6 block. Đặt một tường đá đặc chắn ngang trục ở 3 block, cao ít nhất 3 block. | Vệt dừng ở tường; B giữ nguyên máu. Bỏ tường và chạy lại `direct-hit` để đối chứng. |
| `first-target` | B và C cùng trục, lần lượt 4 và 7 block trước người bắn. | Chỉ B nhận damage, C giữ nguyên máu. |
| `yaw-change` | B vẫn ở làn phía Nam. Người bắn quay 90° sang một làn trống rồi mới cast. | Vệt đổi theo hướng mới và B giữ nguyên máu. |
| `pitch-change` | Dời B lên bục cao hơn sàn 3 block tại vị trí 6 block phía trước. Bắn ngang, rồi giữ yaw và ngẩng khoảng 27° để thử lại. | Phát ngang đi dưới B. Phát ngẩng chếch lên và chạm vùng thân B. |
| `range-expiry` | Dọn vật cản, đặt B đúng trục ở 18 block. | Vệt kết thúc gần tầm cấu hình, B giữ nguyên máu. |

Nếu cả ca trúng và ca lệch đều giữ nguyên máu, kiểm tra log, đường vệt, quyền cast và bảo vệ PvP trước khi chỉnh bán kính. Nếu người đứng lệch mất máu, ghi khoảng lệch, vị trí vệt và nguồn damage rồi thử lại tại cùng tọa độ để cô lập lỗi.

**Checkpoint.** Chờ log nạp và bằng chứng gameplay. [Hồ sơ kiểm thử](case.json) giữ danh sách ca bắt buộc. Sau khi người dùng xác nhận, lưu bản sửa và ca hồi quy vào [hồ sơ lỗi](../../../feedback/corrections/README.md) nếu phát hiện lỗi. Chỉ lưu quyết định cá nhân vào [memory](../../../memory/README.md#bài-thực-hành-và-phản-hồi) khi người dùng xác nhận lựa chọn gameplay đó.
