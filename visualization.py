import os
import matplotlib.pyplot as plt
import numpy as np
import SimpleITK as sitk




color_cycle = (
    "000000",  # white
    "42d4f4",  # blue
    "f032e6",  # pink
    "3cb44b",  # green
    "f58231",  # orange
    "4363d8",  # purple
    "e6194B",
    "911eb4",
    "ffe119",
    "bfef45",
    "f032e6",
    "000075",
    "9A6324",
    "808000",
    "800000",
    "469990",
)


def hex_to_rgb(hex: str):
    assert len(hex) == 6
    return tuple(int(hex[i:i + 2], 16) for i in (0, 2, 4))


def generate_overlay(input_image: np.ndarray, segmentation: np.ndarray, mapping: dict = None, color_cycle=color_cycle,
                     overlay_intensity=0.3):
    """
    image must be a color image, so last dimension must be 3. if image is grayscale, tile it first!
    Segmentation must be label map of same shape as image (w/o color channels)
    mapping can be label_id -> idx_in_cycle or None

    returned image is scaled to [0, 255]!!!
    """
    # assert len(image.shape) == len(segmentation.shape)
    # assert all([i == j for i, j in zip(image.shape, segmentation.shape)])

    # create a copy of image
    image = np.copy(input_image)

    if len(image.shape) == 2:
        image = np.tile(image[:, :, None], (1, 1, 3))
    elif len(image.shape) == 3:
        assert image.shape[2] == 3, 'if 3d image is given the last dimension must be the color channels ' \
                                    '(3 channels). Only 2D images are supported'

    else:
        raise RuntimeError("unexpected image shape. only 2D images and 2D images with color channels (color in "
                           "last dimension) are supported")

    # rescale image to [0, 255]
    image = image - image.min()
    image = image / image.max() * 255

    # create output

    if mapping is None:
        uniques = np.unique(segmentation)
        print(uniques)
        #mapping = {i: c for c, i in enumerate(uniques)}
        mapping = {c: c for i, c in enumerate(uniques)}
    
    segmentation_transed = segmentation[0,:,:]
    for l in mapping.keys():
        #imager =image[:,:,0]
        a = np.array(hex_to_rgb(color_cycle[mapping[l]]))
        image[segmentation_transed == l] += overlay_intensity * a

    # rescale result to [0, 255]
    image = image / image.max() * 255
    return image.astype(np.uint8)


def plot_overlay(image_file: str, segmentation_file: str, output_file: str, overlay_intensity: float = 0.4):
    image = three_channels(image_file)
    seg = sitk.GetArrayFromImage(sitk.ReadImage(segmentation_file))
    assert len(image.shape) == 3, 'only 3D images/segs are supported'
    overlay = generate_overlay(image, seg, overlay_intensity=overlay_intensity)
    plt.imsave(output_file, overlay)


def three_channels(image_path0):
    image_path1 = image_path0.replace('0000','0001')
    image_path2 = image_path0.replace('0000', '0002')
    channel_r = sitk.GetArrayFromImage(sitk.ReadImage(image_path0)).transpose(1,2,0)
    channel_g = sitk.GetArrayFromImage(sitk.ReadImage(image_path1)).transpose(1,2,0)
    channel_b = sitk.GetArrayFromImage(sitk.ReadImage(image_path2)).transpose(1,2,0)
    merged_channels = np.concatenate((channel_r, channel_g, channel_b),axis=2)
    return merged_channels


def file_list(label_dir, image_dir):
    segs_path = []
    images_0_path = []
    segmentations = os.listdir(label_dir)
    for segmentation in segmentations:
        segmentation_path = os.path.join(label_dir, segmentation)
        image_0 = segmentation.replace('.nii.gz', '_0000.nii.gz')
        image_0_path = os.path.join(image_dir, image_0)
        segs_path.append(segmentation_path)
        images_0_path.append(image_0_path)
    return segs_path,images_0_path

out_dir = '/nvme/data/visualizations'
label_dir = '/nvme/data/ts_label'
image_dir = '/nvme/data/ts_image'

if __name__ == '__main__':
    seg_path, img_path = file_list(label_dir, image_dir)
    for idx, (spath, ipath) in enumerate(zip(seg_path,img_path)):
        out_name = spath.split('/')[-1].replace('.nii.gz', '.png')
        out_path = os.path.join(out_dir, out_name)
        plot_overlay(ipath, spath, out_path)
