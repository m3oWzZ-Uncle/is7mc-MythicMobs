# Bài 03 · Hỏa Cầu Thuật

Player phóng cầu lửa theo hướng nhìn. Cầu nổ khi chạm mob hoặc tường đặc. Vụ nổ tác động một lần lên các mob trong bán kính 2 block có đường nhìn từ tâm nổ. Khi bay hết tầm mà không va chạm, vệt lửa tắt. Thiết lập thử là PvE trên sàn phẳng với MythicMobs core 5.14.0 làm mốc đối chiếu, không khai báo addon. Tầm 12 block, damage cấu hình 6 và cooldown 3 giây là thông số của bài. [Đề Foundation](../../../training/levels/foundation.md#03--hỏa-cầu-thuật)

## Thiết kế

- Tái sử dụng cách nhắm theo `@Forward` và vẽ vệt tại `@origin` từ [Kiếm Khí Trảm r1](../../../knowledge/player-skills/projectiles/kiem-khi-tram.md). Hai callback `onHit` và `onHitBlock` dùng chung một metaskill impact, theo mẫu [va chạm và AoE](../../../knowledge/patterns/projectile-va-cham.md). Vệt bay không gây damage. Hết tầm không gọi impact vì không có callback `onEnd`. [Wiki Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile)
- Impact vẽ một hạt `explosion` tại origin. Damage chọn mob riêng qua `@EntitiesNearOrigin{r=2}`, lọc người chơi, armor stand và kiểm đường nhìn từ **tâm nổ**. Dùng cùng điểm cho VFX và truy vấn AoE. Hiệu ứng là particle nên cấu hình không có thao tác phá hoặc đốt block. [EntitiesNearOrigin](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/EntitiesNearOrigin) · [Inline Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Inline-Conditions) · [Line of sight from origin](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/lineofsightfromorigin) · [Explosion particle](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/Particle/Particle-Types/Explosion)
- Cần đo nơi engine đặt origin ở callback chạm tường và kiểm số lần gọi impact khi mob áp tường. Nếu tường chặn luôn mục tiêu cùng phía, báo vị trí nổ và bố trí ca thử để xác định nguyên nhân trên build thực tế. [Quy tắc chỉ thêm bảo vệ khi có lý do](../../../memory/decisions/require-evidence-for-defensive-logic.json)

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server. Dùng người chơi Survival và các mob thử cùng loại đứng yên, còn đủ máu. Giữ mỗi lượt cách nhau hơn 3 giây, trừ ca cooldown. Ghi video hoặc máu trước/sau để phân biệt một hit với nhiều hit.

```text
/mm reload
/mm test cast TrainingHoaCauThuat
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `entity-radius` | Đặt mob chính ở 6 block trên trục, một mob lệch ngang khoảng 1 block tính từ điểm va chạm, một mob lệch hơn 2 block. Nổ một lần. Hai mob trong vùng và nhìn thấy tâm nổ mỗi con trúng một lần. Mob ngoài vùng giữ nguyên máu. |
| `block-cover` | Bắn vào giữa tường đá cao 3 block và đủ rộng. Đặt một mob lệch khỏi đường bay ở mặt trước tường và một mob đối diện sau tường, cả hai trong bán kính 2 block tính từ điểm nổ dự kiến. Nổ một lần ở tường. Mob trước tường trúng, mob sau tường giữ nguyên máu. Quan sát vị trí hạt nổ và trạng thái block. |
| `entity-at-wall` | Đặt mob sát mặt trước tường, chụp lại từ bên cạnh. Đếm đúng một hiệu ứng nổ và một lượt sát thương cho mỗi mob hợp lệ. |
| `range-miss` | Bắn trong làn trống dài hơn 12 block. Đặt mob lệch đường bay khoảng 1,5 block ngang dấu hết tầm để làm đối chứng. Vệt biến mất, không nổ và mob giữ nguyên máu. |
| `player-and-cooldown` | Cho B cắt ngang trước mob rồi đứng gần điểm nổ. A cast và thử lại ngay. B cast một lần trong cửa sổ hồi của A. B giữ nguyên máu, còn lượt cast của B được tính riêng. |

Người dùng đã thử và chấp nhận bản r1 trong Minecraft. Xác nhận áp dụng cho toàn cấu hình. Hồ sơ còn thiếu build, log nạp và kết quả riêng từng ca. [Xác nhận kèm hash](evidence/user-confirmation-r1.md) · [Bài học thiết kế](../../../knowledge/player-skills/projectiles/hoa-cau-thuat.md)
