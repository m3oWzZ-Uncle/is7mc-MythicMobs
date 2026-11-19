# Thư viện wiki MythicMobs đã nhập

Nguồn là `E:/Ảnh Kỷ yếu Lớp 9/MythicMobs`, checkout từ GitLab wiki MythicCraft ở commit `db28fb6a7443aca1040ac29be76b840ff7d4d38f`, ngày 02/08/2026 UTC. Đã nhập nguyên byte **1.131 file trong 62 thư mục**, gồm **975 Markdown**, 114 GIF, 40 PNG, `.gitignore` và `.gitlab/redirects.yml`. Metadata thư mục `.git/` được giữ tại nguồn, với upstream và commit ghi trong chỉ mục. Hai file Tags cần giải mã CP1252 dự phòng khi lập chỉ mục, bản Markdown vẫn giữ nguyên byte. [Chỉ mục nhập](import-index.json), [Trang chính thức](https://wiki.mythiccraft.io/mythicmobs/home)

| Nhóm | Markdown |
| --- | ---: |
| Skills, gồm Mechanics 440, Conditions 196, Targeters 90, Triggers 37 và trang Variables | 787 |
| Mobs | 78 |
| Changelogs | 33 |
| Guides, Examples, Items và API | 29 |
| Root, config, drops, Enum, templates, Troubleshooting và tài liệu biên tập wiki | 48 |
| **Tổng** | **975** |

## Tra cứu

Chạy từ gốc kho Training với Python 3.12 trở lên. Công cụ dùng thư viện chuẩn.

```powershell
python -X utf8 tools/wiki_library.py search orbital --topic Skills/Mechanics
python -X utf8 tools/wiki_library.py search ENO
python -X utf8 tools/wiki_library.py search tickRate
python -X utf8 tools/wiki_library.py coverage
python -X utf8 tools/wiki_library.py audit-gaps
python -X utf8 tools/wiki_library.py pending --topic Skills/Conditions --limit 20
python -X utf8 tools/wiki_library.py validate
```

Mở kết quả `knowledge` hoặc `catalog_notes` để đọc phân tích, rồi dùng `sections` để mở đúng dòng trong bản chụp. `official_url` đến từ đợt đối chiếu hoặc catalog nếu khớp. `online_candidate` là URL suy ra từ đường dẫn snapshot, có thể cần tra redirect. Dùng `tools/kb.py search` để lọc plugin, cú pháp hoặc alias khi tên trùng nhau. [Hướng dẫn catalog](../../knowledge/catalog-guide.md)

Chỉ mục JSON lưu tên, chủ đề, đường dẫn tương đối, mục Markdown, SHA-256 và liên kết nội bộ theo từng file. Nguồn gốc mỗi file là thư mục trong `source` ghép với `path` của file. Liên kết có thể mang fragment, và kết quả kiểm đường dẫn chưa kiểm fragment trên server wiki. `audit-gaps` liệt kê liên kết nội bộ cần xem lại, các mục core thiếu đường dẫn khớp và trang snapshot không có bản ghi catalog trùng đường dẫn. Nhiều trang hướng dẫn và changelog nằm ngoài phạm vi catalog mục kỹ thuật.

## Độ bao phủ và phần khác biệt

Hiện có **34/975 trang** đã đối chiếu theo điểm cụ thể trong 4 batch. Có **26** trang khớp ở điểm đã xét, **5** có khác biệt và **3** thiếu nội dung mới hơn. **941** trang còn trong hàng chờ. Chỉ mục ghép được **1.210/1.221** mục catalog core theo đường dẫn. Danh sách 11 mục chưa khớp gồm `tickRate`, `@bound`, hai trigger vùng người chơi, `SetSulfurCubeArchetype` và sáu AI goal. Tra đúng tên các mục này sẽ trả trang online từ catalog. Các bài đã đối chiếu được truy xuất qua chỉ mục wiki và trường `knowledge`. Tiến độ chính của catalog vẫn theo `tools/kb.py`. [Báo cáo khác biệt](../../knowledge/wiki-research/version-gaps.md), [Tiến độ](../../knowledge/wiki-research/README.md)

Trong các đợt đầu, đã ghi khác biệt về pack overrides, `?@`, `Hidden` của metaskill, lọc cancel của OnDamaged, các tùy chọn damage và mở rộng `@Owner` cho dropped item. `hbcond` đã có trong snapshot và changelog xác nhận ở 5.13.0. [Changelog online](https://wiki.mythiccraft.io/mythicmobs/changelogs/Changelogs)

`audit-gaps` hiện có **67** tham chiếu chưa khớp file cục bộ. Chúng gồm đường dẫn GitLab cũ, ảnh hoặc ví dụ thiếu và một số đường dẫn kỹ thuật cần tìm redirect. Giữ đường dẫn gốc để có thể đối chiếu từng trường hợp. Việc thiếu file local cần bằng chứng online trước khi kết luận tài liệu đã bị gỡ.

`validate` kiểm lại file và thư mục so với manifest, SHA-256 và nguồn của các batch. Khi nhập lại cùng snapshot, công cụ kiểm tra xung đột trước khi sao chép, dùng lại bản trùng byte và dừng nếu file đích khác. Với revision khác, đối chiếu provenance trước khi cập nhật nguồn. [Checkpoint](../../knowledge/wiki-research/checkpoint.json)
