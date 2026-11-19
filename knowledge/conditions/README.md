# Conditions

Mốc đọc **MythicMobs 5.14.0**. Xác định đối tượng được xét trước khi chọn điều kiện. Wiki phân loại condition theo ngữ cảnh như Entity, Location, Compare và Meta. [Nguồn và phiên bản](../../docs/wiki/README.md), [Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions)

| Trường metaskill | Đối tượng được xét | Ví dụ dùng |
| --- | --- | --- |
| `Conditions` | Caster | Kiểm tra ngưỡng HP của boss trước khi chuyển phase. |
| `TargetConditions` | Entity hoặc location đã kế thừa | Lọc người chơi nhận hiệu ứng. |
| `TriggerConditions` | Entity kích hoạt chuỗi | Chỉ xử lý sự kiện do người chơi gây ra. |

[Metaskills, revision đã đối chiếu](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills?version_id=9b056129fdf1d2b9787ddb14bfbb6380ccce3078), [Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions)

- `true` yêu cầu điều kiện đúng. `false` yêu cầu điều kiện sai. `cast` có thể gọi thêm skill khi điều kiện đúng, còn `castinstead` chuyển sang skill khác. Kiểm tra action ở đúng khối condition và đối chiếu skill ID được gọi. [Condition Actions](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions#condition-actions)
- `healthpercent{p=<50%} true` là ví dụ wiki về condition dưới 50% HP. `HealthPercent` có tùy chọn tính absorption. Nếu mục tiêu là boss, đặt điều kiện vào ngữ cảnh caster và kiểm thử đúng bằng ngưỡng, thấp hơn ngưỡng và khi có absorption. Health modifier sau trigger là cú pháp riêng, xem [boss phases](../architecture/boss-phases.md). [HealthPercent](https://wiki.mythiccraft.io/mythicmobs/skills/conditions/HealthPercent), [Health Modifiers](https://wiki.mythiccraft.io/mythicmobs/Skills/Skills#health-modifiers)
- `variableEquals` so sánh giá trị ở scope đã chọn. Khi dùng để chuyển trạng thái, thử biến chưa tồn tại, biến có giá trị hợp lệ và sai kiểu. [VariableEquals](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableequals), [Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables)
- Wiki đánh dấu dạng inline `conditions=[…]` trên targeter ở trang Inline Conditions là Premium. **5.14.0** bổ sung tiền tố `?@` để xét từng mục tiêu sau khi targeter chạy. Kiểm tra đúng dạng, edition và build trước khi chuyển cấu hình. [Inline Conditions](https://wiki.mythiccraft.io/mythicmobs/Skills/Inline-Conditions), [Changelog 5.14.0 mục Conditions](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd#conditions)

Khi đọc case, ghi mỗi condition theo dạng **đối tượng → dữ liệu tại thời điểm xét → action → kết quả kỳ vọng**. Thử lần lượt case pass, fail, không có target và hai target chỉ một người pass. [Ví dụ kiểm tra tương tác](../../examples/simple/README.md)
