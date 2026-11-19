# Passive Skills

**FACT · cấu hình.** Holy Cry có trường `passive-type: TIMER` trong bộ dữ liệu. Lục Cốt khai báo `trigger: TIMER` ở registry MythicLib. Hai cấu hình cho thấy cần truy plugin sở hữu timer và ID trước khi diễn giải tần suất hoặc vòng đời. [Holy Cry](../../patterns/cau-noi-mmocore-mythiclib.md#thành-phần) · [Registry Lục Cốt](../../../incoming/Tutien/luccotchivuong/lccv_mythiclib.yml#L41)

Chọn sự kiện nếu hiệu ứng chỉ cần phản ứng với sự kiện đó. Với buff trạng thái, xác định ai giữ aura, cách làm mới và thời điểm hết hiệu lực từ yêu cầu. Chỉ dùng kiểm tra định kỳ khi hành vi cần cập nhật theo thời gian. Nếu có timer hoặc aura dài, thử mất điều kiện, thay đổi trang bị hoặc nhiều người cùng kích hoạt theo đúng vòng đời của caller. [MMOCore Skill Configuration](https://docs.phoenixdevt.fr/mmocore/skills/config.html) · [Aura](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/aura) · [Chi phí timer](../../patterns/toi-uu-timer-va-callback.md)
