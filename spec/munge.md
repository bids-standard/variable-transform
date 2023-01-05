# Compute transformations



## filter string output

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Filter",
        "Input": "familiarity",
        "Query": " familiarity == Famous face ",
        "Output": "famous_face"
    },
    "Description": "filter string output"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time | famous_face   |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|:--------------|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  | Famous face   |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    | nan           |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 | Famous face   |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  | nan           |


## assign with output and input attribute

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |      1 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |      1 |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |      1 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |      1 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Assign",
        "Input": "response_time",
        "Target": "Face",
        "Output": "new_face",
        "InputAttr": "onset"
    },
    "Description": "assign with output and input attribute"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |   new_face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|-----------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |      1 |          2 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |      1 |          4 |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |      1 |          5 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |      1 |          8 |


## replace string by numeric

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Replace",
        "Input": "familiarity",
        "Replace": {
            "key": "Famous face",
            "value": 1
        },
        "Attribute": "duration"
    },
    "Description": "replace string by numeric"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          1 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          1 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |


## filter string

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Filter",
        "Input": "familiarity",
        "Query": " familiarity == Famous face "
    },
    "Description": "filter string"
}
```

### output 

|   onset |   duration |   repetition | familiarity   | trial_type   |   response_time |
|--------:|-----------:|-------------:|:--------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face   | Face         |            1.5  |
|       4 |          2 |            1 | nan           | Face         |            2    |
|       5 |          2 |            2 | Famous face   | Face         |            1.56 |
|       8 |          2 |            2 | nan           | Face         |            2.1  |


## factor

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Factor",
        "Input": [
            "familiarity"
        ]
    },
    "Description": "factor"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   familiarity_1 |   familiarity_2 |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|----------------:|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |               1 |               0 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |               0 |               1 |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |               1 |               0 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |               0 |               1 |


## assign with output

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |      1 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |      1 |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |      1 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |      1 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Assign",
        "Input": "response_time",
        "Target": "Face",
        "Output": "new_face"
    },
    "Description": "assign with output"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |   new_face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|-----------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |      1 |       1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |      1 |       2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |      1 |       1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |      1 |       2.1  |


## filter string unequal

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Filter",
        "Input": "familiarity",
        "Query": " familiarity ~= Famous face "
    },
    "Description": "filter string unequal"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | nan             | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | nan             | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |


## select event

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Select",
        "Input": [
            "familiarity"
        ]
    },
    "Description": "select event"
}
```

### output 

| familiarity     |   onset |   duration |
|:----------------|--------:|-----------:|
| Famous face     |       2 |          2 |
| Unfamiliar face |       4 |          2 |
| Famous face     |       5 |          2 |
| Unfamiliar face |       8 |          2 |


## factor numeric

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Factor",
        "Input": [
            "age"
        ]
    },
    "Description": "factor numeric"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_10 |   age_18 |   age_21 |   age_46 |   age_NaN |
|--------:|:-------------|:------|----------------:|------:|---------:|---------:|---------:|---------:|----------:|
|       1 | right        | M     |               1 |    21 |        0 |        0 |        1 |        0 |         0 |
|       1 | left         | M     |               0 |    18 |        0 |        1 |        0 |        0 |         0 |
|       0 | nan          | F     |               1 |    46 |        0 |        0 |        0 |        1 |         0 |
|       0 | left         | F     |               0 |    10 |        1 |        0 |        0 |        0 |         0 |
|       0 | right        | F     |               0 |   nan |        0 |        0 |        0 |        0 |         1 |


## and nan

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "And",
        "Input": [
            "handedness",
            "age"
        ],
        "Output": "age_or_hand"
    },
    "Description": "and nan"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_or_hand |
|--------:|:-------------|:------|----------------:|------:|--------------:|
|       1 | right        | M     |               1 |    21 |             1 |
|       1 | left         | M     |               0 |    18 |             1 |
|       0 | nan          | F     |               1 |    46 |             0 |
|       0 | left         | F     |               0 |    10 |             1 |
|       0 | right        | F     |               0 |   nan |             0 |


## assign

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |      1 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |      1 |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |      1 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |      1 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Assign",
        "Input": "response_time",
        "Target": "Face"
    },
    "Description": "assign"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |   1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |   2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |   1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |   2.1  |


## split simple

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Split",
        "Input": [
            "age"
        ],
        "By": [
            "sex"
        ]
    },
    "Description": "split simple"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_BY_sex_F |   age_BY_sex_M |
