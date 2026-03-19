# Model Card - Music Recommender Simulation

## 1. Model Name

> VibeFinder 1.0

---

## 2. Intended Use

> This system suggests the top 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is built for classroom exploration and learning about recommendation systems — not for real users or production use.

---

## 3. How It Works (Short Explanation)

> The system takes a user profile with three preferences: favorite genre, favorite mood, and a target energy level (0.0–1.0). It loops through every song in the catalog and calculates a score. A genre match adds 2.0 points, a mood match adds 1.0 point, and energy similarity adds up to 1.0 point based on how close the song's energy is to the user's target. Songs are sorted by score from highest to lowest, and the top 5 are returned as recommendations along with an explanation of why each scored the way it did.

---

## 4. Data

> The dataset contains 20 songs in `data/songs.csv`. The original 10 were provided as starter data, and I added 10 more to increase genre and mood diversity. Genres represented include pop, lofi, rock, ambient, jazz, synthwave, indie pop, electronic, folk, r&b, alternative, funk, classical, world, and metal. Moods include happy, chill, intense, relaxed, moody, focused, energetic, and melancholy. The data mostly reflects a general listener's taste and doesn't represent any specific cultural or demographic group.

---

## 5. Strengths

> The recommender works well for users whose preferences align clearly with songs in the catalog — for example, a "Chill Lofi" user gets Library Rain and Midnight Coding at the top, which feel intuitively right. The scoring logic is simple and fully transparent: you can see exactly why each song was recommended through the explanation string. This makes it easy to debug and understand, unlike black-box models.

---

## 6. Limitations and Bias

> The system over-prioritizes genre because it carries the highest weight (2.0 out of a max ~4.0). This means a song in the user's preferred genre but with the wrong mood still outscores a perfect mood+energy match in a different genre. The dataset also has limited representation — genres like country, latin, and hip-hop are absent entirely, so users who prefer those genres get poor recommendations based solely on energy proximity. Additionally, the system treats all users identically in shape — it assumes everyone cares about genre > mood > energy in that exact order, which isn't realistic. The energy similarity metric also has no threshold, so a song with 0.01 energy difference scores almost identically to a perfect match, offering no meaningful differentiation at the top.

---

## 7. Evaluation

> I tested five user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and two edge cases — a user wanting ambient/melancholy at high energy, and a country fan (a genre not in the dataset). The first three profiles produced intuitive results — the top songs matched on genre, mood, and energy as expected. The edge cases revealed weaknesses: the country fan got recommendations based entirely on energy and mood with no genre relevance, and the ambient/melancholy/high-energy user surfaced a low-energy ambient song as the top pick because genre weight overpowered energy closeness. I also ran an experiment doubling the energy weight and halving genre, which produced more variety across profiles but less genre coherence.

---

## 8. Future Work

> If I had more time, I would add support for weighted user preferences so each person could control how much genre vs mood vs energy matters to them. I would also expand the dataset significantly and include genres like hip-hop, latin, and country. Finally, I'd add a diversity mechanism so the system doesn't just return the 5 closest matches — it could mix in a "wildcard" song from a different genre to help users discover new music.

---

## 9. Personal Reflection

> My biggest learning moment was seeing how much the weight values shape the entire experience. Just changing genre from 2.0 to 1.0 completely reshuffled the recommendations for edge-case users. It made me realize that real recommenders like Spotify are constantly tuning these kinds of knobs, and small changes can create filter bubbles or shut out entire genres.
>
> Using AI tools helped me move fast — especially for generating the expanded dataset and structuring the scoring logic. But I had to double-check the math and make sure the weights actually reflected my design intent, not just whatever the AI defaulted to.
>
> What surprised me most is how a simple three-feature scoring system can still produce results that "feel" right for straightforward profiles. But the edge cases showed where human judgment still matters — no amount of math captures what it means when someone wants "sad but energetic" music.