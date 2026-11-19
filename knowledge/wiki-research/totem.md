# Totem · hitbox cố định tại một điểm

**Chức năng và cú pháp.** `totem{...} @<location>` đặt bộ phát hit đứng yên. `onTick` phù hợp cho visual và `onHit` chạy khi phát hiện mục tiêu trong vùng theo khoảng nhịp. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/totem?version_id=1f8283a3389908f340de3fcb5bc030ebbd4ae456), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Mechanics/totem.md)

**Thuộc tính.** `charges` (`ch`, `c`) mặc định 0, `yOffset` (`yo`) mặc định 1, `stopAtEntity` mặc định false. `hugSurface` và `hugLiquid` mặc định false. Các callback, bán kính và thời lượng dùng nhóm thuộc tính kế thừa của projectile theo trang mục. [Projectile](../entries/mythicmobs--meta-mechanic--projectile.md)

**Ví dụ và trường hợp dùng.** Soul Weaver đặt Totem trong nhánh tay bẫy tại `@TriggerLocation` với `ch=1`, `i=1`, `md=40` và bán kính ngang/dọc 2. Hợp cho bẫy hoặc vùng đứng yên có thời hạn. Dùng projectile khi hitbox di chuyển, hoặc một lần chọn AoE khi hiệu ứng chỉ cần một nhịp. [YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/EC_soul_Weaver/Skills/EC_SoulWeaver_Scythe.yml#L110)

**Lỗi thường gặp.** Đặt visual và hitbox ở hai tâm khác nhau hoặc đếm `charges` như số tick. Thử số lần hit khi hai người bước vào cùng tick, vị trí lệch cao độ và callback bị ngắt. [Phân tích bẫy Soul Weaver](../dataset-batch-02.md)

**Phiên bản và xác minh.** `Documented`, ngày 14/11/2026. Ví dụ dataset đã parse. Chưa thử hành vi charges trong game.