|--------:|:-------------|:------|----------------:|------:|---------------:|---------------:|
|       1 | right        | M     |               1 |    21 |            nan |             21 |
|       1 | left         | M     |               0 |    18 |            nan |             18 |
|       0 | nan          | F     |               1 |    46 |             46 |            nan |
|       0 | left         | F     |               0 |    10 |             10 |            nan |
|       0 | right        | F     |               0 |   nan |            nan |            nan |


## concatenate numbers

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Concatenate",
        "Input": [
            "onset",
            "response_time"
        ],
        "Output": "trial_type"
    },
    "Description": "concatenate numbers"
}
```

### output 

|   onset |   duration |   repetition | familiarity     |   trial_type |   response_time |
|--------:|-----------:|-------------:|:----------------|-------------:|----------------:|
|       2 |          2 |            1 | Famous face     |        21.5  |            1.5  |
|       4 |          2 |            1 | Unfamiliar face |        42    |            2    |
|       5 |          2 |            2 | Famous face     |        51.56 |            1.56 |
|       8 |          2 |            2 | Unfamiliar face |        82.1  |            2.1  |


## assign with target attribute

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |      1 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |      1 |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |      1 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |      1 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Assign",
        "Input": "response_time",
        "Target": "Face",
        "TargetAttr": "duration"
    },
    "Description": "assign with target attribute"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   Face |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|-------:|
|       2 |       2    |            1 | Famous face     | Face         |            1.5  |    nan |
|       4 |       2    |            1 | Unfamiliar face | Face         |            2    |    nan |
|       5 |       2    |            2 | Famous face     | Face         |            1.56 |    nan |
|       8 |       2    |            2 | Unfamiliar face | Face         |            2.1  |    nan |
|       2 |       1.5  |          nan | nan             | nan          |          nan    |      1 |
|       4 |       2    |          nan | nan             | nan          |          nan    |      1 |
|       5 |       1.56 |          nan | nan             | nan          |          nan    |      1 |
|       8 |       2.1  |          nan | nan             | nan          |          nan    |      1 |


## replace

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Replace",
        "Input": "familiarity",
        "Replace": [
            {
                "key": "Famous face",
                "value": "foo"
            },
            {
                "key": "Unfamiliar face",
                "value": "bar"
            }
        ]
    },
    "Description": "replace"
}
```

### output 

|   onset |   duration |   repetition | familiarity   | trial_type   |   response_time |
|--------:|-----------:|-------------:|:--------------|:-------------|----------------:|
|       2 |          2 |            1 | foo           | Face         |            1.5  |
|       4 |          2 |            1 | bar           | Face         |            2    |
|       5 |          2 |            2 | foo           | Face         |            1.56 |
|       8 |          2 |            2 | bar           | Face         |            2.1  |


## concatenate strings

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Concatenate",
        "Input": [
            "trial_type",
            "familiarity"
        ],
        "Output": "trial_type"
    },
    "Description": "concatenate strings"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type           |   response_time |
|--------:|-----------:|-------------:|:----------------|:---------------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face_Famous face     |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face_Unfamiliar face |            2    |
|       5 |          2 |            2 | Famous face     | Face_Famous face     |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face_Unfamiliar face |            2.1  |


## split simple string

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Split",
        "Input": [
            "handedness"
        ],
        "By": [
            "sex"
        ]
    },
    "Description": "split simple string"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age | handedness_BY_sex_F   | handedness_BY_sex_M   |
|--------:|:-------------|:------|----------------:|------:|:----------------------|:----------------------|
|       1 | right        | M     |               1 |    21 | nan                   | right                 |
|       1 | left         | M     |               0 |    18 | nan                   | left                  |
|       0 | nan          | F     |               1 |    46 | nan                   | nan                   |
|       0 | left         | F     |               0 |    10 | left                  | nan                   |
|       0 | right        | F     |               0 |   nan | right                 | nan                   |


## split empty by

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Split",
        "Input": [
            "age"
        ],
        "By": []
    },
    "Description": "split empty by"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |


## split nested

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Split",
        "Input": [
            "age"
        ],
        "By": [
            "sex",
            "handedness"
        ]
    },
    "Description": "split nested"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_BY_handedness_NaN_BY_sex_F |   age_BY_handedness_NaN_BY_sex_M |   age_BY_handedness_left_BY_sex_F |   age_BY_handedness_left_BY_sex_M |   age_BY_handedness_right_BY_sex_F |   age_BY_handedness_right_BY_sex_M |
