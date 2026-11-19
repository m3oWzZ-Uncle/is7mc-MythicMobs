# delay

**Loại** `meta-mechanic` · **Plugin** `mythicmobs` · **Alias** Chưa ghi alias trong chỉ mục.

**Nguồn đọc ngày 2026-11-13.** Mốc đối chiếu MythicMobs 5.14.0. Build tương thích của mục này chưa xác nhận riêng. [Wiki chính thức](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/delay)

## Chức năng và cú pháp

**FACT · wiki.** Dời phần kế tiếp của skill tree theo tick. [Trang mục](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/delay)

Cú pháp đọc trong nguồn: `delay 30`.

## Thuộc tính và mặc định

Các giá trị dưới đây là dữ liệu thuộc tính do wiki công bố. Dấu — biểu thị ô trống trong nguồn.

[Attributes](https://wiki.mythiccraft.io/mythicmobs/Skills/Mechanics/delay#attributes)

| Thuộc tính | Alias | Kiểu nếu có | Mặc định |
| --- | --- | --- | --- |
| ticks | — | — | 0 |

ticks có dạng positional hoặc trong braces và nhận placeholder theo wiki. Universal delay trên một dòng lên lịch cho dòng đó.

## Chọn target, condition và trigger

Đặt sau telegraph. Khi trạng thái có thể đổi trong lúc đợi, kiểm tra guard trong metaskill hit.

## Ví dụ và cách dùng khác nhau

**FACT · YAML.** Delay 30 tick trước wave. [Dòng YAML gốc](../../incoming/Tutien/kiemtuytong/vankiemquytong/vkqt_skill.yml#L12)

```yaml
  - delay 30
```

**FACT · YAML.** So sánh delay trên một dòng gọi skill. [Dòng YAML gốc](../../incoming/Tutien/luccotchivuong/lccv_skills.yml#L30)

```yaml
  - skill{s=lccv_danhthuong_Attack_DAMAGE;delay=18}
```

**INFERENCE.** Vạn Kiếm trì hoãn cả chuỗi trước wave. Lục Cốt lên lịch hit riêng với delay trên mechanic skill.

## Giới hạn và kiểm chứng

**INFERENCE.** Đo tick thực khi TPS thấp và thử hủy/đổi target trong wind-up.

**Bằng chứng.** Reference Checked trong phạm vi các ví dụ được liệt kê. Các ví dụ thuộc đợt YAML 01. Build, log nạp và gameplay vẫn cần xác minh. [Hồ sơ đợt YAML](../dataset-batch-01.md), [Quy ước kiểm chứng](../catalog-guide.md)

[Pattern liên quan](../patterns/dong-bo-animation-damage.md)
