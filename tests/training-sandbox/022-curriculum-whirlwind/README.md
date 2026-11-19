# Bài 05 · Toàn Phong Trảm

Player báo trước rồi chém một vòng quanh mình. Bản r1 biểu diễn vòng xoay bằng cú vung tay và vệt chém 360°; skill không xoay camera hoặc đẩy người chơi. Đây là ca PvE trên arena phẳng. Mốc đối chiếu là MythicMobs core **5.14.0**, không khai báo addon. [Đề Foundation](../../../training/levels/foundation.md#05--toàn-phong-trảm)

## Thiết kế

- Khi cast, vòng lửa bán kính 3 block báo vùng. Sau **12 tick**, người chơi vung tay, hiện vòng chém và quét một lần để gây **6 điểm sát thương cấu hình**. Hiệu ứng chạy cả khi vùng trống vì đặt trước dòng chọn mục tiêu. Cooldown theo caster là **4 giây**. [ParticleRing](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/ParticleRing) · [Delay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/delay) · [PlayAnimation](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/PlayAnimation) · [Cooldown](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cooldown)
- Tâm damage là vị trí caster khi chém. Hitbox là vùng cầu bán kính 3 block giới hạn thêm độ lệch Y từ −1 đến +1 block. Vòng particle thể hiện biên ngang trên sàn phẳng. Lọc player và armor stand. Giữ người cast tại chỗ khi so vòng báo với vùng chém. Nếu caster tự đi trong lúc chờ, vòng chém và damage đi theo vị trí mới; vòng cảnh báo lúc bắt đầu là ảnh chụp vị trí cast. [EntitiesInRadius](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesInRadius) · [YDiff](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/ydiff) · [Inline Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Inline-Conditions)
- Chọn một truy vấn vùng thay vì gây damage theo từng điểm VFX. Tái sử dụng cách đặt animation và damage cùng mốc từ [pattern đồng bộ](../../../knowledge/patterns/dong-bo-animation-damage.md). Yêu cầu vẫn ra đòn khi hụt đến từ đề Bài 05; [phản hồi Dash Cleave](../../../feedback/corrections/MM-2026-006.md) là ca đối chiếu thiết kế. Bài dùng 24 điểm báo và 16 điểm chém, một hạt mỗi điểm, không có timer nền.

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server và thử bằng player Survival. Dùng mob đứng yên cùng loại, cùng cao độ và đủ máu. Chọn arena mở để cô lập bán kính và cao độ. Dùng camera ngôi ba và ghi máu trước/sau, cách các lần cast hơn 4 giây trừ khi đang kiểm hồi chiêu.

```text
/mm reload
/mm test cast TrainingToanPhongTram
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `warning-then-hit` | Đặt mob cách caster 2 block. Ghi hình từ lúc cast. Vòng báo hiện trước, mob chỉ mất máu khi hiện vòng chém sau 12 tick. |
| `four-directions` | Đặt bốn mob cùng tầng ở bốn hướng cách 2 block. Mỗi mob nhận đúng một lượt damage trong cùng một lần cast. |
| `radius-and-height` | So mob ở trong biên và ngoài biên trên sàn phẳng. Thêm mob trên bục cao 2 block và trong hố sâu 2 block, lệch ngang khoảng 1 block để vẫn trong bán kính 3 theo hình học. Hai mob lệch tầng giữ nguyên máu. |
| `enter-and-exit` | Lượt thứ nhất cho mob đi vào vùng trong thời gian báo và còn trong vùng lúc chém. Lượt thứ hai cho mob rời vùng trước cú chém. Chỉ lượt thứ nhất gây damage. |
| `empty-swing` | Cast khi vùng trống. Vẫn hiện vòng báo, vung tay và vòng chém. |
| `multiplayer-cooldown` | A và B đứng ở hai làn riêng rồi cast gần đồng thời. A thử lại ngay. Cả hai cast được lượt đầu theo tâm riêng, không gây damage lên nhau. A chưa thể chém lượt hai khi chưa hồi. |

Bản r1 đang chờ log nạp và thử gameplay. Ghi build, kết quả từng ca và xác nhận vào [hồ sơ bài](case.json). [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)

Người dùng đánh giá thiết kế r1 phù hợp với skill không model. Kinh nghiệm về biến thể có model báo hiệu và chém 180° được lưu riêng. [Quyết định và ca đối chiếu](../../../feedback/decisions/MM-D-2026-005.md)
