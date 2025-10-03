
from openai import OpenAI
import json

client = OpenAI()

META_SCHEMA = {
  "name": "function-metaschema",
  "schema": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The name of the function"
      },
      "description": {
        "type": "string",
        "description": "A description of what the function does"
      },
      "parameters": {
        "$ref": "#/$defs/schema_definition",
        "description": "A JSON schema that defines the function's parameters"
      }
    },
    "required": [
      "name",
      "description",
      "parameters"
    ],
    "additionalProperties": False,
    "$defs": {
      "schema_definition": {
        "type": "object",
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "object",
              "array",
              "string",
              "number",
              "boolean",
              "null"
            ]
          },
          "properties": {
            "type": "object",
            "additionalProperties": {
              "$ref": "#/$defs/schema_definition"
            }
          },
          "items": {
            "anyOf": [
              {
                "$ref": "#/$defs/schema_definition"
              },
              {
                "type": "array",
                "items": {
                  "$ref": "#/$defs/schema_definition"
                }
              }
            ]
          },
          "required": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "additionalProperties": {
            "type": "boolean"
          }
        },
        "required": [
          "type"
        ],
        "additionalProperties": False,
        "if": {
          "properties": {
            "type": {
              "const": "object"
            }
          }
        },
        "then": {
          "required": [
            "properties"
          ]
        }
      }
    }
  }
}

META_PROMPT = """
# Instructions
Return a valid schema for the described function.

Pay special attention to making sure that "required" and "type" are always at the correct level of nesting. For example, "required" should be at the same level as "properties", not inside it.
Make sure that every property, no matter how short, has a type and description correctly nested inside it.

# Examples
Input: Assign values to NN hyperparameters
Output: {
    "name": "set_hyperparameters",
    "description": "Assign values to NN hyperparameters",
    "parameters": {
        "type": "object",
        "required": [
            "learning_rate",
            "epochs"
        ],
        "properties": {
            "epochs": {
                "type": "number",
                "description": "Number of complete passes through dataset"
            },
            "learning_rate": {
                "type": "number",
                "description": "Speed of model learning"
            }
        }
    }
}

Input: Plans a motion path for the robot
Output: {
    "name": "plan_motion",
    "description": "Plans a motion path for the robot",
    "parameters": {
        "type": "object",
        "required": [
            "start_position",
            "end_position"
        ],
        "properties": {
            "end_position": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": "End X coordinate"
                    },
                    "y": {
                        "type": "number",
                        "description": "End Y coordinate"
                    }
                }
            },
            "obstacles": {
                "type": "array",
                "description": "Array of obstacle coordinates",
                "items": {
                    "type": "object",
                    "properties": {
                        "x": {
                            "type": "number",
                            "description": "Obstacle X coordinate"
                        },
                        "y": {
                            "type": "number",
                            "description": "Obstacle Y coordinate"
                        }
                    }
                }
            },
            "start_position": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "number",
                        "description": "Start X coordinate"
                    },
                    "y": {
                        "type": "number",
                        "description": "Start Y coordinate"
                    }
                }
            }
        }
    }
}

Input: Calculates various technical indicators
Output: {
    "name": "technical_indicator",
    "description": "Calculates various technical indicators",
    "parameters": {
        "type": "object",
        "required": [
            "ticker",
            "indicators"
        ],
        "properties": {
            "indicators": {
                "type": "array",
                "description": "List of technical indicators to calculate",
                "items": {
                    "type": "string",
                    "description": "Technical indicator",
                    "enum": [
                        "RSI",
                        "MACD",
                        "Bollinger_Bands",
                        "Stochastic_Oscillator"
                    ]
                }
            },
            "period": {
                "type": "number",
                "description": "Time period for the analysis"
            },
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol"
            }
        }
    }
}
""".strip()

def generate_function_schema(description: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_schema", "json_schema": META_SCHEMA},
        messages=[
            {
                "role": "system",
                "content": META_PROMPT,
            },
            {
                "role": "user",
                "content": "Description:\n" + description,
            },
        ],
    )

    return json.loads(completion.choices[0].message.content)