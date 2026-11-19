# signal

**Loại** `mechanic` · **Plugin** `mythicmobs` · **Alias** `sendsignal`

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/signal)

## Chức năng và cú pháp

**FACT · wiki.** Gửi signal tới Mythic mob được chọn để trigger nhận chạy. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/signal)

Cú pháp đọc trong nguồn: `signal{s=...} @targeter`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/signal#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| signal | s | — | ping |

signal là tên mà onSignal bên nhận cần khớp. Tên mặc định được nêu trong bảng.

## Chọn target, condition và trigger

Dùng @Children khi mỗi boss cần gửi cho add riêng, hoặc @Parent cho đường gửi về. Không cần quét toàn map nếu quan hệ đã có.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Phát Mid cho mob con. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L67)

```yaml
  - signal{s=Mid} @Children
```

**FACT · YAML.** Phát Rythme trong ultimate. [Dòng YAML gốc](../../incoming/no-model/MythicMobsCariMc/MythicMobs/packs/PixelBarrel%27s%20Hollow%20Woods%20Vol.2/Skills/Conductor_skills.yml#L204)

```yaml
  - signal{s=Rythme} @Children
```

**INFERENCE.** Conductor phát Mid và Rythme cho children; nhánh Lift đi ngược về boss qua các nguồn trong pack.

## Giới hạn và kiểm chứng

**INFERENCE.** Thử add spawn sau lần phát, trùng tên signal và hai boss cạnh nhau.

**Bằng chứng.** YAML Parsed trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/boss-phase-score-signal.md)
