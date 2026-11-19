# Hiệu năng MythicMobs

Mốc đọc **MythicMobs 5.14.0**. Các thay đổi cấu hình dưới đây là giả thuyết cần đo trên server với gameplay dự kiến. [Nguồn và phiên bản](../../docs/wiki/README.md)

## Xác định phần việc cần đo

| Điểm phát sinh tải | Cách phân tích và thử thay đổi |
| --- | --- |
| `~onTimer` | Ghi interval và số mob hoạt động. Timer dùng đồng hồ chung, nên quan sát cả các tick mà nhiều mob cùng kích hoạt. Nếu một sự kiện sẵn có biểu đạt đúng gameplay, thử dùng nó thay cho quét định kỳ. Kiểm tra lại độ trễ phản hồi và số lần cast. [On Timer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer) |
| Tìm và xử lý mục tiêu | Ghi bán kính, tập ứng viên, số kết quả và các callback chạy sau đó. Chọn phạm vi đúng gameplay. `sort` và `limit` giới hạn kết quả theo tài liệu, còn chi phí tìm và sắp xếp cần đo. [Target Limits](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters#target-limits) |
| Projectile và aura | Ghi số instance đồng thời, duration, interval, callback mỗi tick và số hit. Nếu chỉnh interval hoặc nội suy, thử cả mục tiêu di chuyển nhanh, va chạm tường, nhiều người đứng sát nhau và thời điểm cleanup. [Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile), [Aura](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/aura) |
| Particle và model | Đo server khi gặp mật độ hiệu ứng thực tế. Thu thêm FPS hoặc quan sát giật trên cùng máy client và cùng góc nhìn. Thử điều chỉnh mật độ hiệu ứng trong giới hạn vẫn thấy được telegraph và mốc va chạm. [On Timer](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers/onTimer), [ModelEngine State](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State) |

## Đo trước và sau

1. Ghi build server/plugin, số người chơi, số mob, arena, thời gian đo và số lượt cast. Dùng cùng điều kiện ở hai lần đo và tái hiện đúng đoạn có vấn đề. Paper tích hợp spark từ Minecraft 1.21. [PaperMC Profiling](https://docs.papermc.io/paper/profiling/)
2. Ghi TPS và MSPT, ưu tiên xem median, p95 và max để thấy cả mức thường gặp lẫn spike. Khi có spark và quyền dùng, chạy `/spark tps` trong lúc tái hiện. Dùng `/spark profiler start --timeout 600` theo ví dụ Paper khi cần lấy mẫu và lưu mã hoặc liên kết báo cáo phù hợp với phạm vi chia sẻ dữ liệu. [spark TPS và MSPT](https://spark.lucko.me/docs/guides/TPS-and-MSPT), [PaperMC Profiling](https://docs.papermc.io/paper/profiling/)
3. Chọn một thay đổi, đo lại rồi so cả số liệu và hành vi. Ghi số mục tiêu bị trúng, tick chạm đòn, số lần gây damage và cleanup cuối lượt. Nếu mẫu tải thay đổi giữa hai lần đo, ghi yếu tố đó cùng kết quả. [spark Using the Viewer](https://spark.lucko.me/docs/Using-the-viewer)

Mẫu kết quả cho mỗi lần đo: `build | kịch bản | người chơi | mob | lượt cast | thời lượng | TPS | MSPT median/p95/max | báo cáo spark | kiểm tra gameplay`.

## Mốc phiên bản có ảnh hưởng khi so kết quả

- **5.11.0** thêm `ShareComponents` để dùng chung các mechanic, targeter và condition giống nhau. **5.12.1** ghi nhận xếp hàng và gom các particle effect để giảm lưu lượng packet. Ghi build và giá trị cấu hình thực tế khi so kết quả giữa server. [Changelog 5.11.0 và 5.12.1](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd)
- **5.14.0** ghi nhận `General.AsyncPathfinding` cho pathfinding và quét mục tiêu của AI goals trên worker threads với Premium, trừ Folia. Đây là phạm vi thay đổi được changelog nêu. Đối chiếu config thật và đọc profile theo thread khi kiểm tra. [Changelog 5.14.0](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd#5140)
