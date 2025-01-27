# -*- coding:utf-8 -*-

"""
Created on 2024/02/29
@author: Raisul Islam
@group : bdshare.xyz
@contact: raisul.me@gmail.com
"""

import pandas as pd
import os
from . import cons as ct


BK = 'bk'


def set_token(token):
    """
    Set the user's token in a local file.

    :param token: str, the token
    :return: None
    """
    df = pd.DataFrame([token], columns=['token'])
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, ct.TOKEN_F_P)
    df.to_csv(fp, index=False)


def get_token():
    user_home = os.path.expanduser('~')
    fp = os.path.join(user_home, ct.TOKEN_F_P)
    if os.path.exists(fp):
        df = pd.read_csv(fp)
        return str(df.ix[0]['token'])
    else:
        print(ct.TOKEN_ERR_MSG)
        return None


def set_broker(broker='', user='', passwd=''):
    df = pd.DataFrame([[broker, user, passwd]],
                      columns=['broker', 'user', 'passwd'],
                      dtype=object)
    if os.path.exists(BK):
        all = pd.read_csv(BK, dtype=object)
        if (all[all.broker == broker]['user']).any():
            all = all[all.broker != broker]
        all = all.append(df, ignore_index=True)
        all.to_csv(BK, index=False)
    else:
        df.to_csv(BK, index=False)


def get_broker(broker=''):
    if os.path.exists(BK):
        df = pd.read_csv(BK, dtype=object)
        if broker == '':
            return df
        else:
            return df[df.broker == broker]
    else:
        return None


def remove_broker():
    os.remove(BK)
