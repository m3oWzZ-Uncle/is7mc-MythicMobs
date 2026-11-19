# Advanced Slash và Projectile Spread

**Đợt 02 · syntax-checked.** Source đã đọc tĩnh, hành vi lấy mẫu, hướng và va chạm chưa xác minh trong game. [Checkpoint](iontech-study-checkpoint.json)

## Advanced Slash

Input gồm origin, đích lấy hướng, `arc`, yaw/pitch/roll, thời gian, radius, số điểm và callback. Entry dùng branch, init nạp mặc định và ghi location gốc. Nhánh visual tạo slash, giữ cặp điểm trước/sau và nội suy `@line`; mỗi điểm tính hướng từ origin để dịch điểm taper. Nhánh hit lấy radius giảm theo `radius−2·hitboxsize`, chọn hits ngay hoặc rải theo duration, rồi dựng totem ngắn ở mẫu trên đường nối. Callback cuối nhận entity và gọi skill do caller truyền. [Init và các nhánh](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/advanced_slash-mechanic.yml#L47) · [Totem](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/advanced_slash-mechanic.yml#L166)

**INFERENCE.** Hình VFX và hitbox chia sẻ góc nhưng có thể lệch vì radius, số điểm, duration và đường nối khác nhau. Có hit theo `@trigger` riêng sau init. Hai aura được viết bên cạnh việc set cờ `slash_hit`; cần truy caller và đo xem cờ có thật sự chặn damage trùng giữa mẫu hoặc caster. Test mép cung và hai người cast cùng mục tiêu. Với một cung cơ bản, dùng `slash` core với `onPoint` và `onHitEntity` trong cùng một mechanic. [Wiki Slash](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/slash) · [Ca 013](../../tests/training-sandbox/013-hitzone-vfx/README.md)

## Spread, Barrage và Pierce

- **Spread:** lưu origin một lần, một hướng gọi trực tiếp, nhiều hướng lấy điểm do Slash sinh rồi gọi `vskill` theo ID tham số. `points` và arc quyết định lượng và góc phát; roll ngẫu nhiên cộng 180° khi bật `twoside`. [Spread](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/projectile-skills.yml#L11)
- **Barrage:** dùng parity `2·(itr mod 2)−1`, polygon dịch nguồn và ray trace chọn đích với độ lệch. Chưa thấy cập nhật `itr` trong đoạn barrage của file này. Cần test số lần lặp và luân phiên thực. Scatter được đánh dấu **INCOMPLETE**. [Barrage và Scatter](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/projectile-skills.yml#L42)
- **Pierce:** khởi tạo `hits`, tăng theo callback và kết thúc projectile khi số hit đạt/vượt giới hạn. Cần xác nhận một hit callback tương ứng đơn vị mong muốn và kiểm tra hai projectile có giữ bộ đếm độc lập. Với đạn dừng ở mục tiêu đầu, chọn `sE=true`. [Pierce](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/projectile-skills.yml#L91) · [Wiki Projectile](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/projectile)
- **HIGH_RISK:** Fractal kết thúc một đạn có thể tạo 3–5 lượt mới và ghi block. Bài thay thế dùng một cha, hai con và không có cạnh ngược. [Fractal](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Demo%20Skills/fractal.yml) · [Ca 012](../../tests/training-sandbox/012-bounded-fork/README.md)

## Demo và VFX

| File | Luồng đọc từ YAML và điểm cần thử |
| --- | --- |
| [Shot](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Demo%20Skills/shot.yml#L1) | Eye origin → projectile → VFX tick/end và damage chỉ từ callback entity. Entry truyền `range=12`, còn projectile khai báo `MaxRange=64`. Đo quãng thực tế trước khi dùng tham số entry làm giới hạn. |
| [Chain Missile](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Demo%20Skills/chain_missile.yml#L5) | Ray trace phân biệt entity/location rồi chuyển cho `chainmissile` với `bounces=12`. Xác nhận cơ chế và edition trên build, thứ tự chọn đích, cùng chi phí khi nhiều entity. |
| [Spiral Shot](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Demo%20Skills/spiral_shot.yml#L15) | Callback tăng iteration, lấy 3 mẫu Slash quanh đường đạn và đặt roll `24·iteration` độ. Quỹ đạo VFX thay đổi, chưa thấy cập nhật hướng đạn ở đoạn này. |
| [Particle Spiral](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/particle_spiral-vfx.yml#L45) | Dùng Slash, giữ cặp điểm và truyền sang callback vẽ. Kiểm tra mẫu đầu, hai lần cast và ID alias trùng. |
| [Particle Shockwave](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/particle_shockwave-vfx.yml#L31) | Slash sinh điểm, mỗi điểm tạo projectile tồn tại ngắn để lấy hướng cho VFX. Demo cấu hình 100 điểm. Đo chi phí theo điểm trước khi dùng cùng nhiều caster. |

Công thức hình học riêng có phép thử tại [Advanced Math](../advanced-math/geometry.md).
