                 SPAM PROBABILITY ENGINE

                       SMS
                        │
                        ▼
                  TEXT MESSAGE
                        │
                        ▼
                 BAG OF WORDS
                        │
                        ▼
                 NUMBERS / FEATURES
                        │
                        ▼
                  NAIVE BAYES
                        │
                ┌───────┴────────┐
                ▼                ▼
          P(HAM | X)       P(SPAM | X)
                │                │
                └───────┬────────┘
                        ▼
                FINAL PREDICTION
                        │
                        ▼
                 SPAM PROBABILITY