|--------:|:-------------|:------|----------------:|------:|---------------------------------:|---------------------------------:|----------------------------------:|----------------------------------:|-----------------------------------:|-----------------------------------:|
|       1 | right        | M     |               1 |    21 |                              nan |                              nan |                               nan |                               nan |                                nan |                                 21 |
|       1 | left         | M     |               0 |    18 |                              nan |                              nan |                               nan |                                18 |                                nan |                                nan |
|       0 | nan          | F     |               1 |    46 |                              nan |                              nan |                               nan |                               nan |                                nan |                                nan |
|       0 | left         | F     |               0 |    10 |                              nan |                              nan |                                10 |                               nan |                                nan |                                nan |
|       0 | right        | F     |               0 |   nan |                              nan |                              nan |                               nan |                               nan |                                nan |                                nan |


## merge identical rows cellstr

### input

| trial_type   |   duration |   onset | stim_type   |
|:-------------|-----------:|--------:|:------------|
| house        |          1 |       3 | delete      |
| face         |          1 |       1 | delete      |
| face         |          1 |       2 | keep        |
| house        |          1 |       6 | keep        |
| chair        |          1 |       8 | keep        |
| house        |          1 |       4 | delete      |
| chair        |          1 |       7 | delete      |

### transformation 

```json
{
    "Instructions": {
        "Name": "MergeIdenticalRows",
        "Input": [
            "trial_type"
        ]
    },
    "Description": "merge identical rows cellstr"
}
```

### output 

| trial_type   |   duration |   onset | stim_type   |
|:-------------|-----------:|--------:|:------------|
| face         |          2 |       1 | keep        |
| house        |          4 |       3 | keep        |
| chair        |          2 |       7 | keep        |


## filter numeric

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Filter",
        "Input": "response_time",
        "Query": " response_time ~= 1.56"
    },
    "Description": "filter numeric"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |             1.5 |
|       4 |          2 |            1 | Unfamiliar face | Face         |             2   |
|       5 |          2 |            2 | Famous face     | Face         |           nan   |
|       8 |          2 |            2 | Unfamiliar face | Face         |             2.1 |


