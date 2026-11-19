# Expert

Ngân sách callback, điều phối trạng thái và test tải. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 36 · Fractal Sword Array

- **Gameplay.** Một kiếm chia nhánh qua hữu hạn thế hệ.
- **Bắt buộc.** Công bố độ sâu, giới hạn tổng, giới hạn per caster và hành vi kết thúc. Không đặt block hoặc dùng recursion không chặn.
- **Tình huống biên.** Đụng nhiều đích trong một tick, hai caster, cha bị ngắt.
- **Kiểm thử.** Đếm mọi lượt sinh theo cây, đối chiếu ngân sách có thể tái hiện và kiểm còn đạn sau timeout.

## 37 · Dynamic Skill Graph

- **Gameplay.** Điều hướng các bước skill theo input và sự kiện tại runtime.
- **Bắt buộc.** Định nghĩa node, cạnh hợp lệ, điều kiện kết thúc và giới hạn số chuyển. Lỗi ID hoặc callback có đường kết thúc quan sát được.
- **Tình huống biên.** Cạnh quay lại, sự kiện lặp, node không tồn tại, hai graph đồng thời.
- **Kiểm thử.** Chạy hai đường hợp lệ, một đường lỗi và vòng được giới hạn. Ghi trace để đối chiếu số bước.

## 38 · Orbital Combat System

- **Gameplay.** Các kiếm orbit có thể phòng thủ hoặc được phóng theo lệnh.
- **Bắt buộc.** Giữ số slot, quyền sở hữu và quy tắc chuyển từ orbit sang đạn. Chỉ đếm mỗi slot một lần, có giới hạn theo caster.
- **Tình huống biên.** Lệnh phóng đồng thời lúc bị hit, hết thời gian, hai chủ đứng sát.
- **Kiểm thử.** Đối chiếu số model, slot và đạn trước/sau. Đo hit trong hai chế độ và kiểm dọn tất cả callback.

## 39 · Thần Thông Vạn Biến

- **Gameplay.** Một entry đổi bộ kỹ năng từ ba thế đã định.
- **Bắt buộc.** Mỗi thế có dấu hiệu và tài nguyên riêng hoặc dùng chung theo quy ước. Chuyển thế trong lúc cast tuân luật commitment công bố.
- **Tình huống biên.** Đổi thế lúc callback, hai input cạnh nhau, trạng thái thiếu sau reload.
- **Kiểm thử.** Chạy từng thế và từng chuyển thế. So caster, modifier, tài nguyên và nguồn hiệu ứng.

## 40 · Ultimate Tu Tiên Skill

- **Gameplay.** Kết hợp chuẩn bị, chuyển động, model, va chạm và kết thúc trong một chiêu cuối player.
- **Bắt buộc.** Có mốc quan sát được, ngân sách projectile/VFX, luật ngắt và dọn đúng chủ. Giải thích vai trò cụ thể của từng module.
- **Tình huống biên.** Trần/tường, mục tiêu né, asset lỗi, hai caster và rời arena giữa chừng.
- **Kiểm thử.** Quay đủ timeline, đối chiếu số hit và entity. Chạy hai caster và ghi tải theo cùng điều kiện với ca chuẩn.
