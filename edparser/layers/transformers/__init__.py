# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2019-12-29 15:17
# mute transformers
import logging

logging.getLogger('transformers.file_utils').setLevel(logging.ERROR)
logging.getLogger('transformers.filelock').setLevel(logging.ERROR)
logging.getLogger('transformers.tokenization_utils').setLevel(logging.ERROR)
logging.getLogger('transformers.configuration_utils').setLevel(logging.ERROR)
logging.getLogger('transformers.modeling_tf_utils').setLevel(logging.ERROR)
logging.getLogger('transformers.modeling_utils').setLevel(logging.ERROR)

zh_albert_models_google = {
    'albert_base_zh': 'https://storage.googleapis.com/albert_models/albert_base_zh.tar.gz',
    'albert_large_zh': 'https://storage.googleapis.com/albert_models/albert_large_zh.tar.gz',
    'albert_xlarge_zh': 'https://storage.googleapis.com/albert_models/albert_xlarge_zh.tar.gz',
    'albert_xxlarge_zh': 'https://storage.googleapis.com/albert_models/albert_xxlarge_zh.tar.gz',
}
