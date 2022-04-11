# Hackathon2022JaxPeteSpence
============================= Welcome to Geodle! ==============================

- The goal of the game is to successfully guess the secret country.
- You are given 10 tries to guess from a list of over 100 major countries.
- After entering your guess, feedback about your guess will be given.
- There are 5 categories of feedback: 
- **LETTER**- If the first letter of your guess is the same as the first letter of the secret country, the '_name_' box will become green; if the guess letter is within 5 letters of the secret country on either side within the alphabet, the box will become yellow; if outside this range, it will become grey.
- **HEMISPHERE**- If your guess is in the same hemisphere as the secret country, this box will become green, and if not, it will remain grey. In the special case that the secret country is in both hemishperes, the hemisphere box will show up as yellow. 
- **CONTINENT**- If your guess is in the same continent as the secret country, the box will become green; if it is in a bordering continent, it will become yellow, and if not, will remain grey.
- **AREA**- If your guess has a land area within 250,000 sq. km of the secret country, the box will become yellow, and if outside this range, grey.
- **POPULATION**- If your guess has a population within 10 million of the secret country, the box will become yellow, and if outside this range, grey.
-   **Arrows** - arrows will appear on the area and population boxes to show whether the secret country's corresponding value is lower or higher in that category than the guessed country's.
- Use the information provided to assist you on your quest to becoming the best Geodler!


-Run driver.py to play.
-Some countries lie on the border of continents. Whichever continent they predominantly reside on is classified as their home continent for Geodle's sake. (i.e. Russia is classified as Asian)
