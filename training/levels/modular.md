# Modular

Hợp đồng giữa module, tham số mặc định và hành vi khi lỗi. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 31 · Blood Pact

- **Gameplay.** Dùng một phần máu để lấy buff trong thời hạn.
- **Bắt buộc.** Chi phí trừ đúng một lần, giới hạn máu tối thiểu, buff thuộc caster. Luật cast thất bại và hết hạn minh bạch.
- **Tình huống biên.** Máu ngay ngưỡng, hai input đồng thời, người khác đang giữ buff.
- **Kiểm thử.** Ghi máu trước/sau khi đủ và thiếu. Kiểm buff chỉ có ở lượt trả chi phí hợp lệ.

## 32 · Spatial Rift

- **Gameplay.** Đặt khe không gian rồi kích hoạt transport ở lượt sau.
- **Bắt buộc.** Lưu hai đầu theo owner, giới hạn thời hạn và luật điểm đến an toàn. Chỉ đối tượng được phép đi qua.
- **Tình huống biên.** Đầu kia bị chặn, hai cặp khe giao, rời world.
- **Kiểm thử.** Đối chiếu chủ khe, tọa độ trước/sau và kết quả khi điểm thoát không hợp lệ.

## 33 · Adaptive Weapon Skill

- **Gameplay.** Cùng input đổi hành vi theo loại vũ khí đang dùng.
- **Bắt buộc.** Chọn đúng module từ vũ khí tại mốc đã nêu, có luật vũ khí không hỗ trợ, giữ nhất quán chi phí/cooldown.
- **Tình huống biên.** Đổi item khi chuẩn bị, item thiếu dữ liệu, hai người cùng dùng.
- **Kiểm thử.** Thử ba loại đã khai báo và một loại ngoài danh sách. Ghi module được gọi, damage và lần trừ chi phí.

## 34 · Reactive Combat

- **Gameplay.** Thực hiện callback theo sự kiện combat với thứ tự rõ ràng.
- **Bắt buộc.** Định nghĩa tối thiểu hai loại event và thứ tự modifier. Một callback không tự tạo vòng lặp hoặc kích hoạt trùng.
- **Tình huống biên.** Cùng tick có hai event, thêm/gỡ modifier, callback phát sinh hit mới.
- **Kiểm thử.** Ghi trace loại event, thứ tự và số lần chạy. Thử ca lồng event và player khác.

## 35 · Modular Spell System

- **Gameplay.** Dùng một hợp đồng cast cho ba spell có hành vi khác nhau.
- **Bắt buộc.** Định nghĩa input, defaults, kết quả, lỗi và người sở hữu tài nguyên. Lỗi một spell không phải sửa các spell còn lại.
- **Tình huống biên.** ID spell sai, thiếu modifier, thiếu tài nguyên hoặc hủy giữa warm-up.
- **Kiểm thử.** Chạy cả ba spell qua cùng entry. So lỗi đầu vào và chứng minh không trừ tài nguyên hai lần.
