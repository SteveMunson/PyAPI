"""https://requests.readthedocs.io/en/latest/"""
import requests


class PyHttpApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint='/', data=None, params=None, headers=None) -> requests.Response:
        '''
        The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.

        Args:
            endpoint (_type_): _description_
            params (_type_, optional): _description_. Defaults to None.
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        '''
        url = self.base_url + endpoint
        response = requests.get(
            url, data=data, params=params, headers=headers, timeout=10)
        return response

    def post(self, endpoint, data=None, headers=None) -> requests.Response:
        '''
        The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

        Args:
            endpoint (_type_): _description_
            data (_type_, optional): _description_. Defaults to None.
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        '''
        url = self.base_url + endpoint
        response = requests.post(url, json=data, headers=headers, timeout=10)
        return response

    def put(self, endpoint, data=None, headers=None) -> requests.Response:
        '''
        The PUT method replaces all current representations of the target resource with the request payload.

        Args:
            endpoint (_type_): _description_
            data (_type_, optional): _description_. Defaults to None.
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        '''
        url = self.base_url + endpoint
        response = requests.put(url, json=data, headers=headers, timeout=10)
        return response

    def delete(self, endpoint, headers=None) -> requests.Response:
        '''
        The DELETE method deletes the specified resource.

        Args:
            endpoint (_type_): _description_
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        '''
        url = self.base_url + endpoint
        response = requests.delete(url, headers=headers, timeout=10)
        return response

    def patch(self, endpoint, headers=None) -> requests.Response:
        '''
        The PATCH method applies partial modifications to a resource.

        Args:
            endpoint (_type_): _description_
            headers (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        '''
        url = self.base_url + endpoint
        response = requests.patch(url, headers=headers, timeout=10)
        return response
