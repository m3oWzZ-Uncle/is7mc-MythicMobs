# Tích hợp MMOItems, MMOCore và MythicLib

**FACT · tài liệu.** Phoenix mô tả đăng ký custom skills qua MythicLib và dùng lại từ MMOCore hoặc MMOItems. Mẫu Sacred Ward dùng `mythicmobs-skill-id`. Lục Cốt có dạng `source: mythicmobs:…`. Kiểm tra build trước khi chọn dạng cấu hình. [Phoenix MythicMobs integration](https://docs.phoenixdevt.fr/mythiclib/skills/custom/mythic) · [MMOItems Skills](https://docs.phoenixdevt.fr/mmoitems/features/skills) · [Mẫu trong dữ liệu](../../patterns/cau-noi-mmocore-mythiclib.md)

Khi tích hợp, truy chuỗi **item/class → registry → metaskill → callback**. Ghi nơi đọc modifier, sở hữu mana/stamina, bắt đầu cooldown và xử lý lần cast thất bại. Lục Cốt có các modifier `mana`, `stamina`, `cooldown` trong cấu hình. Tên trường tự nó chưa xác nhận lúc trừ hoặc hồi tài nguyên. [Cấu hình Lục Cốt](../../../incoming/Tutien/luccotchivuong/lccv_mythiclib.yml#L1) · [Đối chiếu modifier](../../patterns/doi-chieu-hop-dong-modifier.md)
