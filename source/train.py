import argparse
import os

import torch
from dataloader import MapDrDataset
from torchvision.datasets import Cityscapes  # 添加此行以导入Cityscapes类
from torch.utils.data import DataLoader
from model import Model


if __name__ == '__main__':
    #1--外部参数解析
    parser = argparse.ArgumentParser(description="在线地图")
    parser.add_argument('--workspace_folder_path', type=str, default='/home/g/workspace/source/vector_map', help='工作路径')
    parser.add_argument('--dataset', type=str, default='MapDR-mini/mapdr_mini', help='数据集路径')
    args = parser.parse_args()
    dataset_folder_path = os.path.join(args.workspace_folder_path,"dataset",args.dataset)  
    #2--dataset创建
    map_dr_dataset=MapDrDataset(dataset_folder_path)
    #4--dataloader创建
    data_loader=DataLoader(dataset=map_dr_dataset, 
                    batch_size=1, 
                    shuffle=False, 
                    batch_sampler=None, 
                    num_workers=0, 
                    collate_fn=None,
                    pin_memory=False, 
                    drop_last=False)
    for index,data in enumerate(data_loader):
        print(f"uuid:{data[0]}")
    #5--模型创建及forward
    model=Model()
    input=torch.tensor(1.0)
    output = model(input)
    print(output)


