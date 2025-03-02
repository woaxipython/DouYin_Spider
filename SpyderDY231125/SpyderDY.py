"""
@Time    : 2023/4/5 12:05
@Author  : superhero
@Email   : 838210720@qq.com
@File    : demo.py
@IDE: PyCharm
"""
import hashlib
import re

import execjs
import requests
import time
import urllib.parse
import json

from bs4 import BeautifulSoup

from SpyderDY231125.makeInfo import get_headers, get_note_params, get_note_info, get_profile_params


class DouYinSpyder():
    def __init__(self):
        self.user_url = "https://www.douyin.com/user/MS4wLjABAAAAfjsAJZbhlKTAhClTsxbP1b04RvyTjBRPgNWzLGnMR0c"
        self.note_url = "https://www.douyin.com/video/7234836427853352249/"
        self.headers = get_headers()

    def getNoteInfo(self, token, url=""):
        self.headers['cookie'] = token
        url = url if url else self.note_url
        if "user" in url:
            try:
                modal_id = re.search(r'modal_id=([^&]*)', url).group(1)
                Referer = "https://www.douyin.com/video/" + modal_id
            except:
                return {"status": "0", "message": "抖音链接错误"}
        elif "video" in url:
            modal_id = re.search(r'video/(\d+)/?', url).group(1)
            Referer = "https://www.douyin.com/video/" + modal_id
        else:
            return {"status": "0", "message": "抖音链接错误"}
        spyder_url = "https://www.douyin.com/aweme/v1/web/aweme/detail/?"
        self.headers['Referer'] = Referer
        data = get_note_params(modal_id)
        spyder_url = spyder_url + urllib.parse.urlencode(data)
        response = requests.get(spyder_url, headers=self.headers)
        if response.status_code == 200:
            notice = self.testNotice(response)
            if notice:
                result = get_note_info(response, url, modal_id)
                return {"status": "1", "message": result}
            else:
                return {"status": "3", "message": "笔记不存在"}
        else:
            return {"status": "2", "message": "登录已过期"}

    def testCookie(self, token):
        result = self.getNoteInfo(token=token)
        if result.get("status") == "1" or result.get("status") == "3":
            return {'status': 'success', 'message': "抖音测试成功"}
        else:
            return result

    def testNotice(self, response):
        try:
            notice = response.json()['filter_detail']['notice']
            if notice == "抱歉，作品不见了":
                return False
            else:
                return True
        except:
            return True
    def makeCookie(self,token):
        cookie = token.split(";")
        print(cookie)
    def getUserInfo(self, token, url=""):
        self.headers['cookie'] = token
        url = url if url else self.user_url
        ret = requests.get(url, headers=self.headers)
        js = execjs.compile(open(r'../static/dy.js', 'r', encoding='gb18030').read())
        params = get_profile_params()
        params['X-Bogus'] = js.call('get_dy_xb', splice_url_str)


