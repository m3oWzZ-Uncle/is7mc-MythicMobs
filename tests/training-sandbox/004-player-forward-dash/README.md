# Bài 004 · Lướt theo hướng nhìn của người chơi

Utility active dùng một cú lướt ngang theo yaw lúc cast. Trong bài, người nhập lệnh là caster. `@Forward` cung cấp điểm ngắm. Boss, mob và người chơi bên cạnh không tham gia làm caller. Cấu hình dùng MythicMobs core **5.14.0** làm mốc đối chiếu, không khai báo addon. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [Thiết lập người chơi làm caster khi dùng lệnh test](https://wiki.mythiccraft.io/mythicseasons/examples/Common-Examples)

## Thiết kế

- **FACT · tài liệu.** `@Forward` chọn điểm phía trước caster. `lockpitch=true` lấy điểm như pitch bằng 0. Danh mục Mechanics mô tả `lunge` đưa caster về phía mục tiêu. Chọn `lunge` cho tình huống này vì có một điểm ngắm phía trước cần lao tới. `velocity` hữu ích khi yêu cầu cần đặt hoặc thay đổi vectơ trực tiếp. [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [Mechanics](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics) · [Lunge](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/lunge) · [Velocity](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/velocity)
- **INFERENCE · cấu hình bài thử.** `f=5` đặt điểm ngắm. Lực 0,85 và `velocityY=0` là giả định cho cú lướt trên sàn phẳng. Quãng lướt và va chạm tường phải đo trên build thực tế. Cooldown 3 giây cho phép thử hồi chiêu riêng của từng caster. [Cooldown của metaskill](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cooldown)
- Bài có một mechanic di chuyển và cooldown, không cần damage, aura, biến, timer hay hệ thống tài nguyên. Khi tích hợp class/item, đường cast và chi phí của addon cần ca riêng. [Movement](../../../knowledge/player-skills/movement/README.md) · [Tích hợp](../../../knowledge/player-skills/integrations/README.md)

## Thử trong Minecraft

Chép [YAML](Skills/player-forward-dash.yml) vào `Skills/` của bản sao server. Dùng hai người chơi Survival có quyền test, bật ghi hình nếu có thể. Chọn sàn phẳng, đứng yên trước mỗi lượt, đánh dấu điểm bắt đầu và đợi hơn 3 giây giữa các ca độc lập. Không cần spawn mob.

```text
/mm reload
/mm test cast TrainingPlayerForwardDash
```

| Ca | Thao tác | Kỳ vọng |
| --- | --- | --- |
| `caster-only` | A đứng cạnh B và cast. B đứng lệch đường lướt để tránh bị va chạm bởi entity. | Chỉ A nhận chuyển động của skill. Hai người giữ nguyên máu trên sàn phẳng. |
| `heading-and-pitch` | A cast theo hai hướng yaw khác nhau. Lặp cùng yaw khi nhìn chếch lên rồi chếch xuống. | Chuyển động đổi theo yaw và cú lướt không tự thêm lực dọc do pitch. Ghi quãng dịch chuyển thực tế. |
| `wall` | A đứng trước một tường đá đặc cao ít nhất 3 block, cách khoảng 1 block và cast thẳng vào tường. Sau đó cast trên đường trống để đối chứng. | A bị tường chặn và vẫn có thể đi bình thường khi cú lướt kết thúc. |
| `independent-cooldown` | A cast, thử lại ngay khi đang hồi. Trong cửa sổ 3 giây của A, B cast trên làn riêng. A thử lại sau hơn 3 giây tính từ phát đầu. | A bị chặn trong cooldown và cast lại sau khi hồi. B vẫn có thể cast lượt đầu. |

Giữ log reload, phiên bản server/MythicMobs và kết quả quan sát trong [hồ sơ bài](case.json). Chưa có bằng chứng nạp server hoặc gameplay.
