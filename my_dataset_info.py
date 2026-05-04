from mmseg.datasets import BaseSegDataset
from mmseg.registry import DATASETS

@DATASETS.register_module()
class Polipi2class(BaseSegDataset):

    METAINFO = dict(
        classes=('polipi', 'no_polipi'),
        palette=[[0, 0, 0], [128, 128, 128]])

    def __init__(self, **kwargs):
        super().__init__(img_suffix='.png', seg_map_suffix='.png', **kwargs)