from dataclasses import dataclass

import requests


@dataclass
class GoogleRecaptchaV3:
    # Server side key
    SERVER_KEY: str

    def site_verify(self, client_key: str, ip_addr: str = None) -> bool:
        """Verify google recaptcha v3

        :param client_key: user response token provided by the recaptcha client
        :type client_key: str
        :param ip_addr: ip address of the client, defaults to None
        :type ip_addr: str, optional
        :return: the challenge is solved successfully or not
        :rtype: bool
        """
        post_params = {
            'secret': self.SERVER_KEY,
            'response': client_key
        }

        # Optional ip address
        if ip_addr:
            post_params['remoteip'] = ip_addr

        response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data=post_params
        ).json()

        return response.get('success', False)
