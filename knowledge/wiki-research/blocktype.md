# BlockType · xét vật liệu ở một vị trí

**Chức năng và cú pháp.** `blocktype{type=<danh sách>}` xét vật liệu tại vị trí đang được kiểm tra. Đặt trong `TargetConditions` khi muốn xét vị trí truyền từ targeter. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/blocktype), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Conditions/blocktype.md)

**Thuộc tính.** `types` có các alias như `type`, `material` và `block`. Wiki ghi mặc định `DIRT` và hỗ trợ danh sách, wildcard, block tag. Đối chiếu cách khớp block state theo build. [Điều kiện và ngữ cảnh](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions)

**Ví dụ và trường hợp dùng.** Vạn Kiếm kiểm `AIR,CAVE_AIR,VOID_AIR` ở các điểm đại diện trước khi di chuyển. Dùng để lọc điểm đáp hoặc vật liệu cho phép va chạm. Nếu cần đánh giá một hộp va chạm hay cả đoạn đường, nhiều mẫu kiểm tra hoặc công cụ chuyên dụng phù hợp hơn kiểm một điểm. [Ví dụ YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L21), [Projectile](../entries/mythicmobs--meta-mechanic--projectile.md)

**Lỗi thường gặp.** Dùng `Conditions` khi muốn kiểm điểm truyền vào, hoặc nhầm vật liệu cho phép với block có hitbox trống. Thử mép block, trần thấp và vật liệu ngoài danh sách.

**Phiên bản và xác minh.** `Documented`, ngày 14/11/2026. Changelog ghi hỗ trợ partial block state ở 5.14.0. [Changelog](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#conditions)
