# Orbital · hiệu ứng hoặc vùng chạm đi theo entity

**Chức năng và cú pháp.** `orbital{...} @targeter` tạo quỹ đạo quanh entity được chọn. Nó kế thừa thuộc tính aura và có thể dùng projectile bullet, ví dụ `bulletType=MOB`. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/orbital), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/orbital.md)

**Thuộc tính.** `radius` (`r`, 4) đặt bán kính, `points` (`p`, 32) đặt số điểm, `offsety` (`oy`, 0) dịch theo trục Y. `rotate` mặc định true. `onHit` nhận mục tiêu chạm, `castAsOrbital` mặc định false. Wiki liệt kê cùng alias `hs` cho `hitSelf` và `hugSurface`. Dùng tên đầy đủ khi cần phân biệt. Thuộc tính thời lượng và hủy đọc ở [Aura](../entries/mythicmobs--meta-mechanic--aura.md).

**Ví dụ và trường hợp dùng.** Vòng Vạn Kiếm dùng `r=0`, `p=1`, `rotate=false` và mob bullet. Dùng mẫu này khi vị trí VFX bám theo caster còn xoay do animation của model. Với vùng sát thương đứng độc lập, dùng Totem. Với chỉ một particle báo cast, cân nhắc effect đơn giản hơn. [Dòng orbital trong YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L10)

**Lỗi thường gặp.** Dùng `@self` trong callback khi muốn tâm của bullet. Kiểm tra `@origin`, hit radius, quyền sở hữu và dọn orbital theo tên aura khi cast ngắt. Nếu nhiều caster, đo số bullet và callback theo tick. [AuraRemove](../entries/mythicmobs--mechanic--auraremove.md), [Pattern neo caster](../patterns/projectile-neo-caster.md)

**Phiên bản và xác minh.** `Documented`, so sánh snapshot với wiki online ngày 14/11/2026. Wiki ghi projectile bullet cho orbital từ 4.11. Ca Vạn Kiếm có bằng chứng parse riêng, chưa đo runtime.
