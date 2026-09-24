import colorsys

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont


def _generate_colors(n: int) -> list[tuple[int, int, int]]:
    """ラベル数に応じてHSV色空間から均等に色を生成する。"""
    colors = []
    for i in range(n):
        hue = i / max(n, 1)
        r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 0.9)
        colors.append((int(r * 255), int(g * 255), int(b * 255)))
    return colors


def draw_detections(
    image: Image.Image,
    results: list[dict],
    id2label: dict[int, str],
    line_width: int = 3,
    font_size: int = 16,
) -> Image.Image:
    """検出結果のバウンディングボックスとラベルを画像に描画する。"""
    draw_image = image.copy()
    draw = ImageDraw.Draw(draw_image)

    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except (OSError, IOError):
        font = ImageFont.load_default()

    # 検出されたラベルIDのユニーク値に色を割り当てる
    all_label_ids = sorted(
        {label_id.item() for r in results for label_id in r["labels"]}
    )
    colors = _generate_colors(len(all_label_ids))
    color_map = dict(zip(all_label_ids, colors))

    for result in results:
        for score, label_id, box in zip(
            result["scores"], result["labels"], result["boxes"]
        ):
            score_val = score.item()
            label = label_id.item()
            x1, y1, x2, y2 = box.tolist()
            color = color_map[label]
            label_text = f"{id2label[label]}: {score_val:.2f}"

            # バウンディングボックスの描画
            draw.rectangle([x1, y1, x2, y2], outline=color, width=line_width)

            # テキスト背景の描画
            text_bbox = draw.textbbox((0, 0), label_text, font=font)
            text_w = text_bbox[2] - text_bbox[0]
            text_h = text_bbox[3] - text_bbox[1]
            text_bg = [x1, y1 - text_h - 4, x1 + text_w + 4, y1]

            # テキスト背景が画像上端からはみ出す場合はボックス下に配置
            if text_bg[1] < 0:
                text_bg = [x1, y2, x1 + text_w + 4, y2 + text_h + 4]

            draw.rectangle(text_bg, fill=color)
            draw.text(
                (text_bg[0] + 2, text_bg[1] + 2),
                label_text,
                fill="white",
                font=font,
            )

    return draw_image


def show_detections(
    image: Image.Image,
    results: list[dict],
    id2label: dict[int, str],
    figsize: tuple[int, int] = (12, 8),
) -> None:
    """検出結果を画像に描画し、matplotlibで表示する。"""
    result_image = draw_detections(image, results, id2label)

    plt.figure(figsize=figsize)
    plt.imshow(result_image)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
