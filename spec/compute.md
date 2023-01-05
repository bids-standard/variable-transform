# Compute transformations



## product

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Product",
        "Input": [
            "onset",
            "duration"
        ],
        "Output": "onset_times_duration"
    },
    "Description": "product"
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   onset_times_duration |
|--------:|-----------:|:-------------|---------------:|-----------------------:|
|       2 |          2 | VisMot       |              1 |                      4 |
|       4 |          2 | VisStat      |              2 |                      8 |
|       6 |          2 | VisMot       |             -1 |                     12 |
|       8 |          2 | VisStat      |             -2 |                     16 |


## constant

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Constant",
        "Value": 2,
        "Output": "cst"
    },
    "Description": "constant"
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   cst |
|--------:|-----------:|:-------------|---------------:|------:|
|       2 |          2 | VisMot       |              1 |     2 |
|       4 |          2 | VisStat      |              2 |     2 |
|       6 |          2 | VisMot       |             -1 |     2 |
|       8 |          2 | VisStat      |             -2 |     2 |


## add coerce value

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Add",
        "Input": "onset",
        "Value": "3"
    },
    "Description": "add coerce value"
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       5 |          2 | VisMot       |           2 |
|       7 |          2 | VisStat      |          -4 |


## divide several inputs

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Divide",
        "Input": [
            "onset",
            "duration"
        ],
        "Value": 2
    },
    "Description": "divide several inputs"
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       1 |          1 | VisMot       |           2 |
|       2 |          1 | VisStat      |          -4 |


## basic to specific rows

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
        "Name": "Subtract",
        "Input": "onset",
        "Query": "response_time < 2",
        "Value": 1
    },
    "Description": "basic to specific rows"
}
```

### output 

|   onset |   duration |   repetition | familiarity     | trial_type   |   response_time |
|--------:|-----------:|-------------:|:----------------|:-------------|----------------:|
|       1 |          2 |            1 | Famous face     | Face         |            1.5  |
|       4 |          2 |            1 | Unfamiliar face | Face         |            2    |
|       4 |          2 |            2 | Famous face     | Face         |            1.56 |
|       8 |          2 |            2 | Unfamiliar face | Face         |            2.1  |


## subtract

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Subtract",
        "Input": "onset",
        "Value": 3
    },
    "Description": "subtract"
}
```

### output 

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|      -1 |          2 | VisMot       |           2 |
|       1 |          2 | VisStat      |          -4 |


## threshold

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Threshold": 1,
        "Binarize": true,
        "Above": true,
        "Signed": false
    },
    "Description": "threshold"
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              0 |
|       4 |          2 | VisStat      |              1 |
|       6 |          2 | VisMot       |              0 |
|       8 |          2 | VisStat      |              1 |


## scale nan after

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
[
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "Rescale": false,
            "Output": [
                "age_not_rescaled"
            ]
        },
        "Description": "scale nan after"
    },
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "Demean": false,
            "Output": [
                "age_not_demeaned"
            ]
        },
        "Description": "scale nan after"
    },
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "ReplaceNa": "after",
            "Rescale": false,
            "Output": [
                "age_not_rescaled_after"
            ]
        },
        "Description": "scale nan after"
    },
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "ReplaceNa": "after",
            "Demean": false,
            "Output": [
                "age_not_demeaned_after"
            ]
        },
        "Description": "scale nan after"
    }
]
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_not_rescaled |   age_not_demeaned |   age_not_rescaled_after |   age_not_demeaned_after |
|--------:|:-------------|:------|----------------:|------:|-------------------:|-------------------:|-------------------------:|-------------------------:|
|       1 | right        | M     |               1 |    21 |              -2.75 |           1.35109  |                    -2.75 |                 1.35109  |
|       1 | left         | M     |               0 |    18 |              -5.75 |           1.15808  |                    -5.75 |                 1.15808  |
|       0 | nan          | F     |               1 |    46 |              22.25 |           2.95954  |                    22.25 |                 2.95954  |
|       0 | left         | F     |               0 |    10 |             -13.75 |           0.643378 |                   -13.75 |                 0.643378 |
|       0 | right        | F     |               0 |   nan |             nan    |         nan        |                     0    |                 0        |


