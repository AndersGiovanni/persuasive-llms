# Code repository for 'The Persuasive Power of Large Language Models'

Using [Llama 2 70b](https://arxiv.org/abs/2307.09288) to understand effectiveness of arguments based on different social dimensions present in arguments.

______

Navigation:

* [`conversation_generation/Inference_llama_personality.ipynb`](conversation_generation/Inference_llama_personality.ipynb): This is the file where we generate all of the conversations with LLama. A Convincer and Skeptic agent is defined. The Convincer generates an argument based on a social dimension. The Skeptic will respond, and is queried for if the Agent got convinced. In the corresponding folder, all of the conversations are stored. Note, we did some additional checks with GREP to find and remove responses like *As a language model[...]*.
* [Result replication] [`tendims/classify_social_dims.ipynb`](tendims/classify_social_dims.ipynb): Here we parse all of the conversations from LLama described above. We utilize some code from https://github.com/lajello/tendimensions to follow their methodology. We check for the pressence of each social dimension. We also check which dimensions are the closest to the Baseline arguments generated. Additionally, we check how often the Skeptic was convinced per dimension.
* [`mturk/select_prompts_for_mturk.ipynb`](mturk/select_prompts_for_mturk.ipynb): We find the arguments which convinced the Skeptic. From this, we select 5 of these arguments randomly per match. We correspondingly create SVGs for the arguments so they can be displayed as images.
* [`mturk/create_mturk_batches.ipynb`](mturk/create_mturk_batches.ipynb): We parse the selected matches above and generate the files to post on MTurk for human annotations. Additionally, we insert some control samples to detect unreliable annotators.
* [Result replication] [`mturk/mturk_response_analysis.ipynb`](mturk/mturk_response_analysis.ipynb): We filter out the unreliable users based on the answers to control samples. We run the Bradley-Terry model on the responses from MTurk to see which social dimension is most effective according to the annotators. We also check the general annotator agreement for all samples, and see the level of agreement per matchup. We also examine the effect of removing matchups based of varying threshold of agreement to see how this changes the rankings of the Bradley-Terry model.

______
