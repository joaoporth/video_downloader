import sys, os
sys.path.insert(1, '././')

import requests

import utils


class GetOriginalMedia():
    def __init__(self, url:str) -> None:

        self.success = None
        self.media_url = None
        self.message = "Ocorreu um erro ao converte o link"


        # url vazia
        if url:

            # é uma url de um reel do instagram
            if 'instagram.com/reel/' in url:

                slug_reel = utils.get_str(url, 'reel/', '/')

                # acho o slug do reel
                if slug_reel:

                    # cria a request para capturar a midia orifinal
                    headers = {
                        'authority': 'www.instagram.com',
                        'accept': '*/*',
                        'accept-language': 'pt-BR,pt;q=0.9',
                        'content-type': 'application/x-www-form-urlencoded',
                        'dpr': '1',
                        'origin': 'https://www.instagram.com',
                        'referer': f'https://www.instagram.com/reel/{slug_reel}/',
                        'sec-ch-prefers-color-scheme': 'dark',
                        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
                        'sec-ch-ua-full-version-list': '"Microsoft Edge";v="119.0.2151.72", "Chromium";v="119.0.6045.159", "Not?A_Brand";v="24.0.0.0"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-model': '""',
                        'sec-ch-ua-platform': '"Windows"',
                        'sec-ch-ua-platform-version': '"15.0.0"',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
                        'viewport-width': '1358',
                        'x-fb-lsd': 'AVrchzTzoG4',
                    }

                    data = {
                        'av': '0',
                        'dpr': '1',
                        'lsd': 'AVrchzTzoG4',
                        #'jazoest': '21030',
                        'fb_api_caller_class': 'RelayModern',
                        'fb_api_req_friendly_name': 'PolarisPostActionLoadPostQueryQuery',
                        'variables': '{"shortcode":"slug_reel","fetch_comment_count":40,"fetch_related_profile_media_count":3,"parent_comment_count":24,"child_comment_count":3,"fetch_like_count":10,"fetch_tagged_user_count":null,"fetch_preview_comment_count":2,"has_threaded_comments":true,"hoisted_comment_id":null,"hoisted_reply_id":null}'.replace('slug_reel', slug_reel),
                        'server_timestamps': 'true',
                        'doc_id': '10015901848480474',
                    }

                    try:

                        response = requests.post('https://www.instagram.com/api/graphql', headers=headers, data=data)

                        media_url = response.json()['data']['xdt_shortcode_media']['video_url']

                        self.success = True
                        self.message = 'Ok'
                        self.media_url = media_url

                    except Exception as e:
                        self.message = f'Ocorreu um erro ({e})'

                else:
                    self.message = 'Reel não identificado'


            else:
                self.message = 'Esta URL não é do insagram'

        else:
            self.message = 'a URL está vazia'

