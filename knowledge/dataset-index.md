# Chỉ mục dữ liệu MythicMobs

Gói bổ sung ngày 15/11/2026 có 84 YAML. Xem [kiểm kê, đồ thị phụ thuộc và checkpoint IonTech](modular-design/README.md). Các số liệu bên dưới thuộc ảnh chụp cũ.

Ảnh chụp ngày 13/11/2026. Phạm vi là toàn bộ cây `incoming/`, gồm 158 thư mục con. [Báo cáo đợt 01](dataset-batch-01.md) phân tích đúng **30 YAML rời**. [Manifest kiểm kê](dataset-inventory.json) lưu đường dẫn, kích thước, SHA-256 và số mục trong mỗi archive. [Dữ liệu phân tích đợt 01](dataset-batch-01.json) lưu đúng 30 đường dẫn, ID, dòng nguồn, nhãn và các cạnh tham chiếu.

Tra cứu kỹ thuật đã rút từ đợt 01 qua [mục lục pattern theo nhu cầu](patterns/README.md).

## Tiến độ đến 14/11/2026

| Đợt | YAML rời | YAML trong archive | Nội dung |
| --- | ---: | ---: | --- |
| [01](dataset-batch-01.md) | 30 | 0 | Tu Tiên, Conductor, Assistant, Arctic và ví dụ cấu hình |
| [02](dataset-batch-02.md) | 12 | 0 | Cầu nối IgnisArctic và Soul Weaver |
| [03](dataset-batch-03.md) | 5 | 6 | Boss Wu và ba Armor Boss |
| **Tổng** | **47/214** | **6/1.961 lớp ngoài** | **53 YAML, 0 server-loaded, 0 verified-in-game** |

[Checkpoint dataset](dataset-checkpoint.json) lưu báo cáo, JSON từng đợt và các cụm tiếp theo. Mẫu số trong archive bao gồm entry lặp. Các số liệu phần đợt 01 giữ phạm vi của đợt đó.

## Kiểm kê toàn bộ cây

| Vị trí | File | YAML rời | Archive | BBModel rời | File khác |
| --- | ---: | ---: | ---: | ---: | ---: |
| `no-model/` | 225 | 206 | 4 | 2 | 13 |
| `Tutien/` | 18 | 8 | 0 | 10 | 0 |
| `MobsBoss/` | 31 | 0 | 31 | 0 | 0 |
| `SkillPacks/` | 44 | 0 | 44 | 0 | 0 |
| `OtherExamples/` | 66 | 0 | 66 | 0 | 0 |
| Gốc `incoming/` | 2 | 0 | 0 | 0 | 2 |
| **Tổng** | **386** | **214** | **145** | **12** | **15** |

145 archive gồm 132 ZIP, 9 RAR và 4 TAR.GZ. Đọc được mục lục lớp ngoài của cả 145 gói, tổng cộng **21.508 mục file**, trong đó 1.961 YAML, 1.236 BBModel, 8.896 PNG, 6.079 JSON, 1.786 OGG, 482 MCMETA và 6 schematic. Có 140 archive chứa YAML trực tiếp. 31 gói trong `MobsBoss/` có 175 mục YAML ở lớp ngoài. Các số này đếm từng mục theo gói và bao gồm các bản lặp. Còn 41 archive lồng (36 ZIP, 5 RAR) trong hàng chờ. Chưa mở nội dung YAML trong archive.

### Phân loại sơ bộ theo đường dẫn

| Loại đường dẫn | YAML rời | Mục YAML trong archive lớp ngoài |
| --- | ---: | ---: |
| MythicMobs mob | 42 | 258 |
| MythicMobs skill | 55 | 341 |
| MythicMobs item | 12 | 237 |
| MythicMobs config hoặc stats | 6 | 9 |
| Pack metadata | 7 | 39 |
| MythicLib | 12 | 160 |
| MMOCore class | 17 | 60 |
| MMOCore skill | 62 | 356 |
| MMOCore loại khác | 0 | 16 |
| Khác hoặc chưa rõ | 1 | 485 |
| **Tổng** | **214** | **1.961** |

Đây là số **file theo đường dẫn**, có thể đổi loại sau khi đọc nội dung. Ví dụ `lccv_backgroung.yml` chưa nhận diện được qua tên nhưng đợt 01 tìm thấy 9 metaskill. Số định nghĩa mob, boss, skill, mechanic và ID trùng toàn dataset sẽ tăng theo các đợt. Tên gói trong `MobsBoss/` là gợi ý chọn mẫu.

### Trùng nội dung

