import os
import os.path
import numpy as np

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
parent_path  = os.path.dirname(ROOT_DIR)
IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]
def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def dataloader(filepath):
    images = []
    lidars = []
    depths = []

    temp = filepath
    filepathi = temp + '/run/media/sssssy/File/Repositories/data/KITTI-raw/'
    filepathl = temp + '/run/media/sssssy/File/Repositories/data/KITTI/train/'
    filepathd = temp + '/run/media/sssssy/File/Repositories/data/KITTI/train/'
    filepathgt = temp + '/run/media/sssssy/File/Repositories/data/KITTI/train/'

    seqs = [seq for seq in os.listdir(filepathl) if seq.find('sync') > -1]
    left_fold = '/image_02/data'
    right_fold = '/image_03/data'
    lidar_foldl = '/proj_depth/velodyne_raw/image_02'
    lidar_foldr = '/proj_depth/velodyne_raw/image_03'
    depth_foldl = '/proj_depth/groundtruth/image_02'
    depth_foldr = '/proj_depth/groundtruth/image_03'

    for seq in seqs:
        temp = os.path.join(filepathgt, seq)

        imgsl = os.path.join(filepathi, seq[0:10], seq) + left_fold
        imagel = [os.path.join(imgsl, img) for img in os.listdir(imgsl)]
        imagel.sort()
        images = np.append(images, imagel)
        imgsr = os.path.join(filepathi, seq[0:10], seq) + right_fold
        imager = [os.path.join(imgsr, img) for img in os.listdir(imgsr)]
        imager.sort()
        images = np.append(images, imager)

        lids2l = os.path.join(filepathl, seq) + lidar_foldl
        lidar2l = [os.path.join(lids2l, lid) for lid in os.listdir(lids2l)]
        lidar2l.sort()
        lidars = np.append(lidars, lidar2l)
        lids2r = os.path.join(filepathl, seq) + lidar_foldr
        lidar2r = [os.path.join(lids2r, lid) for lid in os.listdir(lids2r)]
        lidar2r.sort()
        lidars = np.append(lidars, lidar2r)

        depsl = os.path.join(filepathd, seq) + depth_foldl
        depthl = [os.path.join(depsl, dep) for dep in os.listdir(depsl)]
        depthl.sort()
        depths = np.append(depths, depthl)
        depsr = os.path.join(filepathd, seq) + depth_foldr
        depthr = [os.path.join(depsr, dep) for dep in os.listdir(depsr)]
        depthr.sort()
        depths = np.append(depths, depthr)

        break

    left_train = images
    lidar2_train = lidars
    depth_train = depths

    return left_train,lidar2_train,depth_train

if __name__ == '__main__':
    datapath = ''

    for i in dataloader(datapath):
        print(i[0])


