# skill

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** `meta`, `metaskill`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill)

## Chức năng và cú pháp

**FACT · wiki.** Gọi metaskill theo ID, truyền ngữ cảnh target theo quy tắc kế thừa. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill)

Cú pháp đọc trong nguồn: `skill{s=ID} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/skill#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| skill | s, $, (), m, mechanics, meta, spell | — | — |
| forcesync | sync | — | false |
| branch | b, fork, f | — | false |
| executeafterdeath | continueafterdeath | — | false |
| snapshotcasterstats | snapshotstats, scs | — | false |

skill chọn ID; forcesync, branch, executeafterdeath và snapshotcasterstats lần lượt liên quan scheduler, cây con, việc gọi sau khi caster chết và dữ liệu stat chụp lại.

## Chọn target, condition và trigger

Gắn trigger ở điểm vào mob; giữ target kế thừa nếu child dùng cùng tập mục tiêu. Cố định targeter khi child cần ngữ cảnh khác.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Wave được gọi lặp bằng ID. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L15)

```yaml
  - skill{s=VKQT_WAVE;repeat=23;repeatInterval=10}
```

**FACT · YAML.** Damage được gọi theo mốc riêng. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L30)

```yaml
  - skill{s=lccv_danhthuong_Attack_DAMAGE;delay=18}
```

**INFERENCE.** Wave lặp ID, đòn tay dùng chung skill damage và gắn delay ở caller.

## Giới hạn và kiểm chứng

**INFERENCE.** Dò ID, target rỗng, branch và thứ tự callback. Đo khi cast đồng thời.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/multi-stage-skill.md)
