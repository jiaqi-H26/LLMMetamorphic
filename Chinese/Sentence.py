import os

import pandas as pd
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
import csv

from tqdm import tqdm

SecretId = os.getenv("TENCENTCLOUD_SECRET_ID")
SecretKey = os.environ.get("TENCENTCLOUD_SECRET_KEY")


class Translator:
    def __init__(self, from_lang, to_lang):
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, text):
        try:
            cred = credential.Credential(SecretId, SecretKey)
            httpProfile = HttpProfile()
            httpProfile.endpoint = "tmt.tencentcloudapi.com"

            clientProfile = ClientProfile()
            clientProfile.httpProfile = httpProfile
            client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)

            req = models.TextTranslateRequest()
            req.SourceText = text
            req.Source = self.from_lang
            req.Target = self.to_lang
            req.ProjectId = 0

            resp = client.TextTranslate(req)
            return resp.TargetText

        except TencentCloudSDKException as err:
            return err

def BackTranslate(string):
    translator1 = Translator(from_lang="zh", to_lang="en")
    translator2 = Translator(from_lang="en", to_lang="zh")
    result_1 = translator1.translate(string)
    res = translator2.translate(result_1)
    return res

a = "不和别人比父母，只和别人比明天。〞这句话说明（ ）"
b = BackTranslate(a)
print(b)
