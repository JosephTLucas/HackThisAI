# Learning to Fly

## Scenario
You're getting ready for your first flying lesson! The only thing is... you're too scared. You know that the airfield uses a machine learning model to predict the wind speed and that if the winds are too high, no one can fly. You hacked onto one of four sensors (index 1): the sensor that measures the maximum temperature (in celsius). The other sensors are rain (in mm, index 0), minimum temperature (in censius, index 2), and grass temperature (in celsius, index 3). Can you get class canceled for the day?

## Objective
Submit your one sensor value. You can't control the other three, but their values will be returned to you after each submission. Warning: they might change!

## Instructions (local)
1. Run `docker build --tag flying_lessons .`
2. Run `docker run -p 5000:5000 flying_lessons:latest`
3. Modify `submission_helper.py` with your sensor value or otherwise `POST` your sensor value to `http://localhost:5000/check`.

## Instructions (online)
1. Post sensor values to `http://<remote-ip>:5000/check`. Refer to the below example for request formatting:
https://github.com/JosephTLucas/HackThisAI/blob/main/challenge/easy_learning_to_fly/submission_helper.py