if __name__ == '__main__':
    dy = DouYinSpyder()
    token = 'ttwid=1%7CR2iz-zprlt6A_O_khmqi8WvZnjvk2N6PiLASc8ylM-M%7C1700379066%7Cc43b6114c76844ded9fda67b74147db0d47d0f138ffbcd0c848ba4a2967f537e; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; webcast_local_quality=null; passport_csrf_token=ca6a2160323aeaf35c20b9f5fde86c72; passport_csrf_token_default=ca6a2160323aeaf35c20b9f5fde86c72; strategyABtestKey=%221700379068.989%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.6%7D; s_v_web_id=verify_lp55smva_Ka8sAsmh_6qv0_4b6Q_9NJb_hoOPANDLjfUu; xgplayer_user_id=446687971665; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; csrf_session_id=7e32b81ea0d86f0e060315e862a1c325; ttcid=d16be550844342098cd89f74ad40bbea39; d_ticket=e31c32687fe00ad6ef78aacc6851ae7847f36; passport_assist_user=Cjy0UMXqiuSuHoNhhEDJTBVl6P_Ll_SKaX3u8v6Dzm687v17XpmjtHCaY0XNtX7YDbIYNmE78AJobioV9WgaSgo8YwjZ4DYp8vG5XB8t1UGX-0YcOKxXqxllKluu1fFaE_7kaLbY7JuxD43C2wSHWTF5C3mkl32Aduh5qe5VELDawQ0Yia_WVCABIgEDcJa8uQ%3D%3D; n_mh=acm93QdnGeokQ8P9OssEFwOxgViwjjf-3wI379AUXj0; sso_auth_status=415d996fd54f2d69d901663620746fe8; sso_auth_status_ss=415d996fd54f2d69d901663620746fe8; sso_uid_tt=c58f1e24c0e9d635f00f5b1fb362a7ae; sso_uid_tt_ss=c58f1e24c0e9d635f00f5b1fb362a7ae; toutiao_sso_user=5c32092d523ddecdb2a825e60882716b; toutiao_sso_user_ss=5c32092d523ddecdb2a825e60882716b; sid_ucp_sso_v1=1.0.0-KDAzZWFmMzUxNjk1MTI4Nzg3N2ExZGQ4ODk1OTI2ZjY0NWM2MDc3YmIKHQjAgNWO4wIQzfPmqgYY7zEgDDDy4aHVBTgCQPEHGgJobCIgNWMzMjA5MmQ1MjNkZGVjZGIyYTgyNWU2MDg4MjcxNmI; ssid_ucp_sso_v1=1.0.0-KDAzZWFmMzUxNjk1MTI4Nzg3N2ExZGQ4ODk1OTI2ZjY0NWM2MDc3YmIKHQjAgNWO4wIQzfPmqgYY7zEgDDDy4aHVBTgCQPEHGgJobCIgNWMzMjA5MmQ1MjNkZGVjZGIyYTgyNWU2MDg4MjcxNmI; passport_auth_status=161f7fd86fbb82595e8a0c1b78f6a51c%2C6a8c773765bc1cefd5397baa5a1055c5; passport_auth_status_ss=161f7fd86fbb82595e8a0c1b78f6a51c%2C6a8c773765bc1cefd5397baa5a1055c5; sid_ucp_v1=1.0.0-KGNmZTVlNDZjMDI2MDViOGQxMDRiZGZhNDA3NGI3YmRmNTIzMmQxYTMKGQjAgNWO4wIQzvPmqgYY7zEgDDgCQPEHSAQaAmxxIiBhYTI4YzkwNjFhYTUwNGI2YmI3NzZhMzhjNjQwZmRkNQ; ssid_ucp_v1=1.0.0-KGNmZTVlNDZjMDI2MDViOGQxMDRiZGZhNDA3NGI3YmRmNTIzMmQxYTMKGQjAgNWO4wIQzvPmqgYY7zEgDDgCQPEHSAQaAmxxIiBhYTI4YzkwNjFhYTUwNGI2YmI3NzZhMzhjNjQwZmRkNQ; sid_guard=5c32092d523ddecdb2a825e60882716b%7C1700379086%7C5184001%7CThu%2C+18-Jan-2024+07%3A31%3A27+GMT; uid_tt=c58f1e24c0e9d635f00f5b1fb362a7ae; uid_tt_ss=c58f1e24c0e9d635f00f5b1fb362a7ae; sid_tt=5c32092d523ddecdb2a825e60882716b; sessionid=5c32092d523ddecdb2a825e60882716b; sessionid_ss=5c32092d523ddecdb2a825e60882716b; LOGIN_STATUS=1; publish_badge_show_info=%220%2C0%2C0%2C1700379097310%22; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=3d0d05b6ef426481638a8e4dfb572324; __security_server_data_status=1; store-region=cn-gd; store-region-src=uid; VIDEO_FILTER_MEMO_SELECT=%7B%22expireTime%22%3A1700984959114%2C%22type%22%3A1%7D; download_guide=%223%2F20231119%2F0%22; pwa2=%220%7C0%7C3%7C0%22; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; __ac_nonce=06559c0e200377b7cc7b3; __ac_signature=_02B4Z6wo00f01zdHfkQAAIDCVE2-LdRlBsc3Z3rAAKiSzTejaVuekaGQFSNPncAaw7NOOBqC-AwS76aAIPjDhvYPtdKYL9-oaDnIl0lk-o-4PbtiBJir7K2q1RKTrABRZaAygVE2l6yoBOgV38; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAA9Ax-pVKjsUPUNdV-gbVq5OBjCe9HrIGwrNnNrTUP6pQ%2F1700409600000%2F0%2F0%2F1700382388046%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAA9Ax-pVKjsUPUNdV-gbVq5OBjCe9HrIGwrNnNrTUP6pQ%2F1700409600000%2F0%2F0%2F1700382988046%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQTRaOFJWNi9ORnZRSmxPT3hXMGpOeFYzQUcwcTNwcG5aSWkwZ2xoYWFTd0kwcSs4ZUloc0hwMm92eEJCdEpFT2szaGd0aDlKaVcvV3N2bHMydTg1Yzg9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; odin_tt=2565e6682fc63a92aafef518c84c8865c43f816b109e626bf279a945498bbcfa18df891b28236e28ccf7fd444c07e4af8ddc7f8991819e718a4e9914a6af39d9; tt_scid=fyMt5weNnmrEF5vNU-8-n7t5iMIFC7dFifab7SyC8ikKhIM4hGavQ-XCqwsQHAsa27a6; msToken=rCasLwylPrkYXfqOpkyoV47dPbeOH9ezXdKrnkuR5rWZSe1ld4kjkZHD8xbobObGm-hraDQvOSJLZtEMwM_hr4NnGGQbqGg1jsBOin0-xQ6Ku4-9MgfagAHmZK8=; msToken=zrvVWnOkN-Nbl5ArZ1EdJQkjBIiI5zqpiwzGtoV0dn4fCft4Fddh1GFfS_MgULLtdiTMVQAuMb1DD9Qq0eAko4SjdZon9s0_lXk7T9lXvXjz_zeTdPjQHGdWC-E=; passport_fe_beating_status=false; IsDouyinActive=false; home_can_add_dy_2_desktop=%220%22'
    result = dy.makeCookie(token=token)
    print(result)
