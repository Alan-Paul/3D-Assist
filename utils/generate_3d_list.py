import os
import json
import argparse

def main(args):
    data_root = args.data_root
    save_list = args.save_list
    cams = ['1', '2', '3', '4', '5', '6']
    if not os.path.exists(save_list):
        os.mkdir(save_list)
    for cam in cams:
        ori_path = os.path.join(data_root, cam, 'ori')
        nb_path = os.path.join(data_root, cam, 'nb')
        id_dirs = sorted(os.listdir(ori_path))
        list_file = os.path.join(save_list, 'c%s_list.txt' % cam)
        print('generating list_file : %s' % list_file)
        if not os.path.exists(list_file):
            os.mknod(list_file)
        with open(list_file, 'w') as lf:
            for id_dir in id_dirs:
                pid = id_dir
                imgs = sorted(os.listdir(os.path.join(ori_path,id_dir)))
                img_path = os.path.join(ori_path, id_dir)
                nb_img_path = os.path.join(nb_path, '%s_r' % id_dir)
                for img in imgs:
                    cur_img_path = os.path.join(img_path, img)
                    cur_nb_img_path = os.path.join(nb_img_path, img)
                    img_info = '%s %s %s %s\n' % (pid, img, cur_img_path, cur_nb_img_path)
                    lf.write(img_info)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_root', type=str, default='/ssd4/ltb/datasets/PersonX', help='specify the data root')
    parser.add_argument('--save_list', type=str, default='/ssd4/ltb/datasets/PersonX/data_list')
    args = parser.parse_args()
    main(args)