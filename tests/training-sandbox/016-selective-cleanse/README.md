# 016 · Thanh tẩy có chọn lọc

Xóa Poison của caster và giữ hiệu ứng khác. Chỉ định `type` vì bỏ trường này làm mechanic xóa mọi hiệu ứng. Đây là ca utility một lần, không có yêu cầu cooldown hay kiểm tra có Poison trước khi cast. [PotionClear](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/potionclear)

## Thử trong Minecraft

Chép [YAML](Skills/player-skill.yml) vào `Skills/` trên bản sao server. Dùng MythicMobs core với mốc đối chiếu 5.14.0, không khai báo addon. Dùng tài khoản Survival có quyền chạy test. Player chạy lệnh là caster. [Lệnh MythicMobs](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions) · [Ví dụ player làm caster](https://wiki.mythiccraft.io/mythicseasons/examples/Common-Examples)

```text
/mm reload
/mm test cast TrainingSelectiveCleanse
```

| Ca | Thao tác và kỳ vọng |
| --- | --- |
| `selective` | Dùng `/effect give <A> minecraft:poison 20 0` và `/effect give <A> minecraft:speed 20 0` trên server thử. A cast khi cả hai hiệu ứng còn thời lượng. Poison biến mất và Speed còn hiệu lực. |
| `caster-only` | Cho B cũng có Poison và để B đứng cạnh A. A cast. Poison của B còn nguyên. |
| `empty` | A chỉ có Speed rồi cast. Speed không mất và không xuất hiện ảnh hưởng mới. |

**Trạng thái.** Chờ log nạp và gameplay. Lưu build, kết quả quan sát và xác nhận vào [hồ sơ ca](case.json) và [nhật ký](../../../feedback/training/README.md).
