# -*- coding: utf-8 -*-

from snsapi.snspocket import SNSPocket
from datetime import datetime
import time

TEXTS = ['凌晨好', '清晨好', '早上好', '下午好', '傍晚好', '晚上好']
#URL = 'https://github.com/hupili/snsapi/tree/master/app/clock'
URL = 'http://t.cn/zj1VSdV'
AD = '10行写个跨平台的钟：%s' % URL

sp = SNSPocket()
sp.load_config()
sp.auth()

while True:
    h, m = datetime.now().hour, datetime.now().minute
    if m == 9:
        t = '%s -- 0x%X点钟， %s。(%s)' % ('烫' * h, h, TEXTS[h / 4], AD)
        print t
        sp.update(t)
    time.sleep(60)
