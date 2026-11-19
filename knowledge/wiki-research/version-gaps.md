# Khác biệt giữa snapshot và tài liệu phát hành

Snapshot là checkout Git của wiki tại commit `db28fb6a7443aca1040ac29be76b840ff7d4d38f`, ngày 02/08/2026 UTC. Changelog trong snapshot bắt đầu bằng 5.13.0. Mốc phát hành dùng để đối chiếu trong kho là 5.14.0. Một số trang snapshot phản ánh thay đổi của 5.13.0, cần xem từng mục và phiên bản plugin của server. [Changelog bản nhập](../../docs/wiki/MythicMobs/changelogs/Changelogs.md), [changelog online](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#5140)

| Tính năng | Bằng chứng và cách áp dụng |
| --- | --- |
| `PackOverrides` và `FileOverrides` | Trang `Packs.md` của snapshot chưa có phần này. Ở 5.14.0, overrides bỏ qua gói hoặc file khi điều kiện khớp. Dependencies bỏ qua khi điều kiện yêu cầu thiếu. Dùng khi có nhiều bản pack theo addon. Thử cả trường hợp có và thiếu addon, đồng thời kiểm tra log về pattern và việc đăng ký file. [Snapshot](../../docs/wiki/MythicMobs/Packs.md), [Packs online](https://wiki.mythiccraft.io/mythicmobs/Packs#dependencies-and-overrides) |
| Tiền tố `?@` | Changelog 5.14.0 xác nhận xét từng target trên một dòng sau khi targeter chạy. `?` xét caster. Khi cần giữ cấu hình dùng được trên phiên bản cũ hơn, cân nhắc `TargetConditions` trong metaskill hoặc cú pháp inline targeter mà build hỗ trợ. Xác nhận edition trước khi chọn cú pháp inline. [Snapshot](../../docs/wiki/MythicMobs/Skills/Inline-Conditions.md), [changelog online](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#conditions) |
| `hitBlockConditions` | Có ở cả bản nhập và wiki online. Changelog ghi trong 5.13.0. Thuộc tính lọc **block** mà đạn định dừng, cần `stopAtBlock` và Premium. Dùng khi vật liệu quyết định va chạm. Thử đạn xuyên block không khớp và dừng tại block khớp. [Snapshot](../../docs/wiki/MythicMobs/Skills/Mechanics/projectile.md), [Projectile online](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [changelog online](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#5130) |

| `Hidden` cho metaskill | Có từ 5.14.0 theo changelog. Mặc định false. Dùng cho helper nội bộ khi muốn ẩn khỏi gợi ý lệnh. ID vẫn gọi được, vì vậy không dùng khóa này để kiểm soát quyền thực thi. Kiểm tra autocomplete và gọi trực tiếp trên build đích. [Snapshot](../../docs/wiki/MythicMobs/Skills/Metaskills.md), [Metaskills online](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#hidden) |

Chỉ mục core đã có các mục 5.14.0 như `tickRate`, `@bound`, `onPlayerEnter`/`onPlayerExit`, `SetSulfurCubeArchetype` và sáu conditional AI goals. Chúng chưa có trang khớp theo đường dẫn trong snapshot. Có thể mở trang online từ `audit-gaps`. [Changelog 5.14.0](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs#5140)

**Mức kiểm chứng** `Documented` theo các điểm đối chiếu trên. Phạm vi phiên bản lấy theo mục changelog. Các điều kiện nạp pack và va chạm chưa được chạy trên server trong đợt này.
