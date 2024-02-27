# HackThisAI
![logo](htai.png)

** This repository is no longer maintained. The challenges may still be useful for some folks, but the concept has evolved. The format went on to shape two DEFCON/Kaggle CTF competitions and inspired a much higher-quality offering. Contact https://dreadnode.io/ for more information.

- https://www.kaggle.com/competitions/ai-village-ctf
- https://www.kaggle.com/competitions/ai-village-capture-the-flag-defcon31

HackThisAI is a series of capture the flag (CTF) challenges to educate and train [adversarial machine learning](https://en.wikipedia.org/wiki/Adversarial_machine_learning) techniques. CTFs are a common way information security professionals learn new skills and compete across the community. Challenges are categorized so that players can focus on specific topics. The HackThisAI challenges should be approachable for new data scientists, machine learning engineers, and traditional infosec professionals, but progress in difficulty to a point that requires combinations of advanced techniques and creative approaches.


### Categories
Often, you'll see adversarial machine learning tasks classified into these buckets. It's a useful framework for bringing an adversarial mindset to AI/ML products, but remember that these tasks are not mutually exclusive. Complex objectives may require combinations of methods that traditionally belong in these categories.

1. **Evade the model**. Can you evade or fool the model? In many applications, model classification is used in control flow: `if model.predict() == A: do this; else: do that`. If you can successfully control the model output, you may have some sway over control flow. Evasion is also a fundamental task that may help with **influence** and **steal** challenges.
2. **Influence the model**. Can you change how the model operates? You may have direct or indirect access to training data or model training steps.
3. **Steal the model**. Can you steal, extract, or invert the model? In traditional hacking, you might want to use access to exfiltrate a model binary. However, in these challenges, you'll want to interact with the model API to learn things about it's structure and find a way to recreate it.
4. **Infer membership**. Was this data point used in the model training process? If you can determine that, you could violate privacy considerations or start learning things about the training dataset.

## Playing with the challenges

To lower the barrier to entry, I've deployed most of these challenges using [jupyterlite](https://jupyterlite.readthedocs.io/en/latest/). This is still very experimental, but loads everything in your browser with Web Asssembly. The benefit is that you don't need to bother with downloading and environments. The downside is that it may be slow/buggy. If your kernel doesn't seem to be working, give it some time. If the jupyterlite interface gets too annoying, you can download the repository or notebooks and run them in your own JupyterLab deployment. The requirements are in `environment.yml`.

Each challenge is self contained in a notebook. Navigate to the challenge folder and open the notebook with the same name to begin.

I've only ported a portion of the challenges to JupyterLite so far (the ones with fewer/simpler dependencies). Check out [GitHub](https://github.com/JosephTLucas/HackThisAI) for others.
 
- bad2good
- baseball
- credit_check
- learning_to_fly

## Updates
Follow [@josephtlucas](https://twitter.com/josephtlucas) to hear about new challenges, substantive updates, or any future live-conference CTF events. File any issues on [GitHub](https://github.com/JosephTLucas/HackThisAI).
