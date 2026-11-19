# ModelEngine cho Player Skills

**FACT · cấu hình.** Lục Cốt gọi animation trên model con và điều phối damage ở luồng riêng. Vạn Kiếm dùng model cho phần hiển thị projectile. Đối chiếu ID model và state từ asset, YAML và registry thực tế. [Lục Cốt](../../patterns/dong-bo-animation-damage.md) · [Vạn Kiếm](../../patterns/projectile-va-cham.md) · [ModelEngine State](https://wiki.mythiccraft.io/modelengine/Skills/Mechanics/State)

Theo dõi caster gốc và caster sau khi gọi model. Đo mốc chạm, recovery và dọn model ở các đường kết thúc mà skill hỗ trợ. Ghi build ModelEngine cùng MythicMobs khi thử, nhất là khi projectile dùng hitbox của model hoặc animation chạy bằng callback.

Với đòn chém trước mặt có model báo hiệu rồi model chém 180°, chọn totem cho vùng tập trung trước caster hoặc targeter theo góc/tầm khi vùng cần bám cung. Căn cùng pivot, yaw và frame chạm. [Kinh nghiệm và ca đối chiếu](../../../feedback/decisions/MM-D-2026-005.md)
