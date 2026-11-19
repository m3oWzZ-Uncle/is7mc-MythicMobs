# Gameplay

Luật mục tiêu, commitment và chính sách ngắt. [Chương trình và tiêu chuẩn bằng chứng](../curriculum.md)

## 16 · MOBA Dash Slash

- **Gameplay.** Player lướt về một đích đã chọn và chém sau khi dừng.
- **Bắt buộc.** Ra đòn kể cả khi đích né sau lúc lướt bắt đầu. Vùng chém tính ở nơi player thực sự dừng, timing đọc được.
- **Tình huống biên.** Tường cản, đích bước ngang, mục tiêu khác đi vào vùng chém.
- **Kiểm thử.** Quay mốc lướt và chém. So hụt, chạm tường và đòn trúng người đứng trong vùng mới.

## 17 · Martial Arts Combo

- **Gameplay.** Chuỗi 3 đòn gồm hai input thường và một nhánh lên gối với input thay thế.
- **Bắt buộc.** Công bố thứ tự input, cửa tiếp đòn và điều kiện hủy. Nhánh cuối không sinh thêm damage mặc định ngoài số hit quy định.
- **Tình huống biên.** Sai input, đổi mục tiêu giữa nhát, nhấn đúng ranh giới timeout.
- **Kiểm thử.** Chạy cả hai nhánh, xen kẽ input giữa hai player và kiểm đòn hụt không làm cast tiếp ngoài luật.

## 18 · Shadow Mark

- **Gameplay.** Đặt dấu riêng lên mục tiêu, lần đánh kế tiếp của chủ dấu kích nổ.
- **Bắt buộc.** Mỗi dấu có owner và hạn. Tiêu thụ đúng một dấu của người đánh, không kích dấu của player khác.
- **Tình huống biên.** Hai dấu trên một mob, chủ khác đánh, đích chết hoặc dấu hết hạn.
- **Kiểm thử.** A và B đặt dấu rồi đánh lần lượt. Ghi ID owner, thời điểm nổ và lần đánh khi đã hết dấu.

## 19 · Ice Prison

- **Gameplay.** Nhốt địch trong vùng băng tạm thời, đòn kết thúc giải phóng vùng.
- **Bắt buộc.** Cảnh báo và phạm vi rõ ràng. Đích hợp lệ bị giữ đúng thời lượng hoặc được giải phóng khi nhà tù vỡ. Phục hồi hành vi và dọn VFX.
- **Tình huống biên.** Đích giáp mép, đích đã có buff chậm, caster rời vùng.
- **Kiểm thử.** Thử trong/ngoài, chấm dứt sớm và hết hạn. Kiểm tra điều khiển trở lại và giữ buff ngoài skill.

## 20 · Time Rewind

- **Gameplay.** Quay về một snapshot gần đây của chính caster.
- **Bắt buộc.** Lưu/tua vị trí và hướng. Máu, inventory và trạng thái khác nằm ngoài ca. Đích snapshot phải an toàn và trong cùng world.
- **Tình huống biên.** Block mới chiếm vị trí cũ, đổi world, snapshot hết hạn, hai người cast.
- **Kiểm thử.** Ghi tọa độ và yaw trước/sau. Snapshot lỗi khiến người chơi ở nguyên chỗ; không dùng dữ liệu của player khác.
