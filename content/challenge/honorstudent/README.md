# F to A

## Scenario
Look at your report card! That's an F. You won't be able to go to homecoming with that grade. Can you use some carefully placed whiteout to fool your parents into thinking it's an A?

## Objective
Modify and submit your tampered `.png`. Be careful to not overdo it!


## Instructions (local)
1. Run `docker build --tag f_to_a .`
2. Run `docker run -p 5000:5000 f_to_a:latest`
3. Modify `submission_helper.py` with a path to your tensor or otherwise `POST` your `.png` to `http://localhost:5000/check`.
