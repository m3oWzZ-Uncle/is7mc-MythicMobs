# Variables

Mốc đọc **MythicMobs 5.14.0**. Scope xác định nơi giá trị tồn tại. `setvariable` cho phép chọn `type`, thời lượng và lưu lại qua một số sự kiện vòng đời tùy scope. [Nguồn và phiên bản](../../docs/wiki/README.md), [Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables), [SetVariable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable)

| Scope | Vòng đời hoặc đối tượng | Cách dùng trong thiết kế |
| --- | --- | --- |
| `SKILL` | Skill tree hiện tại | Dữ liệu tạm trong một lượt cast. Xem `branch` khi gọi metaskill con. |
| `CASTER` | Mob đang cast | Phase, cờ bận hoặc trạng thái riêng từng boss. |
| `TARGET` | Đối tượng của mechanic/condition | Dấu hiệu riêng từng target. Ghi rõ cờ có được dùng chung giữa các caster hay không. |
| `WORLD` | World hiện tại | Trạng thái dùng chung theo world. Kiểm tra trường hợp nhiều trận chung world. |
| `GLOBAL` | Server | Trạng thái chủ ý dùng chung cả server. |

[Variable Scopes](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes), [Skill và Branch](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill#branch-attribute)

- `var=caster.phase` định danh biến `phase` trong scope `CASTER`. Dùng `<caster.var.phase>` trong trường hỗ trợ placeholder. Dấu chấm dùng để phân tách scope và tên. [Variables, Usage và Variable Placeholders](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables)
- Wiki ghi kiểu mặc định của `setvariable` là `INTEGER`. Với text, khai báo `STRING`. `duration` dạng số dùng tick, `save` mặc định là `false`, và cả hai không áp dụng cho scope `SKILL`. Nếu case cần giữ trạng thái qua reload/restart, thử vòng đời đó trên chính scope và build dự kiến. [SetVariable](https://wiki.mythiccraft.io/mythicmobs/skills/mechanics/setvariable)
- Dùng `Variables` trên mob để xem giá trị lúc khởi tạo. Trong phân tích case, ghi nơi khởi tạo, nơi đọc/ghi, điều kiện reset, và giá trị dự kiến khi thiếu biến. `variableEquals` dùng để kiểm tra giá trị. [Mob Variables](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#mob-variables), [VariableEquals](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableequals)
- **5.10.0** bổ sung nhiều kiểu, trong đó có `Set`, `List`, `Map`, `Boolean` và `Vector`, cùng cú pháp chuỗi meta placeholder. Khi nghiên cứu file dùng kiểu nâng cao, kiểm tra mechanic cụ thể có hỗ trợ thao tác đó trên kiểu đã chọn. [Changelog 5.10.0 mục Variables](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs?version_id=d7c47c878837c833a7602dcf02bca7b9b87056dd), [Variable Types](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-types)

Một ca thử trạng thái nên có hai mob cùng loại hoạt động đồng thời, một lượt cast mới sau khi lượt trước kết thúc, và một lần reset. Nếu dùng scope `TARGET`, thêm hai người chơi và hai caster cùng tác động. Đối chiếu giá trị quan sát được với vòng đời ở bảng trên. [Boss phases](../architecture/boss-phases.md)
