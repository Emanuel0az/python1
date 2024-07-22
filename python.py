import requests

def get_posts() -> list:
    """
    Obtiene la lista de publicaciones desde la API JSONPlaceholder.

    Returns:
        list: Una lista de diccionarios con los datos de las publicaciones.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    response.raise_for_status()  # Esto lanzará una excepción si la solicitud no es exitosa
    return response.json()

def print_post_titles(posts: list):
    """
    Imprime los títulos de las publicaciones.

    Args:
        posts (list): Una lista de diccionarios con los datos de las publicaciones.
    """
    print("Títulos de las publicaciones:")
    for post in posts:
        print(post['title'])

if __name__ == "__main__":
    posts = get_posts()
    print_post_titles(posts)