## replace regexp

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Replace",
        "Input": "familiarity",
        "Replace": {
            "key": ".*face",
            "value": "foo"
        }
    },
    "Description": "replace regexp"
}
```

### output 

|   onset |   duration |   repetition | familiarity   | trial_type   |   response_time |
|--------:|-----------:|-------------:|:--------------|:-------------|----------------:|
|       2 |          2 |            1 | foo           | Face         |            1.5  |
|       4 |          2 |            1 | foo           | Face         |            2    |
|       5 |          2 |            2 | foo           | Face         |            1.56 |
|       8 |          2 |            2 | foo           | Face         |            2.1  |


## filter string output across columns

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Filter",
        "Input": "onset",
        "Query": " familiarity == Famous face ",
        "Output": "new"
    },
    "Description": "filter string output across columns"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |   new |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |     2 |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |   nan |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |     5 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |   nan |


## and

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "And",
        "Input": [
            "sex_m",
            "age_gt_twenty"
        ],
        "Output": "men_gt_twenty"
    },
    "Description": "and"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   men_gt_twenty |
|--------:|:-------------|:------|----------------:|------:|----------------:|
|       1 | right        | M     |               1 |    21 |               1 |
|       1 | left         | M     |               0 |    18 |               0 |
|       0 | nan          | F     |               1 |    46 |               0 |
|       0 | left         | F     |               0 |    10 |               0 |
|       0 | right        | F     |               0 |   nan |               0 |


## replace with output

### input

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       2 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       5 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |

### transformation 

```json
{
    "Instructions": {
        "Name": "Replace",
        "Input": "familiarity",
        "Output": "tmp",
        "Replace": {
            "key": "Famous face",
            "value": 1
        },
        "Attribute": "all"
    },
    "Description": "replace with output"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time | tmp             |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|:----------------|
|       1 |          1 |            1 | Famous face     | Face         |            1.5  |                  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    | Unfamiliar face |
|       1 |          1 |            2 | Famous face     | Face         |            1.56 |                  |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  | Unfamiliar face |


## select

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Select",
        "Input": [
            "age"
        ]
    },
    "Description": "select"
}
```

### output 

|   age |
|------:|
|    21 |
|    18 |
|    46 |
|    10 |
|   nan |


## label identical rows

### input

| trial_type   |   stim_type | other_type   |
|:-------------|------------:|:-------------|
| face         |           1 | face         |
| face         |           1 |               |
| house        |           1 |               |
| house        |           2 |               |
| house        |         nan | nan          |
| house        |           5 | chair        |
| house        |           2 | chair        |
| chair        |         nan | nan          |

### transformation 

```json
{
    "Instructions": {
        "Name": "LabelIdenticalRows",
        "Input": [
            "trial_type",
            "stim_type",
            "other_type"
        ]
    },
    "Description": "label identical rows"
}
```

### output 

| trial_type   |   stim_type | other_type   |   trial_type_label |   stim_type_label |   other_type_label |
|:-------------|------------:|:-------------|-------------------:|------------------:|-------------------:|
| face         |           1 | face         |                  1 |                 1 |                  1 |
| face         |           1 |               |                  2 |                 2 |                  1 |
| house        |           1 |               |                  1 |                 3 |                  2 |
| house        |           2 |               |                  2 |                 1 |                  1 |
| house        |         nan | nan          |                  3 |                 1 |                  1 |
| house        |           5 | chair        |                  4 |                 1 |                  1 |
| house        |           2 | chair        |                  5 |                 1 |                  2 |
| chair        |         nan | nan          |                  1 |                 1 |                  1 |


## label identical rows cumulative

### input

| trial_type   |
|:-------------|
| face         |
| face         |
| house        |
| house        |
| face         |
| house        |
| chair        |

### transformation 

```json
{
    "Instructions": {
        "Name": "LabelIdenticalRows",
        "Input": [
            "trial_type"
        ],
        "Cumulative": true
    },
    "Description": "label identical rows cumulative"
}
```

### output 

| trial_type   |   trial_type_label |
|:-------------|-------------------:|
| face         |                  1 |
| face         |                  2 |
| house        |                  1 |
| house        |                  2 |
| face         |                  3 |
| house        |                  3 |
| chair        |                  1 |


## not

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Not",
        "Input": [
            "age_gt_twenty"
        ],
        "Output": "ager_lt_twenty"
    },
    "Description": "not"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   ager_lt_twenty |
|--------:|:-------------|:------|----------------:|------:|-----------------:|
|       1 | right        | M     |               1 |    21 |                0 |
|       1 | left         | M     |               0 |    18 |                1 |
|       0 | nan          | F     |               1 |    46 |                0 |
|       0 | left         | F     |               0 |    10 |                1 |
|       0 | right        | F     |               0 |   nan |                1 |


## merge identical rows numeric

### input

|   trial_type |   duration |   onset | stim_type   |
|-------------:|-----------:|--------:|:------------|
|            1 |          1 |       3 | keep        |
|            2 |          1 |       1 | delete      |
|            2 |          1 |       2 | keep        |
|          nan |          1 |       6 | keep        |
|            1 |          1 |       8 | keep        |
|            3 |          1 |       4 | keep        |
|            3 |          1 |       7 | keep        |

### transformation 

```json
{
    "Instructions": {
        "Name": "MergeIdenticalRows",
        "Input": [
            "trial_type"
        ]
    },
    "Description": "merge identical rows numeric"
}
```

### output 

|   trial_type |   duration |   onset | stim_type   |
|-------------:|-----------:|--------:|:------------|
|            2 |          2 |       1 | keep        |
|            1 |          1 |       3 | keep        |
|            3 |          1 |       4 | keep        |
|          nan |          1 |       6 | keep        |
|            3 |          1 |       7 | keep        |
|            1 |          1 |       8 | keep        |


## or

### input

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |
|--------:|:-------------|:------|----------------:|------:|
|       1 | right        | M     |               1 |    21 |
|       1 | left         | M     |               0 |    18 |
|       0 | nan          | F     |               1 |    46 |
|       0 | left         | F     |               0 |    10 |
|       0 | right        | F     |               0 |   nan |

### transformation 

```json
{
    "Instructions": {
        "Name": "Or",
        "Input": [
            "sex_m",
            "age_gt_twenty"
        ],
        "Output": "men_or_gt_twenty"
    },
    "Description": "or"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   men_or_gt_twenty |
|--------:|:-------------|:------|----------------:|------:|-------------------:|
|       1 | right        | M     |               1 |    21 |                  1 |
|       1 | left         | M     |               0 |    18 |                  1 |
|       0 | nan          | F     |               1 |    46 |                  1 |
|       0 | left         | F     |               0 |    10 |                  0 |
|       0 | right        | F     |               0 |   nan |                  0 |
