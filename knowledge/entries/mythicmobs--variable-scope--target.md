# TARGET

**Loại** `variable-scope` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Tài liệu chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes)

## Chức năng và cú pháp

**FACT · wiki.** Định vị biến trên đối tượng đang được xử lý. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Variables#variable-scopes)

Cú pháp đọc trong nguồn: `var=target.name`.

## Thuộc tính và mặc định

Scope target được liệt kê trong bảng Variables. Đối tượng cụ thể tùy mechanic hoặc condition.

## Chọn target, condition và trigger

Dùng khi trạng thái thuộc người nhận. Định nghĩa rõ nhiều caster có chia sẻ cùng dấu hay không.

## Ví dụ và cách dùng khác nhau

Chưa có dòng ví dụ trong dataset đã phân tích.

**INFERENCE.** Đợt 01 dùng aura target cho miễn lặp. Biến TARGET là phương án nếu cần giá trị có kiểu.

## Giới hạn và kiểm chứng

**INFERENCE.** Chưa ghi nhận ví dụ TARGET đủ rõ trong batch. Thử hai caster cùng target trước khi dùng.

**Bằng chứng.** Documented trong phạm vi trang tài liệu. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/variable-scope.md)
