# VariableInRange · điều kiện theo khoảng số

**Chức năng và cú pháp.** `variableinrange{var=caster.<tên>;value=1to16}` xét biến số trong khoảng. Dùng condition action hoặc inline condition theo ngữ cảnh của caller. [Wiki online](https://wiki.mythiccraft.io/mythicmobs/Skills/Conditions/variableinrange), [Markdown gốc](../../docs/wiki/MythicMobs/Skills/Conditions/variableinrange.md)

**Thuộc tính.** `variable` có alias `var`, `name`, `n`, `key`, `k`. Khoảng truyền vào `value` (`val`, `v`, `range`, `r`). Có thể chỉ định scope riêng. Wiki cũng ghi `<skill.var.index>` cho chỉ số mục tiêu, bắt đầu từ 0.

**Ví dụ và trường hợp dùng.** Vạn Kiếm dùng bước 1–16 để nâng, bước 16–111 để bắn. Hợp khi nhiều nhịp cần chia sẻ một bộ đếm. Nếu chỉ có một chuyển tiếp theo thời gian và ít nhánh, một `delay` hoặc callback aura có thể đủ. [Ví dụ YAML](../../examples/advanced/vankiemquytong-airborne/vkqt_skill.yml#L13), [VariableAdd](../entries/mythicmobs--meta-mechanic--variableadd.md)

**Lỗi thường gặp.** Quên khởi tạo biến số, dùng sai scope hoặc lặp tick ở mốc biên. Kiểm tra biên dưới, biên trên và cast đồng thời của hai caster.

**Phiên bản và xác minh.** `Documented`, ngày 14/11/2026. Chưa có bằng chứng gameplay cho bộ đếm dùng trong aura của ca này.