## power

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Power",
        "Input": "intensity",
        "Value": 3,
        "Output": "intensity_cubed"
    },
    "Description": "power"
}
```

### output 

|   onset |   duration | trial_type   |   intensity |   intensity_cubed |
|--------:|-----------:|:-------------|------------:|------------------:|
|       2 |          2 | VisMot       |           2 |                 8 |
|       4 |          2 | VisStat      |          -4 |               -64 |


## add subtract with output

### input

|   onset |   duration | trial_type   |   intensity |
|--------:|-----------:|:-------------|------------:|
|       2 |          2 | VisMot       |           2 |
|       4 |          2 | VisStat      |          -4 |

### transformation 

```json
{
    "Instructions": [
        {
            "Name": "Subtract",
            "Input": "onset",
            "Value": 3,
            "Output": "onset_minus_3"
        },
        {
            "Name": "Add",
            "Input": "onset",
            "Value": 1,
            "Output": "onset_plus_1"
        }
    ],
    "Description": "add subtract with output"
}
```

### output 

|   onset |   duration | trial_type   |   intensity |   onset_minus_3 |   onset_plus_1 |
|--------:|-----------:|:-------------|------------:|----------------:|---------------:|
|       2 |          2 | VisMot       |           2 |              -1 |              3 |
|       4 |          2 | VisStat      |          -4 |               1 |              5 |


## scale nan before

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
[
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "ReplaceNa": "before",
            "Output": [
                "age_before"
            ]
        },
        "Description": "scale nan before"
    },
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "ReplaceNa": "before",
            "Rescale": false,
            "Output": [
                "age_not_rescaled_before"
            ]
        },
        "Description": "scale nan before"
    },
    {
        "Instructions": {
            "Name": "Scale",
            "Input": [
                "age"
            ],
            "ReplaceNa": "before",
            "Demean": false,
            "Output": [
                "age_not_demeaned_before"
            ]
        },
        "Description": "scale nan before"
    }
]
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_before |   age_not_rescaled_before |   age_not_demeaned_before |
|--------:|:-------------|:------|----------------:|------:|-------------:|--------------------------:|--------------------------:|
|       1 | right        | M     |               1 |    21 |    0.116642  |                         2 |                  1.22474  |
|       1 | left         | M     |               0 |    18 |   -0.0583212 |                        -1 |                  1.04978  |
|       0 | nan          | F     |               1 |    46 |    1.57467   |                        27 |                  2.68277  |
|       0 | left         | F     |               0 |    10 |   -0.524891  |                        -9 |                  0.583212 |
|       0 | right        | F     |               0 |   nan |   -1.1081    |                       -19 |                  0        |


## scale

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
        "Name": "Scale",
        "Input": [
            "age"
        ],
        "Demean": true,
        "Rescale": true,
        "ReplaceNa": "off",
        "Output": [
            "age_demeaned_centered"
        ]
    },
    "Description": "scale"
}
```

### output 

|   sex_m | handedness   | sex   |   age_gt_twenty |   age |   age_demeaned_centered |
|--------:|:-------------|:------|----------------:|------:|------------------------:|
|       1 | right        | M     |               1 |    21 |               -0.176929 |
|       1 | left         | M     |               0 |    18 |               -0.369943 |
|       0 | nan          | F     |               1 |    46 |                1.43152  |
|       0 | left         | F     |               0 |    10 |               -0.884645 |
|       0 | right        | F     |               0 |   nan |              nan        |


## sum

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Sum",
        "Input": [
            "onset",
            "duration"
        ],
        "Weights": [
            2,
            1
        ],
        "Output": "onset_plus_duration_with_weight"
    },
    "Description": "sum"
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   onset_plus_duration_with_weight |
|--------:|-----------:|:-------------|---------------:|----------------------------------:|
|       2 |          2 | VisMot       |              1 |                                 6 |
|       4 |          2 | VisStat      |              2 |                                10 |
|       6 |          2 | VisMot       |             -1 |                                14 |
|       8 |          2 | VisStat      |             -2 |                                18 |


## threshold output

### input

|   onset |   duration | trial_type   |   to_threshold |
|--------:|-----------:|:-------------|---------------:|
|       2 |          2 | VisMot       |              1 |
|       4 |          2 | VisStat      |              2 |
|       6 |          2 | VisMot       |             -1 |
|       8 |          2 | VisStat      |             -2 |

### transformation 

```json
{
    "Instructions": {
        "Name": "Threshold",
        "Input": "to_threshold",
        "Output": "tmp"
    },
    "Description": "threshold output"
}
```

### output 

|   onset |   duration | trial_type   |   to_threshold |   tmp |
|--------:|-----------:|:-------------|---------------:|------:|
|       2 |          2 | VisMot       |              1 |     1 |
|       4 |          2 | VisStat      |              2 |     2 |
|       6 |          2 | VisMot       |             -1 |     0 |
|       8 |          2 | VisStat      |             -2 |     0 |
