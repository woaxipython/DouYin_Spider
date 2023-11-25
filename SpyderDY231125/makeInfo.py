import time


def get_headers():
    return {
        "authority": "www.douyin.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "https://www.douyin.com/user/MS4wLjABAAAAigSKToDtKeC5cuZ3YsDrHfYuvpLqVSygIZ0m0yXfUAI",
        "sec-ch-ua": "\"Microsoft Edge\";v=\"117\", \"Not;A=Brand\";v=\"8\", \"Chromium\";v=\"117\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"
    }


def get_profile_params():
    return {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "publish_video_strategy_type": "2",
        "source": "channel_pc_web",
        "sec_user_id": "",
        "pc_client_type": "1",
        "version_code": "170400",
        "version_name": "17.4.0",
        "cookie_enabled": "true",
        "screen_width": "1707",
        "screen_height": "1067",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Edge",
        "browser_version": "117.0.2045.47",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "117.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "20",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "50",
        # "webid": "7285671865124996668",
        "webid": "",
        "msToken": "",
    }


def get_note_params(modal_id):
    return {
        "device_platform": "webapp",
        "aid": "6383",
        "channel": "channel_pc_web",
        "aweme_id": modal_id,
        "pc_client_type": "1",
        "version_code": "190500",
        "version_name": "19.5.0",
        "cookie_enabled": "true",
        "screen_width": "1920",
        "screen_height": "1080",
        "browser_language": "zh-CN",
        "browser_platform": "Win32",
        "browser_name": "Chrome",
        "browser_version": "114.0.0.0",
        "browser_online": "true",
        "engine_name": "Blink",
        "engine_version": "114.0.0.0",
        "os_name": "Windows",
        "os_version": "10",
        "cpu_core_num": "16",
        "device_memory": "8",
        "platform": "PC",
        "downlink": "10",
        "effective_type": "4g",
        "round_trip_time": "50",
        "webid": "7303072417411532314",
        "msToken": "rCasLwylPrkYXfqOpkyoV47dPbeOH9ezXdKrnkuR5rWZSe1ld4kjkZHD8xbobObGm-hraDQvOSJLZtEMwM_hr4NnGGQbqGg1jsBOin0-xQ6Ku4-9MgfagAHmZK8=",
    }


def get_note_info(response, url, modal_id):
    data = response.json()['aweme_detail']

    upload_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data.get("create_time")))
    return {
        "title": data.get("desc"),
        "content_id": modal_id,
        "liked": data.get("statistics").get("digg_count"),
        "desc": data.get("statistics").get("desc"),
        "collected": data.get("statistics").get("collect_count"),
        "commented": data.get("statistics").get("comment_count"),
        "forwarded": data.get("statistics").get("share_count"),
        "imageList": [],
        "commentList": [],
        "hashTags": [],
        "video_link": url,
        "spyder_url": url,
        "upload_time": upload_time,
        "content_link": "",
        "status": "正常",
    }
