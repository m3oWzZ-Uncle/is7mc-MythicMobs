# RPG

Mục tiêu chọn trước, tài nguyên, cửa sổ combo và sự kiện phản công. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 06 · Thunder Strike

- **Gameplay.** Đánh sét vào điểm người chơi ngắm sau một cảnh báo nhìn thấy.
- **Bắt buộc.** Điểm cảnh báo giữ nguyên trong thời gian chờ, damage tại mốc đánh. Không để sét trang trí tạo nguồn damage thứ hai hoặc cháy địa hình.
- **Tình huống biên.** Quay đi giữa cast, đích rời điểm, sàn nhiều tầng.
- **Kiểm thử.** Đánh dấu điểm ban đầu. Chỉ đích trong vùng ở mốc sét mất máu một lần. So máu trước cảnh báo và sau va chạm.

## 07 · Vampire Slash

- **Gameplay.** Chém cận chiến và hồi máu nếu gây sát thương thực.
- **Bắt buộc.** Tính hồi theo damage thực của mục tiêu chính với trần ghi rõ. Hụt hoặc hit bị chặn không hồi, không vượt max health.
- **Tình huống biên.** Đích có giáp, miễn damage, chết bởi hit, caster gần đầy máu.
- **Kiểm thử.** So hai đích có mitigation khác nhau và một lần hụt. Ghi damage, máu hồi và số callback.

## 08 · Hàn Băng Địa Mạch

- **Gameplay.** Player phóng luồng băng bám sàn. Vệt ICE, bụi xanh và mảnh băng bám theo đường đi thực tế.
- **Bắt buộc.** Projectile chạy thẳng theo yaw lúc cast, khoảng 2 block/giây trong 10–15 block. Tách va chạm tường khỏi hết tầm. Mỗi mob nhận damage một lần mỗi cast, stun 80 tick và có hai tầng khối băng hiển thị quanh thân. Mask và VFX có hạn, các lượt cast có dữ liệu riêng.
- **Tình huống biên.** Bậc thấp, vực, tường đứng, mob theo luồng, đích khác cỡ, hai caster và mask chồng nhau.
- **Kiểm thử.** Đo theo mốc sàn, đếm hit và callback tường, kiểm gỡ stun, giới hạn khối VFX và khôi phục mask. [Ca 026](../../tests/training-sandbox/026-curriculum-frost-ground-surge/README.md)

## 09 · Gravity Pull

- **Gameplay.** Hút nhiều mục tiêu về một tâm cố định rồi kết thúc.
- **Bắt buộc.** Báo tâm, kéo theo hướng về tâm và có giới hạn vùng. Caster và người ngoài vùng không bị hút.
- **Tình huống biên.** Đích ở tâm, tường giữa hai bên, đích bước ra trước khi kéo.
- **Kiểm thử.** Đặt đích từ bốn hướng và một đích ngoài vùng. So vector dịch chuyển và không có kéo tiếp sau khi kết thúc.

## 10 · Counter Attack

- **Gameplay.** Vào thế thủ ngắn, phản đúng kẻ gây đòn cận chiến hợp lệ đầu tiên.
- **Bắt buộc.** Consume một lượt phản công. Đòn thứ hai, projectile hoặc môi trường không sinh thêm phản công.
- **Tình huống biên.** Hai attacker gần đồng thời, đứng cạnh nhưng không đánh, hết cửa sổ.
- **Kiểm thử.** Đếm số phản công và đúng danh tính attacker. Thử đối chứng bằng cung và đòn sau timeout.

## Đề 08 trước khi thay thế · Triple Sword Combo

- **Gameplay.** Ba nhát kiếm dành cho ba input nối đòn.
- **Bắt buộc.** Mỗi input hợp lệ tạo đúng một nhát, cửa sổ nối hữu hạn. Nhát 3 kết thúc chuỗi, lần sau bắt đầu nhát 1.
- **Tình huống biên.** Input tới trễ, spam, luân phiên hai player, hụt ở nhát 2.
- **Kiểm thử.** Quay 1→2→3, làm lại sau timeout và thử hai người bấm xen kẽ. So kiểu nhát và mốc damage.
