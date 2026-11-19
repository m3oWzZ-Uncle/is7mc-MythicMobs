# Cấp 2 · Bài 03 · Hàn Băng Địa Mạch

**Bài 08 thay thế · r1 · Player-cast, PvE.** Một luồng băng chạy theo yaw lúc cast, để lại vệt ICE và các khối băng trồi lên. Chạm tường tạo một vùng đóng băng trang trí. Mob trúng đòn nhận 6 điểm sát thương cấu hình. Mob sống sót sau đòn được stun 80 tick với một lồng băng bám theo. Bản thử chọn trần 6 mob hợp lệ mỗi cast và hồi chiêu 12 giây. Mốc thử là **MythicMobs 5.14.0 Premium**, trên Paper tương thích. VFX dùng block/item hiển thị và particle vanilla. [Đề RPG](../../../training/levels/rpg.md#08--hàn-băng-địa-mạch) · [Phát hành 5.14.0](https://hangar.papermc.io/Lumine/MythicMobs/versions/v5.14.0)

## Đường đi và va chạm

| Phần | Cách triển khai |
| --- | --- |
| Phóng | `@Forward{lockpitch=true}` lấy hướng ngang tại lúc cast. Điểm đầu và điểm ngắm đều nâng 0,25 block. Tầm tối đa 12 block, tốc độ 2 block/giây, hạn 140 tick. `powerAffectsRange=false` và `powerAffectsVelocity=false` giữ thông số khi caller truyền power. |
| Bám bề mặt | `hugSurface=true`, `heightFromSurface=0.25`, `gravity=0`. Dùng một lần thử leo và hai lần thử hạ cho địa hình nhỏ. `interval=2` cho bước ngang dự kiến khoảng 0,2 block ở 20 TPS. `highAccuracyMode=true` giữ ray trace va chạm. |
| Đụng tường | Chỉ `onHitBlock` gọi nhánh tường. Mask ICE hình cầu bán kính 3 tồn tại 100 tick. Vòng bụi R1 hiện ngay, vòng R3 hiện sau 3 tick. Bản r1 dùng bụi cho va chạm tường. |
| Hết tầm hoặc hết hạn | Engine kết thúc projectile chính. Skill không có `onEnd` tạo vùng băng. Nếu chạy tới vực sâu hơn khả năng dò xuống, kiểm riêng cách engine kết thúc. |
| Trúng mob | `stopAtEntity=false` để luồng đi tiếp. `onHit` nhận đúng entity va chạm. `foreach` xử lý mỗi entity riêng và kiểm đường nhìn từ origin để giảm hit xuyên vật cản. Bản thử lọc player, caster và armor stand. |

**Tài liệu và giới hạn.** Wiki mô tả `maxClimbHeight` và `maxDropHeight` theo số lần thử. Cần đo trên server xem engine ưu tiên chỉnh cao độ hay ray trace khi gặp mép bậc, và một lần dừng vì leo thất bại có gọi `onHitBlock` hay không. Thử bậc thấp lẫn tường cao trước khi chốt tương thích. Nếu build xử lý hai trường hợp giống nhau, phương án tiếp theo là kiểm block trước luồng cùng khoảng hở phía trên, gọi nhánh tường và `endprojectile` khi gặp cột kín, rồi thử lại ca vực và bậc. Bản r1 dùng xử lý địa hình sẵn có của engine. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) · [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [Line of Sight From Origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/lineofsightfromorigin) · [End Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/endprojectile)

## Vệt ICE và vòng đời khối băng

- Mỗi callback tick vẽ bụi xanh nhạt tại `@origin`. Cứ 5 callback, nhánh lấy mẫu làm lạnh sàn bằng một lớp `BlockMask` ICE, thêm bụi cyan chuyển xanh biển và phóng một bullet `SMALLBLOCK` bằng PACKED_ICE. Bán kính mask 1 theo X/Z, Y bằng 0, tâm hạ 0,55 block từ origin. Đây là mốc phù hợp để thử sàn block đầy. Kiểm riêng biên slab vì hình khối nhìn thấy có thể khác bề mặt vật lý. [Origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Origin) · [BlockMask](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/blockmask) · [Dust Color Transition](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/Particle/Particle-Types/Dust_Color_Transition)
- Nhánh `Rise` lấy origin hiện tại làm mốc. Nó phóng thẳng lên 0,12 block/giây, bắt đầu thấp hơn 0,22 block và tồn tại tối đa 100 tick. Dịch chuyển dự kiến trong 5 giây là 0,6 block. Projectile phụ có vòng đời riêng, bỏ va chạm với entity và block, và không có callback damage hoặc callback sinh tiếp. [Projectile Bullets](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile#projectile-bullets)
- BlockMask chỉ đổi hình ảnh phía client, tự khôi phục sau 100 tick, kể cả khi luồng chính đã kết thúc. Nó không tạo mặt ICE có độ trượt hoặc va chạm mới. Mask vệt và mask tường được gửi tới người chơi quanh origin trong 32 block. Bản 5.13.0 ghi nhận bản sửa cho hai mask có thời hạn chồng nhau. Vẫn cần thử chồng vệt, và với WorldGuard hoặc plugin bảo vệ thực tế phải kiểm riêng chính sách damage/stun và hình ảnh ở biên vùng. [BlockMask](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/blockmask) · [Audience](https://wiki.mythiccraft.io/mythicmobs/Skills/Audience) · [Changelog](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#5130)

## Damage, stun và hình học lồng

1. Projectile dùng bộ miễn hit native `immuneDelay=20000`. Wiki mô tả đây là khoảng trước lần chạm lại cùng mục tiêu. Giá trị chọn dài hơn cửa sổ bay bình thường. Cần đo một mob ở lại trong vùng hit suốt nhiều tick và hai projectile chạm cùng mob để xác nhận phạm vi và cách engine tính thời gian. Biến `skill.frost_hits` đếm tối đa 6 lần xử lý hợp lệ, kể cả một lần damage sau đó bị hủy. Biến `skill.frost_pulse` chỉ giữ nhịp lấy mẫu. Cả hai sống trong lượt cast, ngừng cùng cây skill và không dùng registry global hay biến của đích. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile) · [ForEach](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ForEach) · [Skill Trees](https://wiki.mythiccraft.io/mythicmobs/Skills/SkillTrees)
2. `damage{then=...}` gọi nhánh đóng băng sau hit. Nhánh này cần đích còn sống để stun và gắn khối. Dùng component `stun` với `stopAI=true` và chống knockback. Aura stun kéo dài 80 tick. Khi một lượt khác đóng băng cùng mob, `mergeAll` và các tên cố định được dùng để làm mới một bộ stun/lồng, tránh tạo thêm một bộ lồng trên cùng mob. Kiểm riêng lúc aura hết hạn, bị gỡ sớm và mob chết. [Changelog 5.14.0 · Damage](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#damage) · [Stun component](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/AuraComponents/Stun) · [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura)
3. Hai tầng khối dùng 4 điểm mỗi vòng, lệch nhau một phần tư vòng. Mô hình kiểm tra là `P(k,h) = C + (r·cos(kπ/2), h, r·sin(kπ/2))`, với `k=0…3` và hai giá trị h. `Orbital` xử lý đường tròn quanh đúng mục tiêu, nên YAML chỉ truyền bán kính, độ cao và chỉ số điểm. Hai tầng có tên riêng, dùng chung tag `FGS_CAGE`. Khi aura stun kết thúc, `removeTaggedAuras` gỡ tối đa 8 dấu trên đúng entity. Mỗi orbital cũng có hạn 80 tick và quy tắc kết thúc khi đích chết của aura. [Orbital](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital) · [Changelog · removeTaggedAuras](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#new-removetaggedauras) · [KB hình học](../../../knowledge/advanced-math/geometry.md)

| Hình thể | Ví dụ | Bán kính | Cao độ hai tầng so với chân mob |
| --- | --- | --- | --- |
| Nhỏ | Gà, thỏ, silverfish, endermite, mèo | 0,57 | 0,18 và 0,62 |
| Thường | Zombie, bò và các đích mặc định | 0,86 | 0,34 và 1,35 |
| Lớn/cao | Enderman, iron golem, ravager, ngựa | 1,25 | 0,55 và 2,30 |

Ba preset là ước lượng theo loại, dùng được để bắt đầu so hình thể. Mob custom, mob con và mob đổi scale cần preset riêng nếu lồng bị chật. Các dấu dùng projectile bullet DISPLAY với vật liệu ICE/PACKED_ICE. Cần kiểm `startingpoint`, `rotate=false` và độ cao hiển thị trên build thực tế. Các điểm có thể xoay cùng nhau nếu build xử lý cờ rotate theo hướng bullet thay vì dừng chuyển động vòng. Điều cần giữ là đủ bốn góc mỗi tầng và giữ tâm ở đích.

IonTech được dùng làm tham chiếu cho việc tách tâm, điểm mẫu và nhánh VFX. Module stun của IonTech có orbital nhưng dùng Slowness trong tick; bài này dùng stun component. Cách lưu danh sách UUID chỉ đáng thêm nếu ca thử chứng minh hit native lặp trong một lượt cast. [Phân tích IonTech](../../../knowledge/modular-design/slash-projectile.md) · [Module stun nguồn](../../../incoming/Iontech/IonTech-s-Modular-Systems-main/packs/IonTech%27s%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/stun-mechanic.yml)

## Ngân sách ước tính

Ở 20 TPS trên sàn phẳng, luồng đi 12 block mất khoảng 6 giây. Một đợt có tối đa **15 mẫu vệt** theo hạn 140 tick và nhịp 10 tick, tính cả sai lệch ở mốc đầu/cuối. Với vòng đời 100 tick, tối đa **11 bullet vệt cùng lúc** tính cả tick giao nhau. Lồng có tối đa **6 × 8 = 48 khối** mỗi cast. Tổng trần dự kiến là **59 khối VFX đang sống cho mỗi cast**. Với N cast đang chồng nhau, trần là 59N. Đây là trần cấu hình, chưa phải số đo server. Nếu TPS thấp hoặc caller bỏ qua cooldown, tính N theo số cast còn hiệu ứng. Cần đo riêng luồng quét đông mob, mask tường và chi phí packet khi nhiều người xem. Bullet dùng audience `tracked` và particle đặt view distance 32.

## Thử trong Minecraft

Chép [YAML](Skills/frost-ground-surge.yml) vào `Skills/` của server thử. Cast bằng player Survival có quyền test, bật Particles All, đợi hết cooldown giữa các lượt của cùng người. Chuẩn bị sàn dài 17 block có mốc 0, 4, 8 và 12, một bậc lên/xuống, một vực và một tường đặc cao ít nhất 3 block. Dùng mobs đứng yên để đếm hit. Dùng một mob có AI đang di chuyển trong ca stun.

```text
/mm reload
/mm test cast TrainingFrostGroundSurge
/summon minecraft:cow ~ ~ ~ {NoAI:1b,Tags:["training_fgs"]}
/data get entity @e[type=minecraft:cow,tag=training_fgs,sort=nearest,limit=1] Health
```

| Ca | Kiểm tra |
| --- | --- |
| `flat-speed-range-pitch` | Cast nhìn ngang, nhìn lên và nhìn sát chân với cùng yaw. Đo từ lúc phóng đến mốc 4/8/12 block, khoảng 2/4/6 giây ở 20 TPS. Cả ba đường đi bám mặt sàn. Quay camera sau cast để kiểm hướng không đổi. |
| `small-terrain-and-drop` | So slab, bậc +1, bậc −1, bậc −2 và vực sâu hơn. Ghi điểm projectile đổi cao độ hoặc dừng. Vệt/mảnh băng phải xuất hiện sát đúng địa hình mà luồng đi qua. Ghi nếu bậc hợp lệ bị nhận là tường hoặc vực tạo hiệu ứng tường. |
| `wall-only-vs-expiry` | Đặt tường đặc ở mốc 5 và một mob ngay sau tường. Luồng dừng trước hoặc tại mặt chạm. Chỉ một vùng mask bán kính 3 và hai vòng bụi phát ra. Mob sau tường giữ máu. Lặp trên đường trống hết tầm và kiểm không xuất hiện vùng mask lớn. |
| `pierce-and-dedup` | Đặt 3 bò dọc đường và một con lệch rõ ra ngoài. Ba con trong luồng mất máu mỗi con một lần. Bò lệch, người chơi và armor stand không bị đánh. Lặp với một mob chạy cùng hướng hoặc giữ nhiều tick trong vùng hit. |
| `stun-and-cage-size` | Quan sát một mob có AI và đủ máu sống qua hit. Đo thời gian nó ngừng di chuyển rồi hoạt động lại, dự kiến 80 tick. So gà, zombie và iron golem đủ máu. Đếm hai tầng, bốn góc mỗi tầng, và kiểm lồng bám đúng mob. Dùng đích có thêm máu cho gà trong ca này. |
| `thaw-and-death` | Đo một lần hết 80 tick, một lần hạ mob giữa stun và một lần gỡ aura tên `TrainingFrostGroundSurgeStun` bằng `auraremove` lên đúng đích. Kiểm AI và các dấu băng được dọn tương ứng. |
| `mask-restoration` | Quay hình hai vệt cắt nhau. Mask mới nhất phải tồn tại theo hạn riêng. So block thật trước/sau bằng `/execute if block` và thử đi qua để xác nhận va chạm theo block thật. Kiểm thêm ở biên vùng bảo vệ trên bản sao server. |
| `concurrency-and-budget` | A và B cast cùng tick ở hai làn rồi thử chạm cùng một mob. Theo dõi nhịp gần 0,5 giây, một bộ lồng mỗi đích và thời gian dọn. Lặp với >6 mob hợp lệ trong một cast để kiểm cap và việc luồng vẫn tới tường/hết tầm. Dùng video hoặc bộ đếm hiện có của server để đo số đối tượng hiển thị. |

Ghi build, edition, log nạp, kết quả từng ca và xác nhận vào [hồ sơ](case.json). Static check chỉ kiểm tra cấu trúc và ID. Hành vi terrain, phát callback tường, dedup, vòng đời aura và BlockMask chưa xác minh trên server. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [AuraRemove](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/auraremove)
