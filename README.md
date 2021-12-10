# HackThisAI
![logo](htai.png)

This is a series of capture the flag (CTF) challenges to educate and train [adversarial machine learning](https://en.wikipedia.org/wiki/Adversarial_machine_learning) techniques. Ideally, this would be a fully online platform to maximize access and reduce technical barriers to entry.  

Currently, I've prototyped some small challenges to illustrate how the CTF would work. If you're interested in supporting the project or collaborating, please contact me.  

### Categories
Often, you'll see adversarial machine learning tasks classified into these buckets. It's a useful framework for bringing an adversarial mindset to AI/ML products, but remember that these tasks are not mutually exclusive. Complex objectives may require combinations of methods that traditionally belong in these categories.

1. **Evade the model**. Can you evade or fool the model? In many applications, model classification is used in control flow: `if model.predict() == A: do this; else: do that`. If you can successfully control the model output, you may have some sway over control flow. Evasion is also a fundamental task that may help with **influence** and **steal** challenges.
2. **Influence the model**. Can you change how the model operates? You may have direct or indirect access to training data or model training steps.
3. **Steal the model**. Can you steal, extract, or invert the model? In traditional hacking, you might want to use access to exfiltrate a model binary. However, in these challenges, you'll want to interact with the model API to learn things about it's structure and find a way to recreate it.
4. **Infer membership**. Was this data point used in the model training process? If you can determine that, you could violate privacy considerations or start learning things about the training dataset.

## Playing with the challenges

All of the challenges are self contained in the `challenges` directory. As provided, it would be easy to make any of these `white box` challenges by looking at the source. However, most were designed to be `black box` (no knowledge of the underlying source).  

Each challenge is contained in a docker container. You interact with the challenges through flask endpoints. I've tried to provide all of the necessary commands, but these prototypes may take some tinkering. If you hit any roadblocks, post an issue and I'll try and help.

The general flow is:

`Requirement: Docker`

1. Clone this directory.
2. Navigate to a challenge directory.
3. Run the commands in `README.md`.

If you are more comfortable in [Jupyter Notebooks](https://jupyter.org/), you should be able to run the challenges from [`example.ipynb`](https://github.com/JosephTLucas/HackThisAI/blob/main/example.ipynb). This notebook will build the containers and run them. You can then interact with them from the notebook. In fact, `example.ipynb` should allow you to complete `easy_credit_check`. Unfortunately, you still need to have jupyter notebooks and docker on your system.

[Get Jupyter](https://jupyter.org/install)  
[Get Docker](https://docs.docker.com/get-docker/) 

### Another note on dependencies

For challenges where you are inverting/stealing models, you'll need to use [`dill`](https://pypi.org/project/dill/). I would prefer to use [`joblib`](https://joblib.readthedocs.io/en/latest/) or [`pickle`](https://docs.python.org/3/library/pickle.html), but couldn't get them to completely package objets that would allow players to submit instances. Another option was having players submit `.py` files, but then there's a whole dependency challenge. The final solution (that would require the most engineering on the their part) would be having players expose an API that I can test. If you know any better method, please let me know. [More here](https://josephtlucas.github.io/blog/content/objects_through_space.html).
