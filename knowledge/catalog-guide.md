# Tra cứu và nghiên cứu MythicMobs

[Catalog JSON](catalog.json) lập danh mục từ các bảng công khai của MythicCraft, gồm mechanic/meta mechanic, targeter, condition và ngữ cảnh xét, trigger, biến và scope, metaskill, thuộc tính, placeholder, AI và tích hợp. Bản chụp danh mục dùng MythicMobs 5.14.0 làm mốc phát hành. `version.confirmed` để trống cho các mục chưa có bằng chứng ở cấp tính năng. Plugin sở hữu là một phần của ID, vì cùng tên có thể tồn tại trong các registry khác nhau. [Nguồn và phiên bản](../docs/wiki/README.md)

Với cú pháp core, bắt đầu từ [MythicCraft Wiki – MythicMobs](https://wiki.mythiccraft.io/mythicmobs/home). Khi YAML gọi cả core và addon, đối chiếu từng mechanic hoặc condition theo plugin sở hữu. [Kết quả rà soát nguồn và ca Vạn Kiếm Quy Tông](../docs/wiki/doi-chieu-2026-11-14.md)

## Tra cứu

```powershell
python -X utf8 tools/kb.py search projectile --plugin mythicmobs
python -X utf8 tools/kb.py search "@ENO" --type targeter
python -X utf8 tools/kb.py search --gameplay multiplayer
python -X utf8 tools/kb.py search xichhuyetthienthuong_skill.yml
python -X utf8 tools/kb.py search state --plugin modelengine
python -X utf8 tools/kb.py search --status researched --limit 30
python -X utf8 tools/wiki_library.py search orbital
```

Tìm theo tên hoặc alias trước. Thêm `--plugin` và `--type` khi kết quả trùng tên. `--gameplay` dùng các tag đã gắn trong batch nghiên cứu, chẳng hạn `collision`, `timing`, `phase`, `cleanup` và `multiplayer`. Tìm theo đường dẫn YAML, tài liệu hoặc URL nguồn bằng đối số tìm kiếm. Kết quả `indexed` dẫn tới wiki. Kết quả `researched` dẫn tới tài liệu cục bộ. Với yêu cầu thiết kế, mở thêm đúng bài trong [mục lục pattern](patterns/README.md). Tra một ví dụ bằng file và dòng được dẫn, rồi mở thêm caller/callback khi cần.

`wiki_library.py` tra theo đường dẫn, tên trang, tiêu đề và alias từ catalog khi có đường dẫn khớp. Kết quả có `knowledge` từ đợt đối chiếu snapshot và `catalog_notes` từ các đợt nghiên cứu catalog. Hai nguồn lưu tiến độ riêng. [Thư viện wiki](../docs/wiki/thu-vien.md)

## Mức kiểm chứng

| Cấp | Bằng chứng cần có |
| --- | --- |
| Documented | URL chính thức xác nhận có mục. `scope=index` chỉ là xuất hiện trong danh mục. Trang mục đã đọc có hash riêng trong `research`. |
| YAML Parsed | Dòng ví dụ thuộc file có kết quả parse, đường dẫn và SHA-256. |
| Reference Checked | Có thêm cạnh ID đối chiếu trong bộ cài hoặc tên model khớp file. Xem `examples[].references` để biết cạnh nào đã đối chiếu. |
| Server Load Tested | Build, log nạp và kết quả xác nhận mục liên quan đã đăng ký trên môi trường đó. |
| Gameplay Verified | Build, kết quả mong đợi và quan sát thực tế trong game, kèm log, video hoặc hiện vật thử nghiệm cho ca cụ thể. |

Mức kiểm chứng của catalog mô tả phạm vi bằng chứng trên một hoặc nhiều ví dụ được liệt kê. Nó không mở rộng sang mọi biến thể, mọi build hoặc mọi thuộc tính trên trang. Giữ nhãn FACT, INFERENCE và PREFERENCE trong [Design Pattern Library](patterns/README.md). Đối với phiên bản, ghi mốc trong changelog ở mức thuộc tính/tính năng khi nó cụ thể hơn phiên bản của mục. [Quy trình thử](../tests/README.md)

## Tiếp tục nghiên cứu

1. Chạy `python -X utf8 tools/kb.py next --limit 24`. Đọc [checkpoint](research-checkpoint.json) và [tiến độ các batch](research-batches/README.md). Chọn tối đa 30 mục. Mở đúng các trang wiki và các file liên quan trong [chỉ mục dữ liệu](dataset-index.md).
2. Soạn JSON cho batch mới theo [batch 01](research-batches/01.json) hoặc [batch 02](research-batches/02.json). Ghi chức năng, cú pháp, cách chọn target/condition/trigger, cách dùng, rủi ro, các giá trị được xác nhận và đường dẫn YAML đã index. Nếu chưa có ví dụ đã parse, để `examples: []` và nêu điểm còn thiếu. Nếu một trang không truy cập được, giữ mục trong hàng chờ và ghi blocker của batch.
3. Chạy `python -X utf8 tools/publish_research.py knowledge/research-batches/03.json --cache <thu_muc_tam>`. Công cụ đọc trang chính thức, lấy danh sách thuộc tính/mặc định từ bảng của trang, kiểm tra hash dòng nguồn rồi cập nhật catalog, Markdown và checkpoint. Dùng `--offline` khi đã có đúng snapshot nguồn. Mỗi bảng mặc định giữ nguyên dữ liệu đã công bố, phần diễn giải và đánh đổi nằm trong ghi chú nghiên cứu.
4. Chạy `python -X utf8 tools/kb.py validate`. Để làm mới danh mục, chạy `python -X utf8 tools/build_catalog.py --cache <thu_muc_tam> --checked-on YYYY-MM-DD`. Catalog giữ kết quả đã hoàn thành khi URL/ID tương ứng vẫn khớp. Nếu nguồn đổi, công cụ dừng để tránh làm mất bằng chứng cũ.

Tự động hóa lo phần lấy danh mục, bảng thuộc tính, xuất tài liệu, truy vấn và kiểm tra. Việc phân tích hành vi và xác nhận tương thích vẫn dựa trên nội dung trang, dữ liệu thực tế và bằng chứng của từng batch.
