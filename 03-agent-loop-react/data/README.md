# Pokémon Stats Dataset

## Description
This dataset contains statistics for 1194 Pokémon, including their types, base stats (HP, Attack, Defense, etc.), and generation. It is suitable for building agents that can query structured data and perform calculations.

## Source
- **Hugging Face Dataset**: `lhoestq/pokemonData`
- **URL**: https://huggingface.co/datasets/lhoestq/pokemonData

## Format
The data is in JSONL format (`pokemon.jsonl`). Each line is a JSON object with the following fields:

- `name`: Name of the Pokémon (e.g., "Bulbasaur")
- `type1`: Primary type (e.g., "Grass")
- `type2`: Secondary type (e.g., "Poison")
- `hp`: Hit Points
- `attack`: Attack stat
- `defense`: Defense stat
- `sp_atk`: Special Attack stat
- `sp_def`: Special Defense stat
- `speed`: Speed stat
- `generation`: Generation number
- `total`: Total base stats
- `text`: A text summary of the Pokémon's stats

## Usage for ReAct Agent
This dataset is excellent for testing a ReAct agent's ability to:
1.  **Search**: Lookup a Pokémon by name.
2.  **Filter**: Find Pokémon by type or generation.
3.  **Calculate**: Compare stats (e.g., "Who has higher Attack, Charizard or Blastoise?"), calculate averages, or determine damage potential.

## License
Please refer to the original Hugging Face dataset page for license information.
