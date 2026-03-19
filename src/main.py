"""Command line runner for the Music Recommender Simulation."""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = [
        {"name": "High-Energy Pop", "genre": "pop", "mood": "happy", "energy": 0.8},
        {"name": "Chill Lofi", "genre": "lofi", "mood": "chill", "energy": 0.35},
        {"name": "Deep Intense Rock", "genre": "rock", "mood": "intense", "energy": 0.9},
        {"name": "Edge Case: Sad but High Energy", "genre": "ambient", "mood": "melancholy", "energy": 0.95},
        {"name": "Edge Case: No Genre Match", "genre": "country", "mood": "happy", "energy": 0.5},
    ]

    for profile in profiles:
        name = profile.pop("name")
        print(f"\n{'='*50}")
        print(f"Profile: {name}")
        print(f"genre={profile['genre']}, mood={profile['mood']}, energy={profile['energy']}")
        print("="*50)

        recommendations = recommend_songs(profile, songs, k=5)

        for i, (song, score, explanation) in enumerate(recommendations, 1):
            print(f"{i}. {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f} | {explanation}")
            print()

if __name__ == "__main__":
    main()