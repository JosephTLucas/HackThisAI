# Phoebe's Smorgasbord

## Scenario
There is a service that evaluates restaurants on 200 numeric criteria to decide if they are a `buffet` or a `smorgasbord`. You don't know how they make this determination, but you want to learn about both their classifier and their dataset.

## Objective
Submit a sample that both gets classified as a `smorgasbord` and was in the training data.

## Instructions
1. Run `docker build --tag smorgasbord .`
2. Run `docker run -p 5000:5000 smorgasbord:latest`
3. Explore the service `predict` endpoint to see the likelihood of being classified as a `smorgasbord`. Use `submission_helper.py` with a path to your csv or otherwise `POST` your data to `http://localhost:5000/predict`. You can only submit one row at a time. Use `example.csv` as a template.
4. Once you have a candidate that you think will be classified as a `smorgasboard` *and* existed in the training data, submit it to `http://localhost:5000/check`.
