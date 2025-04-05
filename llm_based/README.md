grading_llm/
├── config/
│   └── config.json
├── data/
│   ├── train.csv
│   └── test.csv
├── utils/
│   ├── few_shot.py          ← few_shot_format + create_few_shot_examples
│   └── inference.py         ← single inference call, batching later
├── prompts/
│   └── template.py          ← stores the LLM prompt template
├── main.py                  ← loads data, prepares prompt, runs test
└── requirements.txt