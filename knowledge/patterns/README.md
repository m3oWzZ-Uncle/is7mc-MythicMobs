# Mục lục pattern MythicMobs

Chọn bài theo hành vi cần thiết kế hoặc lỗi cần chẩn đoán. Mỗi bài dẫn đến metaskill, callback hoặc dòng YAML gốc và ghi ca thử server cần thiết. Tra đường dẫn, ID và bằng chứng cú pháp trong [chỉ mục dataset](../dataset-index.md).

| Nhu cầu | Đọc trước | Dấu hiệu tìm kiếm | Ví dụ gốc |
| --- | --- | --- | --- |
| Đạn thật, hụt mục tiêu nhanh, trúng tường, AoE ở điểm va chạm | [Projectile có va chạm](projectile-va-cham.md) | `projectile`, `onHit`, `onHitBlock`, `tickinterpolation`, `@origin` | Vạn Kiếm Quy Tông |
| Hit lệch frame animation, wind-up hoặc hồi đòn | [Đồng bộ animation và damage](dong-bo-animation-damage.md) | `state`, `delay`, `SudoSkill`, `@Children`, `@EIC` | Lục Cốt Chi Vương |
| Giữ một nguồn damage khi có đòn vanilla và skill riêng | [Hủy event đồng bộ](huy-event-dong-bo.md) | `~onAttack`, `sync=true`, `CancelEvent` | Conductor |
| Boss đổi phase và add đổi hành vi theo trận | [Phase theo score và signal](boss-phase-score-signal.md) | `score`, `stance`, `signal`, `offgcd`, reset | Conductor |
| Skill chọn sai phe, sai nhánh, sai đối tượng xét | [Điều kiện theo caster, target và trigger](conditional-skills.md) | `Conditions`, `TargetConditions`, `TriggerConditions`, `castinstead`, `mmoCanTarget` | Lục Cốt, Sacred Ward, Xích Huyết |
| Biến bị ghi đè giữa cast, hai caster hoặc lần làm mới aura | [Scope biến và vòng đời](variable-scope.md) | `skill.var`, `caster.var`, `branch`, counter, `onEnd` | Lục Cốt, Vạn Kiếm |
| Nhặt đúng chủ, thu hồi, hết hạn hoặc dọn add | [Summon có chủ và cleanup](summon-owner-cleanup.md) | `sio`, `sip`, `owner`, `@Children`, `@Owner`, `remove` | Xích Huyết, Conductor |
| Lag khi nhiều timer, projectile, VFX hoặc caster | [Tối ưu timer và callback](toi-uu-timer-va-callback.md) | `~onTimer`, `repeatInterval`, projectile interval, MSPT, FPS | Vạn Kiếm, Conductor, Assistant |
| Skill người chơi gọi sai entry, modifier rỗng hoặc cooldown chồng | [Cầu nối MMOCore và MythicLib](cau-noi-mmocore-mythiclib.md) | `mythicmobs-skill-id`, `source`, `<modifier.…>`, `SUPPORT_ACTION` | Sacred Ward |
| Cùng ID nhưng hành vi khác giữa hai server hoặc hai pack | [Quản lý biến thể cùng ID](bien-the-cung-id.md) | SHA-256, guard aura, duplicate ID, regression | Arctic Knight |
| Xác định người thực sự trúng và số lần damage | [Hitbox và damage](damage-hit-detection.md) | `damage`, `mmodamage`, `onHit`, `onEnd` | Fishball, SkyFall |
| Tách cảnh báo, thực thi, callback và hồi chiêu | [Skill nhiều giai đoạn](multi-stage-skill.md) | entry, delay, repeat, recovery | Vạn Kiếm, Lục Cốt |
| Dash lệch hitbox hoặc mob phụ chọn sai aggro | [Movement và combat AI](movement-combat-ai.md) | `lunge`, `@forward`, AI goals, AI targets | Xích Huyết, Arctic Knight |
| Hai caster hoặc hai boss có thể tác động nhầm trận | [Cô lập trong multiplayer](multiplayer-safety.md) | `mmoCanTarget`, `owner`, `@Children` | Sacred Ward, Xích Huyết, Conductor |
| Vũ khí bay đi rồi quay lại theo người ném | [Projectile khứ hồi](projectile-khu-hoi-owner.md) | `projectile`, `onEnd`, `missile`, `@owner` | Soul Weaver |
| Boss giữ pose và khóa hành động trong wind-up | [Khóa và trả trạng thái](khoa-hanh-dong-trong-windup.md) | `offgcd`, `hasaura`, `setAI`, `lockmodel` | Wu, Armor Boss |
| Lore, scaling và hitbox có thể lệch giữa các plugin | [Đối chiếu modifier](doi-chieu-hop-dong-modifier.md) | `modifiers`, `radius`, `blockmask`, `mythicmobs-skill-id` | IgnisArctic |
| Nâng player, giữ điểm trên không, chạy VFX và bắn theo nhịp | [Neo caster và loạt projectile](projectile-neo-caster.md) | `SetVariableLocation`, `Orbital`, `Teleport`, `@Forward` | Vạn Kiếm Quy Tông |

## Cách đọc bằng chứng

- **FACT** là điều có bằng chứng. `FACT · wiki` ghi hành vi hãng mô tả. `FACT · YAML` ghi trường, ID hoặc giá trị xuất hiện trong file. `FACT · bằng chứng` ghi kết quả đã kiểm tra và phạm vi của kết quả đó. Bằng chứng cấu hình và bằng chứng chạy game có mức xác minh riêng. [Quy ước phiên bản](../../docs/wiki/README.md), [Tiêu chí kiểm thử](../../tests/README.md)
- **INFERENCE** là luồng dự kiến, đánh đổi hoặc giả thuyết rút từ YAML và tài liệu. Sơ đồ trong mỗi bài mô tả luồng suy ra từ nguồn. Dùng các ca thử ghi trong bài để xác nhận trước khi áp dụng như hành vi đã biết.
- **PREFERENCE** là lựa chọn thiết kế người dùng đã xác nhận. Khi có, ghi câu xác nhận, nguồn, ngày và phạm vi áp dụng cùng [hồ sơ quyết định](../../feedback/decisions/TEMPLATE.md). Chưa có xác nhận về việc người dùng ưu tiên một kỹ thuật cụ thể trong các mẫu đợt 01.

**PREFERENCE · quy tắc chung đã xác nhận.** Chọn kiến trúc đơn giản nhất đáp ứng đầy đủ hành vi được yêu cầu, bảo toàn gameplay. Phạm vi là thiết kế trong repo này. [AGENTS.md](../../AGENTS.md)

Các ví dụ hiện có bằng chứng `syntax-checked` theo đợt tương ứng. Build server, MythicMobs, edition và addon cần ghi trước khi xác nhận tương thích. Các khối YAML là trích đoạn phục vụ đọc nguồn. [Tiến độ và mức kiểm chứng](../dataset-index.md)
