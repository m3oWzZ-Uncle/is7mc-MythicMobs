# Đối chiếu tài liệu MythicMobs đã nhập

| Đợt | Phạm vi | Trang đã đọc |
| --- | --- | ---: |
| [01](01.json) | Changelog, Packs, inline condition, Math và projectile | 6 |
| [02](02.json) | Orbital, teleport, velocity, điểm neo, totem và aura component | 11 |
| [03](03.json) | Metaskill, variable scope, lifecycle, targeter, API và options | 10 |
| [04](04.json) | Damage, summon, owner, HasAura và API placeholder | 7 |

Đọc [checkpoint](checkpoint.json) hoặc chạy `python -X utf8 tools/wiki_library.py pending --topic Skills/Mechanics --limit 20`. Mỗi batch có tối đa 30 trang. Khi xong, thêm JSON với `checked_on` và `pages`. Mỗi mục ghi `path` tương đối từ snapshot, `official_url` đã đọc, `status`, `finding` có phạm vi cụ thể và `note` tương đối từ `knowledge/` nếu có. Đăng ký batch ở checkpoint rồi chạy `validate`.

`aligned` nghĩa là những điểm trong `finding` khớp. `differs` ghi khác biệt cụ thể. `outdated` ghi trang thiếu nội dung đã có bằng chứng phát hành mới hơn. `needs-verification` dùng khi bằng chứng chưa đủ để chốt điểm đối chiếu. `unchecked` là trang chưa có trong các đợt. Các trạng thái này thuộc đối chiếu tài liệu. Mức parse YAML, nạp server và gameplay tra theo hồ sơ riêng. [Quy ước xác minh](../catalog-guide.md#mức-kiểm-chứng)

- [Khác biệt theo phiên bản](version-gaps.md)
- [Kết hợp neo caster, vòng báo và projectile](../patterns/projectile-neo-caster.md)
- [Cách tìm bài và kiểm tra độ bao phủ](../../docs/wiki/thu-vien.md)
