import requests

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q":"Monet"}
            )
        response.raise_for_status() # Check for HTTP errors
    except requests.HTTPError:
        print("Couldn't complete request")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")
              

main()