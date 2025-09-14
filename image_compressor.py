import cv2
from tkinter import Tk, filedialog
import os

def compress_image(image_path, quality):
    img = cv2.imread(image_path)
    filename, ext = os.path.splitext(image_path)
    output_file = f"{filename}_compressed.png"

    cv2.imwrite(output_file, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    print(f"تصویر ذخیره شد و در اینجا ذخیره شد {output_file}")

    cv2.imshow("Original Image", cv2.imread(image_path))
    cv2.imshow("Compressed Image", cv2.imread(output_file))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

Tk().withdraw()
file_path = filedialog.askopenfilename(title="انتخاب تصویر")

if file_path:
    quality = int(input("درصد کیفیت را مشخص کنید (مثلا 60%)"))
    compress_image(file_path, quality)
else:
    print("هیچ فایلی انتخاب نشد")