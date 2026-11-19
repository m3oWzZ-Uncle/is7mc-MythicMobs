# Kiểm thử

Các cấp kiểm chứng của catalog và yêu cầu bằng chứng ở cấp mục nằm trong [hướng dẫn catalog](../knowledge/catalog-guide.md#mức-kiểm-chứng).

Sau khi người dùng xác nhận một bản sửa, tạo ca theo [mẫu hồi quy gameplay](gameplay-regression-template.md) và liên kết với [hồ sơ lỗi](../feedback/corrections/README.md).

[Sandbox thực hành](training-sandbox/README.md) lưu bài, lệnh kiểm thử Minecraft, hồ sơ theo build và mốc đánh giá. Dùng `python -X utf8 tools/training.py status` để tìm bài cần tiếp tục.

## Hồi quy bộ nhớ dài hạn

Chạy `python -B -X utf8 -m unittest discover -s tests -p test_memory.py -v` từ thư mục repo. Bộ test dùng hồ sơ giả lập trong thư mục tạm để kiểm tra tìm câu hỏi đã trả lời, áp dụng theo điều kiện, cô lập project, phát hiện mâu thuẫn, giữ mức tin cậy của suy luận, tìm lỗi cũ và quyết định lúc cần hỏi. Dữ liệu kiểm thử không được tính vào báo cáo sử dụng thực tế. [Quy trình bộ nhớ](../memory/README.md)

Trong một phiên Codex mới, dùng `mythicmobs-expert` với một tình huống tương tự. Kiểm tra phiên mới có tự tìm nguồn, áp dụng đúng quy tắc trong phạm vi, giữ nguyên các điểm đang chờ xác nhận và tránh hỏi lại phần đã rõ.

Ca `test_cli_round_trip_in_separate_processes_and_cleanup` dùng `tools/memory.py --root <thư-mục-tạm>` để tạo và đọc lại một quyết định bằng các tiến trình riêng. Ca thử kiểm tra cả project khác và xác nhận thư mục tạm đã được xóa.

## Trạng thái và bằng chứng

| Trạng thái | Bằng chứng tối thiểu |
| --- | --- |
| `unverified` | Chưa có kết quả parse hoặc bằng chứng server cho bản YAML đang xét. Có thể đã đối chiếu wiki. |
| `syntax-checked` | Parser YAML đọc được các file đã ghi trong hồ sơ. Kiểm tra ID được gọi và phụ thuộc riêng. |
| `server-loaded` | Log nạp trên build đã ghi, cùng bằng chứng các định nghĩa liên quan đã đăng ký. Xem warning theo file, ID và dependency. |
| `verified-in-game` | Bước tái hiện, kết quả quan sát đạt kỳ vọng và bằng chứng trên build đã ghi. Gắn theo đúng hành vi, kịch bản và bản YAML đã thử. |

## Quy trình trên bản sao server

1. Từ thư mục repo chạy `python -m pip install PyYAML` nếu Python đang dùng thiếu PyYAML, rồi chạy `python -X utf8 tests/check_yaml.py <thư_mục_hoặc_file>`. Nếu hệ thống dùng lệnh `python3`, dùng cùng lệnh đó ở cả hai bước. Lưu đầu ra của lần chạy. Script kiểm tra parse YAML. Việc kiểm tra ID, option và gameplay thực hiện riêng.
2. Đặt file vào các thư mục `Mobs`, `Skills` hoặc cấu trúc pack tương ứng trên bản sao server. Khởi động với đúng plugin/addon hoặc dùng `/mm reload` khi thử cập nhật cấu hình MythicMobs, giữ đoạn log liên quan. Dùng `/mm mobs list` để kiểm tra ID mob. Xác nhận riêng các skill và phụ thuộc qua log/định nghĩa được nạp nếu có. [Files and Directories](https://wiki.mythiccraft.io/mythicmobs/Guides/%28Step-2%29-Files-And-Directories), [Commands and Permissions](https://wiki.mythiccraft.io/mythicmobs/Commands-and-Permissions)
3. Spawn mob thử bằng `/mm mobs spawn <ID_mob>` từ người chơi có quyền. Kích hoạt bằng thao tác thực tế như click, đánh hoặc chờ timer theo case. Ghi ai bị tác động, số lần chạy và timing. Với combat, chạy thêm trường hợp hụt, đổi target, chết/despawn giữa cast và hai người chơi. [Essential Commands](https://wiki.mythiccraft.io/mythicmobs/Guides/%28Step-4%29-Essential-Commands), [Triggers](https://wiki.mythiccraft.io/mythicmobs/Skills/Triggers)
4. Lưu kết quả và bằng chứng vào hồ sơ case. Với boss, dùng [ma trận chuyển phase](../knowledge/architecture/boss-phases.md#ma-trận-thử-trên-server). Với phép đo tải, dùng [quy trình hiệu năng](../knowledge/architecture/performance.md).
