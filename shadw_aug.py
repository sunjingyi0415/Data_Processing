import math

import cv2 as cv
import numpy as np

PI = math.pi


def cart2poler(image, shadow_intensity=50, flag=cv.INTER_BITS2):
    h, w = image.shape[:2]
    circle_radius = int(h / 2)
    hp, wp = int(circle_radius / 1), int(2 * circle_radius * PI)
    center = (circle_radius, circle_radius)
    # polar_image = cv.warpPolar(image, (hp,wp), center, circle_radius, flag + cv.WARP_POLAR_LINEAR)

    mask = np.full((wp, hp, 3), 255, dtype=np.uint8)
    stripe_num = np.random.randint(1, 7)
    for i in range(stripe_num):
        stripe_start = np.random.randint(0, mask.shape[0])
        delta = np.random.randint(15, 35)
        mask[stripe_start:stripe_start + delta, :, 0] = shadow_intensity * 0.3
        mask[stripe_start:stripe_start + delta, :, 1] = shadow_intensity * 0.5
        mask[stripe_start:stripe_start + delta, :, 2] = shadow_intensity
    cv.imshow("shadow", mask)
    cv.waitKey()

    cs = min(h, w)
    # cart_image = cv.warpPolar(polar_image, (cs, cs), center, circle_radius, flag + cv.WARP_INVERSE_MAP)
    # cv.imshow("shadow", cart_image)
    # cv.waitKey()
    cart_mask = cv.warpPolar(mask, (cs, cs), center, circle_radius, flag + cv.WARP_INVERSE_MAP)
    cv.imshow("shadow", cart_mask)
    cv.waitKey()
    mask_shadow = cv.GaussianBlur(cart_mask, (3, 3), 0, cv.BORDER_REFLECT_101)
    cv.imshow("shadow", mask_shadow)
    cv.waitKey()
    mask_shadow = (mask_shadow - mask_shadow.min()) / (mask_shadow.max() - mask_shadow.min())
    hm, wm, cm = mask_shadow.shape
    if (hm, wm, cm) != image.shape:
        image = image[0:hm, 0:wm, :]
    masked_cart_image = image * mask_shadow
    cv.imshow("shadow", masked_cart_image)
    cv.waitKey()

    circle_mask = np.zeros_like(masked_cart_image)
    c_mask = cv.circle(circle_mask, center, circle_radius - 2, (1, 1, 1), -1)
    result = masked_cart_image * c_mask
    result = (result - result.min()) / (result.max() - result.min())
    return result


image = cv.imread(r'D:\first_set\tr_image\oct_27 Jul 2021 00-47-15_140.png')
res = cart2poler(image)
cv.imwrite(r"D:\oct\1.jpg", res)
cv.imshow("test", res)
cv.waitKey()
cv.destroyAllWindows()
