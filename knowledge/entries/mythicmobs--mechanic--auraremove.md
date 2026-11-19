# auraremove

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `removeaura`, `removebuff`, `removedebuff`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/auraremove)

## Chức năng và cú pháp

**FACT · wiki.** Xóa aura hoặc số stack trên entity được chọn. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/auraremove)

Cú pháp đọc trong nguồn: `auraRemove{aura=...;stacks=...} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/auraremove#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| auraName | aura, b, buff, buffname, debuff, debuffname, n, name | — | default |
| stacks | s | — | Max stacks |

auraName chọn aura; stacks giới hạn số stack bị lấy. Việc chạy onEnd khi xóa phụ thuộc DoEndSkillOnTerminate của aura.

## Chọn target, condition và trigger

Chọn đúng entity đang giữ aura. Guard stack nếu cần tiêu hao một charge và kiểm tra onEnd trước khi dùng cho cleanup.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Lấy một stack khi dash. [Dòng YAML gốc](../../incoming/Tutien/xichhuyetphathienthuong/xichhuyetthienthuong_skill.yml#L100)

```yaml
  - auraremove{aura=XHPTT_SPEAR_CHARGE;stacks=1} @self
```

**FACT · YAML.** Xóa aura hai tay. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L78)

```yaml
  - auraRemove{aura=lccv_haitay} @caster
```

**INFERENCE.** Dash của Xích Huyết lấy một charge; Lục Cốt xóa aura cường hóa theo nhánh.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử stack bằng không, charge cuối, hai cast gần nhau và side effect của onEnd.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/conditional-skills.md)
