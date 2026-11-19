# 017 · Hồi máu có báo trước

Báo trước bằng chat, chờ 20 tick rồi hồi 4 điểm máu cho cùng caster. Cooldown 6 giây để chỉ có một lượt đang chuẩn bị. Ca thử chọn đòn cam kết sau báo trước, nên người di chuyển vẫn nhận hồi. Giới hạn phạm vi ở player còn sống trong cùng phiên thử. Không thêm cơ chế chủ động hủy theo di chuyển, buff tái sinh hay timer lặp. [Heal](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/heal) · [Delay](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/delay)

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server. Dùng MythicMobs core với mốc đối chiếu 5.14.0, không khai báo addon. Dùng tài khoản Survival có quyền chạy test. Player chạy lệnh là caster. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [Ví dụ player làm caster](https://wiki.mythiccraft.io/mythicseasons/examples/Common-Examples)

```text
/mm reload
/mm test cast TrainingDelayedSelfHeal
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `timing` | Cho A thiếu ít nhất 4 điểm máu. Thử trong điều kiện không tự hồi máu, quay clip lúc cast. Thông báo xuất hiện trước, máu chỉ tăng sau 20 tick. |
| `movement` | A di chuyển sau thông báo. Lần hồi vẫn tới khi hết thời gian báo. |
| `caster-only` | A và B cùng thiếu máu. A cast, chỉ A được hồi; chạy đối chứng để loại trừ hồi tự nhiên. |
| `natural-cap` | Cho A thiếu ít hơn 4 điểm rồi cast sau cooldown. Máu dừng tại mức tối đa bình thường. |

**Trạng thái.** Chờ log nạp và gameplay. Lưu build, kết quả quan sát và xác nhận vào [hồ sơ ca](case.json) và [nhật ký](../../../feedback/training/README.md).
