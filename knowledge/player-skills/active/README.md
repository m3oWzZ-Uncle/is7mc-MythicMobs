# Active Skills

**FACT · cấu hình.** Sacred Ward có đường gọi từ class qua một đăng ký MythicLib đến metaskill MythicMobs. Nhánh active nhận modifier và tách buff caster khỏi chọn người hỗ trợ trong vùng. [Mẫu Sacred Ward và đường dẫn YAML](../../patterns/cau-noi-mmocore-mythiclib.md)

Tìm caller sở hữu thao tác cast trước khi thêm trigger. Đối với utility chỉ thao tác lên người cast, chọn caster trực tiếp. Nếu utility chọn đồng đội, xác định vùng và chính sách đồng đội trong build mục tiêu. Khi có nhiều lớp cooldown, thử cả một lượt thành công và một lượt bị từ chối tại điểm vào thật. [Điểm vào MMO](../integrations/README.md) · [Metaskills](https://wiki.mythiccraft.io/mythicmobs/Skills/Metaskills)
