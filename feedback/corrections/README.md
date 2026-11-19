# Ghi nhận lỗi và bản sửa

1. Ghi yêu cầu ban đầu, hành vi người dùng quan sát và điều họ muốn thay đổi. Giữ bản trước hoặc diff trong phạm vi cần sửa để còn đối chiếu. Với project khác, tạo bản sao hoặc diff trước khi sửa theo [quy tắc project](../../AGENTS.md).
2. Phân biệt nguyên nhân có bằng chứng và giả thuyết. Đề xuất và thực hiện bản sửa theo yêu cầu. Chạy các kiểm tra khả thi và đặt hồ sơ ở trạng thái chờ người dùng xác nhận kết quả. [Mẫu ghi nhận lỗi](TEMPLATE.md)
3. Sau khi người dùng xác nhận, ghi ngày và lời xác nhận. Lưu bản trước và bản sau hoặc tham chiếu tới hai phiên bản có thể mở lại. Dùng phần YAML cần thiết khi lưu bản sao trong hồ sơ. Nếu hành vi vẫn sai, giữ hồ sơ mở và ghi phần cần sửa tiếp.
4. Viết nguyên tắc có thể dùng lại trong phạm vi lỗi đã xác nhận và tạo ca hồi quy với các bước tái hiện, hành vi mong đợi và dấu hiệu lỗi cũ quay lại. Lưu ca trong `tests/` và liên kết hai chiều với hồ sơ. Cập nhật [hồ sơ tư duy](../../knowledge/learning-profile.md) nếu lời xác nhận còn cho thấy một tiêu chí thiết kế rõ ràng. [Mẫu ca hồi quy](../../tests/gameplay-regression-template.md)

Sự xác nhận của người dùng về bản sửa và bằng chứng kiểm thử kỹ thuật có trường riêng. Gắn trạng thái kỹ thuật theo đúng phiên bản và hành vi có bằng chứng. [Các cấp kiểm chứng](../../tests/README.md#trạng-thái-và-bằng-chứng)

## Hồ sơ hiện có

- [MM-2026-001](MM-2026-001.md) — Lỗi mã hóa đầu ra khi kiểm tra YAML trên Windows.
- [MM-2026-002](MM-2026-002.md) — Tham chiếu chưa tìm thấy trong bộ Conductor ở phạm vi đợt 01.
- [MM-2026-003](MM-2026-003.md) — Câu hỏi đã giải quyết vẫn hiện khi tra quyết định. Bản sửa đã qua kiểm thử CLI.
- [MM-2026-004](MM-2026-004.md) — Trigger Deprivation của Soul Weaver cần xác minh trên bộ cài gốc.
- [MM-2026-005](MM-2026-005.md) — Vạn Kiếm Quy Tông nâng caster và rải kiếm. Chờ chạy server.
- [MM-2026-006](MM-2026-006.md) — Guard dư, hướng lướt và đòn chém khi hụt trong Dash Cleave. Chờ kiểm thử bản sửa.
- [MM-2026-007](MM-2026-007.md) — Trùng ID VFX trong bản nhập IonTech. Đã đối chiếu khai báo tĩnh.
- [MM-2026-008](MM-2026-008.md) — Hiệu ứng vanilla của Vampire Slash cần vệt chém và phản hồi rõ hơn. Chờ thử bản r2.
