import os
import urllib
import torch
from torch.utils import model_zoo


class CheckpointIO(object):
    def __init__(self, checkpoint_dir='./chkpts', **kwargs):
        self.module_dict = kwargs
        self.checkpoint_dir = checkpoint_dir

        if not os.path.exists(checkpoint_dir):
            os.makedirs(checkpoint_dir)

    def register_modules(self, **kwargs):
        self.module_dict.update(kwargs)

    def save(self, filename, **kwargs):
        filename = os.path.join(self.checkpoint_dir, filename)

        outdict = kwargs
        for k, v in self.module_dict.items():
            outdict[k] = v.state_dict()
        torch.save(outdict, filename)

    def load(self, filename):
        '''Loads a module dictionary from local file or url.
        
        Args:
            filename (str): name of saved module dictionary
        '''
        print(filename)
        if is_url(filename):
            return self.load_url(filename)
        else:
            return self.load_file(filename)

    def load_url(self, url):
        '''Load a module dictionary from url.
        
        Args:
            url (str): url to saved model
        '''
        print(url)
        print('=> Loading checkpoint from url...')
        out_dict = model_zoo.load_url(url, progress=True)
        filename = os.path.join(self.checkpoint_dir, 'model.pt')
        out_file_dict = torch.load(filename)

        print(out_file_dict["model_g"]["geometry_encoder.fc_pos.weight"].size(), out_dict["model"]["encoder.fc_pos.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.fc_pos.bias"].size(), out_dict["model"]["encoder.fc_pos.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_0.fc_0.weight"].size(), out_dict["model"]["encoder.block_0.fc_0.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_0.fc_0.bias"].size(), out_dict["model"]["encoder.block_0.fc_0.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_0.fc_1.weight"].size(), out_dict["model"]["encoder.block_0.fc_1.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_0.fc_1.bias"].size(), out_dict["model"]["encoder.block_0.fc_1.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_0.shortcut.weight"].size(), out_dict["model"]["encoder.block_0.shortcut.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_1.fc_0.weight"].size(), out_dict["model"]["encoder.block_1.fc_0.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_1.fc_0.bias"].size(), out_dict["model"]["encoder.block_1.fc_0.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_1.fc_1.weight"].size(), out_dict["model"]["encoder.block_1.fc_1.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_1.fc_1.bias"].size(), out_dict["model"]["encoder.block_1.fc_1.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_1.shortcut.weight"].size(), out_dict["model"]["encoder.block_1.shortcut.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_2.fc_0.weight"].size(), out_dict["model"]["encoder.block_2.fc_0.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_2.fc_0.bias"].size(), out_dict["model"]["encoder.block_2.fc_0.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_2.fc_1.weight"].size(), out_dict["model"]["encoder.block_2.fc_1.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_2.fc_1.bias"].size(), out_dict["model"]["encoder.block_2.fc_1.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_2.shortcut.weight"].size(), out_dict["model"]["encoder.block_2.shortcut.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_3.fc_0.weight"].size(), out_dict["model"]["encoder.block_3.fc_0.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_3.fc_0.bias"].size(), out_dict["model"]["encoder.block_3.fc_0.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_3.fc_1.weight"].size(), out_dict["model"]["encoder.block_3.fc_1.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_3.fc_1.bias"].size(), out_dict["model"]["encoder.block_3.fc_1.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_3.shortcut.weight"].size(), out_dict["model"]["encoder.block_3.shortcut.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_4.fc_0.weight"].size(), out_dict["model"]["encoder.block_4.fc_0.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_4.fc_0.bias"].size(), out_dict["model"]["encoder.block_4.fc_0.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_4.fc_1.weight"].size(), out_dict["model"]["encoder.block_4.fc_1.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_4.fc_1.bias"].size(), out_dict["model"]["encoder.block_4.fc_1.bias"].size())
        print(out_file_dict["model_g"]["geometry_encoder.block_4.shortcut.weight"].size(), out_dict["model"]["encoder.block_4.shortcut.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.fc_c.weight"].size(), out_dict["model"]["encoder.fc_c.weight"].size())
        print(out_file_dict["model_g"]["geometry_encoder.fc_c.bias"].size(), out_dict["model"]["encoder.fc_c.bias"].size())

        # scalars = self.parse_state_dict(state_dict)
        for k, v in self.module_dict.items():
            print("Start loading: %s" % k)
            if k in out_file_dict:
                # print(out_dict[k])
                v.load_state_dict(out_file_dict[k])
                print("Finished: %s" % k)
            else:
                print('Warning: Could not find %s in checkpoint!' % k)
        scalars = {k: v for k, v in out_file_dict.items()
                    if k not in self.module_dict}
        return scalars

    def load_file(self, filename):
        filename = os.path.join(self.checkpoint_dir, filename)

        if os.path.exists(filename):

            print('=> Loading checkpoint...')
            out_dict = torch.load(filename)
            for k, v in self.module_dict.items():
                print("Start loading: %s" % k)
                if k in out_dict:
                    # print(out_dict[k])
                    v.load_state_dict(out_dict[k])
                    print("Finished: %s" % k)
                else:
                    print('Warning: Could not find %s in checkpoint!' % k)
            scalars = {k: v for k, v in out_dict.items()
                       if k not in self.module_dict}
            return scalars
        else:
            raise FileExistsError

def is_url(url):
    scheme = urllib.parse.urlparse(url).scheme
    return scheme in ('http', 'https')

