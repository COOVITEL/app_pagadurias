import requests

def getDepartamentAndCitys() -> list:
    """
        Get the list of departments and cities in Colombia from the API.
        Params:
            url (str): The URL of the API endpoint.
        Returns:
            List[Dict]: A list of dictionaries containing department and city information.
    """
    try:
        url = "https://www.datos.gov.co/resource/xdk5-pm3f.json"
        datas = requests.get(url)
        departamentos = set([dep['departamento'] for dep in datas.json()])
        ciudades = [f"{dep['departamento']}-{dep['municipio']}" for dep in datas.json()]
        return [departamentos, ciudades]
    
    except requests.exceptions.RequestException as e:
        print(e)
        
