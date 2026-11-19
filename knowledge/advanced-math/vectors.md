# Vector, vị trí và vận tốc

**FACT · YAML, syntax-checked.** `get_location_vector` lưu location từ targeter, rồi chuyển tọa độ của location thành VECTOR; tên output là `<vec>_loc` và `<vec>_vec`. Đọc cùng phần `distance`, `get_direction_vector` và `knockback-eval`. [Vector Skills](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Mechanics/vector-skills.yml#L26) · [Knockback Core](../../incoming/IonTech/IonTech-s-Modular-Systems-main/packs/IonTech's%20Modular%20Systems/skills/Game%20Mechanic%20Skills/Skill%20Handlers/knockback_core.yml#L51) · [Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables)

| Thuật toán | Input → output và công thức | Cách IonTech triển khai | Giới hạn và cách đơn giản |
| --- | --- | --- | --- |
| Trừ vector | Điểm A, B → Δ = (Bx−Ax, By−Ay, Bz−Az) | `setvarloc` cho origin và đích, tách trường x/y/z trong distance hoặc dùng `.sub.` trong direction | Hai điểm cần cùng world; dùng targeter vị trí nếu chỉ cần chuyển hướng tới B. |
| Cự ly 3D và ngang | Δ → √(dx²+dy²+dz²), hoặc √(dx²+dz²) | Dựng VECTOR, dùng `sqrt(abs(...))`. `distance-vertical` trả riêng dy có dấu | `abs` dư với tổng bình phương hữu hạn. Khi chỉ so ngưỡng, có thể so tổng bình phương với r², hoặc chọn điều kiện khoảng cách core cho bài phù hợp. |
| Chuẩn hóa | Δ → Δ/‖Δ‖ | Chuỗi `.sub.<…>.normalized` trong `get_direction_vector` | Zero vector làm công thức không xác định; khi người và đích có thể trùng, phải định nghĩa rõ bỏ qua hoặc dùng một hướng có nghĩa. |
| Cộng và scale | B, unit u, lực k, độ nâng h → B + h + k·u | `knockback-eval` ghép vector đích, vector nâng và displacement đã chuẩn hóa | Biểu thức là vị trí đích dựng từ các vector. Không suy ra quãng dịch chuyển gameplay nếu chưa đo mechanic sau đó. Dùng `Throw` hoặc `velocity` khi đã đúng hướng/luật gameplay. |
| Vận tốc từ hai mẫu | P trước, P hiện tại → ΔP. Vận tốc trung bình = ΔP/Δt | `get_velocity_vector` giữ mẫu trước, trừ mẫu hiện tại rồi đổi mẫu cũ; `speed` là độ dài displacement theo mẫu | Cần hai mẫu và Δt hữu hạn. Với sampling 1 tick, đơn vị danh nghĩa là block/tick; đổi sang block/giây cần TPS thực hoặc giả định. Kiểm tra teleport và world change nếu dùng làm đo vận tốc. |

**Bổ sung toán.** Dùng dung sai khi so số thực. Có thể skip hướng khi ‖Δ‖ ≤ ε với ε gắn đơn vị và hành vi mong muốn. Bản gốc được trích làm bằng chứng và chưa kiểm chứng cho zero vector hay thay world. [Math MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Skills/Math)

**Bài thử độc lập.** A=(1,2,3), B=(4,6,3) cho Δ=(3,4,0), cự ly 5, ngang 3, cao có dấu 4 và unit=(0.6,0.8,0). Hai mẫu cách 0,5 giây từ A tới B cho (6,8,0) block/giây. Thử riêng A=B. [Bài 007](../../tests/training-sandbox/007-vector-dash/README.md) · [Kiểm thử số học](../../tests/test_iontech_math.py)