- Băm SHA-256 toàn bộ 386 file rời, gồm các archive dưới dạng file. Có **39 nhóm trùng byte, gồm 88 file**. Trong đó có **38 nhóm YAML, gồm 80 file**, và một nhóm TXT gồm 8 file. Các nhóm đầy đủ nằm tại khóa `duplicates` trong [manifest kiểm kê](dataset-inventory.json). Chưa băm riêng từng mục trong archive.
- Bốn bản `ArcticKnightMobs.yml` trùng byte. Bốn bản `ArcticKnight.yml` định nghĩa cùng 33 ID nhưng có ba SHA-256 khác nhau. Hai bản IgnisArctic và AllClass trùng byte. Bản tác giả và bản CaRiMC có khác biệt ở hai guard aura. [So sánh đợt 01](dataset-batch-01.md#arctic-knight)

## Kết quả đọc nội dung đợt 01

| Chỉ số | Kết quả |
| --- | ---: |
| YAML đã đọc và parse thành công | 30 |
| File khác SHA-256 trong đợt | 26 |
| Định nghĩa mob, kể cả mob hỗ trợ và VFX | 44 lượt / 41 ID |
| Boss chính nhận diện qua cấu trúc trận | 1, Conductor |
| Metaskill MythicMobs | 281 lượt / 182 ID |
| Đăng ký skill MythicLib | 7 |
| Cấu hình skill/class MMOCore | 4 skill / 1 class |
| Tên mechanic thấy trong YAML MythicMobs | 62 tên / 1.704 lượt |
| Nhóm ID lặp qua các bộ cài | 34, gồm 33 skill và 1 mob |
| Cạnh ID đối chiếu được trong cùng bộ cài | 606, gồm 206 giữa file và 400 nội bộ file |
| Cạnh ID chưa có đích trong đợt | 14 lượt / 11 ID |

ID được so không phân biệt hoa/thường để phát hiện khả năng đụng tên, giữ nguyên spelling và dòng gốc. Trong 30 file, 34 nhóm ID lặp đều nằm ở các bản Arctic thuộc những bộ cài khác nhau. Đây là rủi ro khi nạp chung. Không thấy khóa YAML lặp trong cùng mapping. Bộ đếm mechanic gộp hoa/thường, giữ alias đã viết như `sound` và `effect:sound` riêng, gồm cả bản sao và dòng inline nhận diện được. Các số cạnh là kết quả kiểm tra tĩnh của tham chiếu ID trực tiếp, callback, summon, mount, mob bullet, lệnh spawn cố định và cầu nối MMO trong đợt. Tham chiếu động, model và equipment cần đối chiếu riêng.

### Phiên bản, phụ thuộc và trạng thái

- `packinfo.yml` của Hollow Woods Vol.2 ghi **pack 1.0.0**. README trong `no-model/` ghi dữ liệu cũ từ 2023. Model Tu Tiên đã đọc ghi **Blockbench format 4.10**. Các mốc này chưa xác định build plugin. Một số mob VFX của Xích Huyết dùng `block_display`, loại entity có từ Minecraft Java 1.19.4. Mức hỗ trợ của MythicMobs/ModelEngine vẫn cần build thực tế. [Bản phát hành Minecraft 1.19.4](https://www.minecraft.net/en-us/article/minecraft-java-edition-1-19-4)
- Phụ thuộc được ghi theo nhóm và căn cứ trong [báo cáo đợt 01](dataset-batch-01.md). Tín hiệu chính gồm `model/state/submodel` cho ModelEngine, `mmodamage/mmoCanTarget` cho MythicLib, cấu hình class/skill cho MMOCore và `Disguise` của clone Arctic cho LibsDisguises. Chưa có log gắn build cho các YAML đã phân tích.
- Dùng nhãn yêu cầu `unknown`, `syntax-checked`, `load-tested`, `gameplay-verified`. Ba nhãn tương ứng của repo là `unverified` cho `unknown`, `server-loaded` cho `load-tested` và `verified-in-game` cho `gameplay-verified`. Đợt 01 có 30 `syntax-checked`, 0 `load-tested`, 0 `gameplay-verified`. **184 YAML rời** còn ở mức `unknown` về kiểm tra cú pháp. [Tiêu chí bằng chứng](../tests/README.md)

## Tiếp tục ở phiên Codex khác

1. Đọc [checkpoint](dataset-checkpoint.json). Đối chiếu cặp `path` + `sha256` trong `files` của từng JSON đợt với [manifest kiểm kê](dataset-inventory.json).
2. Chọn theo pack và lấy liền mob, skill, packinfo, item cần thiết. Mỗi đợt tối đa **30 YAML**, tính cả các entry archive đã đọc. Dùng `archive!entry` và hash nội dung entry. ZIP đọc trực tiếp được qua công cụ. RAR, TAR.GZ và archive lồng cần xử lý theo định dạng.
3. Tạo file selection JSON dạng `{ "scope-cua-pack": ["incoming/duong-dan.yml"] }` rồi chạy `python -X utf8 tools/index_dataset_batch.py <số-đợt> <selection.json>` với PyYAML. Công cụ trích từng định nghĩa và một tập cạnh literal. Đọc caller, điều kiện, targeter, biến và callback để phân tích luồng.
4. Lưu báo cáo và cập nhật checkpoint. Khi có log/video, gắn đúng file, hash, build, hành vi và kịch bản. [Mẫu hồ sơ](../incoming/TEMPLATE.md)
