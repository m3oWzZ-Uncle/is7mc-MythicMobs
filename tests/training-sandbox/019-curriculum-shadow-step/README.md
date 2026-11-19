# Bài 02 · Ảnh Bộ

Người chơi đứng tại vị trí hiện tại rồi lướt ngắn theo yaw lúc cast. Đề bài cần một cú lướt ngang có va chạm và đi lại bình thường sau đó. Bản r1 dùng MythicMobs core, mốc đối chiếu **5.14.0**, không khai báo addon. [Đề Foundation](../../../training/levels/foundation.md)

**Thiết kế.** `@Forward{f=5;lockpitch=true}` lấy điểm ngắm theo phương ngang. `lunge{velocity=0.85;velocityY=0}` tạo một lần đẩy. `f=5` là khoảng tới điểm ngắm. Quãng lướt thực tế phụ thuộc chuyển động và va chạm; đo trên sàn phẳng để căn lực 0,85. Chọn cú đẩy một lần để người chơi tiếp tục dùng điều khiển mặc định. Không cần khóa điều khiển hay timer dừng. Cooldown 3 giây là thông số bài thử. [Danh mục Mechanics](https://wiki.mythiccraft.io/mythicmobs/Skills/mechanics) · [Lunge](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/lunge) · [Forward](https://wiki.mythiccraft.io/mythicmobs/Skills/Targeters/Forward) · [Cooldown](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills#cooldown)

Đã tra [bài lướt player 004](../004-player-forward-dash/README.md) làm tham khảo cú pháp và [quy tắc về guard](../../../memory/decisions/require-evidence-for-defensive-logic.json). Bài 004 chưa có bằng chứng gameplay. Lựa chọn `lunge` ở Dash Cleave là một ca boss nhắm người chơi. `velocity` vẫn là phương án phù hợp nếu phiên bản mới của đề cần sửa vectơ hoặc dừng theo một mốc cụ thể. [Movement KB](../../../knowledge/player-skills/movement/README.md)

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server, dùng người chơi Survival có quyền test. Đánh dấu điểm bắt đầu, đứng yên, bỏ các hiệu ứng làm thay đổi tốc độ. Đo tọa độ bằng F3 hoặc quay để so thời điểm cast và dừng. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)

```text
/mm reload
/mm test cast TrainingAnhBo
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `yaw` | Từ cùng điểm, cast về hai hướng cách nhau 90°. Người chơi dịch theo đúng hướng ngang của mỗi lần cast. Sau lướt vẫn đổi hướng và đi bộ được. |
| `pitch` | Giữ yaw, nhìn thẳng, nhìn lên rõ rồi nhìn xuống rõ. Cú lướt trên sàn phẳng không tự đẩy lên hay xuống. Ghi quãng đi thực tế. |
| `wall-and-recovery` | Đứng cách tường đá đặc khoảng 1 block và lướt thẳng vào. Caster không xuyên tường, có thể lùi hoặc đi ngang ngay sau đó. |
| `ledge` | Thử tại bục thấp có sàn phía dưới và đủ chỗ tiếp đất. Khi đi khỏi mép, người chơi rơi theo trọng lực bình thường và tiếp tục điều khiển được sau khi tiếp đất. |
| `independent-cooldown` | A và B đứng ở hai làn. A cast và thử lại trong 3 giây, B cast trong cửa sổ hồi của A. A chỉ cast lại được khi hồi xong và B lướt riêng theo hướng của mình. |

**Trạng thái.** Chờ log nạp, kết quả năm ca và lời xác nhận trên đúng bản YAML. [Hồ sơ ca](case.json)

**Phản hồi thiết kế.** Người dùng đánh giá r1 đúng cho dash thông thường. Với biến thể Ảnh Bộ đi bộ, họ đề xuất thử hạ điểm ngắm `y=-10` để đạt cảm giác sát nền. [Phân tích và ca so sánh](../../../feedback/decisions/MM-D-2026-003.md)
