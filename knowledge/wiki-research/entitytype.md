# EntityType · lọc loại entity và biến thể

**Chức năng và cú pháp.** `entitytype{type=PLAYER}` xét loại entity trong đúng ngữ cảnh condition. `type` (`t`) nhận danh sách các loại. Wiki có cú pháp lồng biến thể như `CAT{variant=TABBY}`. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/EntityType), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Conditions/EntityType.md)

**Thuộc tính.** `type` nhận loại entity Minecraft. Bên trong loại, các khóa như `variant`, `color` hoặc `style` tùy loài. Ngựa có `color` và `style`, còn mèo dùng `variant`. Đối chiếu bảng phiên bản ở trang gốc khi lọc loại entity mới.

**Ví dụ và trường hợp dùng.** Vạn Kiếm có `entitytype{t=PLAYER}` ở entry và loại `ARMOR_STAND` trong bộ lọc projectile. Dùng khi loại entity quyết định khả năng trúng. Nếu cần nhận diện đúng ID của một MythicMob, dùng `MythicMobType`. [YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L1), [MythicMobType](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/mythicmobtype)

**Lỗi thường gặp.** Nhầm loại vanilla với ID tùy chỉnh, xét caster thay vì target hoặc dùng khóa biến thể cho loài không hỗ trợ. Thử một đối tượng hợp lệ, một loại bị loại và một mob có model/hitbox phụ.

**Phiên bản và xác minh.** Cả snapshot và wiki online đều mô tả nested variants. Changelog ghi phần đó ở 5.13.0. `Documented`, ngày 14/11/2026. Chưa chạy gameplay. [Changelog](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#entitytype-condition-nested-variant-matching)
